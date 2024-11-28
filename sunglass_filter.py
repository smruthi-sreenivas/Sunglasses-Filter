# Import libraries
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

import matplotlib
matplotlib.rcParams['figure.figsize'] = (6.0, 6.0)
matplotlib.rcParams['image.cmap'] = 'gray'

window = 'Sunglass Filter'
#video capture object
cap = cv2.VideoCapture(0)
#detect faces
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#detect eye region
eyeCascade = cv2.CascadeClassifier('frontalEyes35x16.xml')
#read goggles image
goggles = cv2.imread('sunglass.png',-1)
#read high contrast image to add reflection on the glass
scenery = cv2.imread('sunglass filter_reflection.jpeg')
#convet to grayscale
scenery_gray = cv2.cvtColor(scenery,cv2.COLOR_BGR2GRAY)
scenery_gray = cv2.merge((scenery_gray, scenery_gray, scenery_gray))

gogglesBGR = goggles[:,:,:3]
gogglesMask = goggles[:,:,3]
# Make the dimensions of the mask same as the input image.
# Since Face Image is a 3-channel image, we create a 3 channel image for the mask
gogglesMask = cv2.merge((gogglesMask, gogglesMask, gogglesMask))
# Set the opacity of the eye. Otherwise eyes become more visible
opacity = 0.3  # Adjust this value between 0 and 1
opacity_scenery = 0.4

while cap.isOpened():
    #read the frame
    value, frame = cap.read()
    # convert the frame to gray
    imgGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #face detection
    faces = faceCascade.detectMultiScale(imgGray,scaleFactor = 1.2, minNeighbors= 10)
    for (x,y,w,h) in faces:
       # cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        faceGray = imgGray[y:(y+h),x:(x+w)]
        faceROI = frame[y:(y+h),x:(x+w)]
        eyes = eyeCascade.detectMultiScale(faceGray,scaleFactor= 1.1,minNeighbors= 5)
        for (ex,ey,ew,eh) in eyes:
           # cv2.rectangle(faceROI,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
            eyesROI = faceROI[ey:ey+eh, ex:ex+ew]
            #resize goggles and mask to fit over eye region
            # resizedGoggles = cv2.resize(goggles, (ew, eh))
            resizedGogglesMask = cv2.resize(gogglesMask,(ew,eh)) #white glass
            resizedGogglesBGR = cv2.resize(gogglesBGR,(ew,eh))
            resizedScenery = cv2.resize(scenery_gray,(ew,eh))

            #masked eye region
            # Make the values [0,1] since we are using arithmetic operations
            normGogglesMask = np.uint8(resizedGogglesMask / 255)
            # print(normGogglesMask.max(axis=(0, 1)))
            # print(normGogglesMask.min(axis=(0, 1)))
            #apply opacity. otherwise glass becomes too light
            opacityGogglesMask = np.float32(normGogglesMask * opacity)
            # print(opacityGogglesMask.max(axis=(0, 1)))
            # print(opacityGogglesMask.min(axis=(0, 1)))
            invMask = 1-(normGogglesMask) #blk glass

            maskedEye = cv2.multiply(eyesROI.astype(np.float32),opacityGogglesMask).astype(np.uint8)
            # add some reflections on sunglasses for more reality
            maskedGoggles = cv2.multiply(resizedGogglesBGR, normGogglesMask)
            #masked scenery
            gogglesAndScenery = cv2.multiply(normGogglesMask.astype(np.float32),opacity_scenery*resizedScenery.astype(np.float32)).astype(np.uint8)
            aroundEye = cv2.multiply(eyesROI, invMask)

            eye_glass = cv2.add(maskedEye,maskedGoggles)
            add_scenery = cv2.add(eye_glass,gogglesAndScenery)

            eye_total = cv2.add(aroundEye,add_scenery)
            faceROI[ey:ey+eh, ex:ex+ew] = eye_total
            cv2.imshow('eye',add_scenery)

    if value:
        cv2.imshow(window,frame)
        if cv2.waitKey(1) & 0xFF == 27: #27 ASCII for esc
            break

cap.release()
cv2.destroyAllWindows()



