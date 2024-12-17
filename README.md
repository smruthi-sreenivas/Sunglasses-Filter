# Sunglass Filter Project

This project applies a virtual sunglass effect to real-time webcam footage using OpenCV and Python. It detects the user's eyes and overlays a sunglass image, complete with reflections for a more realistic look.
![{90EA4BF0-E81B-449D-8D44-A2E29869FAE5}](https://github.com/user-attachments/assets/b7e59853-b26b-4b59-8a9f-93a32930047c)

## Features
- Real-time face and eye detection using Haar cascades.
- Sunglass overlay applied to detected eye regions.
- Adjustable opacity for both the sunglass and the reflection for realism.
- Simple implementation with OpenCV for image processing.

## Requirements
- Python 3.x
- OpenCV
- NumPy
- Matplotlib

## Setup
1. Clone this repository or download the script.
2. Ensure the following files are in the same directory as the script:
   - `haarcascade_frontalface_default.xml` (for face detection)
   - `frontalEyes35x16.xml` (for eye region detection)
   - `sunglass.png` (sunglass image with an alpha channel for transparency)
   - `sunglass filter_reflection.jpeg` (high-contrast image for glass reflection)
3. Install the required Python libraries:
   ```bash
   pip install opencv-python numpy matplotlib
   ```

## Usage
1. Run the script:
   ```bash
   python sunglass_filter.py
   ```
2. A webcam feed will open in a new window with the sunglass effect applied.
3. Press `Esc` to exit the application.

## Code Explanation
1. **Video Capture**: Captures frames from the webcam.
2. **Face and Eye Detection**:
   - Detects faces using `haarcascade_frontalface_default.xml`.
   - Within detected faces, locates eye regions using `frontalEyes35x16.xml`.
3. **Sunglass Overlay**:
   - Resizes the sunglass image and its mask to fit the detected eye region.
   - Blends the sunglass image with the eye region, applying a reflection effect using an additional image.
   - Adjusts opacity for both the sunglass and reflection layers for realism.

## Key Parameters
- `opacity`: Controls the transparency of the sunglass.
- `opacity_scenery`: Adjusts the intensity of the reflection on the sunglass.

## Example Output
The application overlays a realistic sunglass effect onto the detected eyes in the video feed. Reflections on the glass are dynamically added using a high-contrast scenery image, enhancing the realism of the filter.

## Troubleshooting
- Ensure your webcam is properly connected.
- Verify the required XML files and images are present in the working directory.
- If detection fails, ensure adequate lighting and adjust the parameters `scaleFactor` and `minNeighbors` in the Haar cascade detectors.

## Acknowledgments
- OpenCV for providing robust image processing tools.
- Haar cascades for pre-trained face and eye detection.

