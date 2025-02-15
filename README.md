Object Measurement using YOLOv8 and MiDaS Depth Estimation

Overview
# Object Measurement using YOLOv8 and MiDaS Depth Estimation

## Overview
This project utilizes **YOLOv8** for object detection and **MiDaS** for depth estimation to measure object dimensions in real-time using a webcam. The system detects objects, estimates their dimensions, and provides depth measurements for enhanced accuracy.

## Features
- **Real-time Object Detection**: Uses **YOLOv8x** for high-accuracy object detection.
- **Depth Estimation**: Utilizes **MiDaS (DPT-Large)** for depth perception.
- **Measurement Calculation**: Calculates object width, height, and depth in centimeters.
- **Dynamic Reference Selection**: Click on an object to set it as the reference for scaling.
- **Optimized for Performance**: Implements preprocessing for better contour detection.

## Installation
### Prerequisites
Ensure you have Python **3.8+** installed. Install dependencies using:

```sh
pip install -r requirements.txt
```

### Required Dependencies
- **OpenCV**
- **PyTorch**
- **Ultralytics YOLO**
- **MiDaS depth estimation**
- **NumPy**

## Usage
### Running the Script
Run the object measurement script with:

```sh
python object_dimensions.py
```

### Controls
- **Click on the window** to reset the reference object.
- **Press 'q'** to exit the application.

## How It Works
1. **Captures video feed** from a webcam.
2. **Runs YOLOv8x** to detect objects in each frame.
3. **Applies MiDaS depth estimation** to compute depth values.
4. **Calculates real-world dimensions** based on a reference object.
5. **Displays bounding boxes** and dimension labels on detected objects.

## Troubleshooting
- **MiDaS shape mismatch error**: Ensure proper tensor transformation in `estimate_depth()`.
- **No depth values detected**: Check if the camera input is clear and well-lit.
- **Reference object issues**: Click on a stable object for accurate calibration.

## Future Improvements
- **Stereo Camera Support** for improved depth accuracy.
- **LiDAR Integration** for advanced distance measurement.
- **Drone Compatibility** to extend real-world use cases.

## License
This project is licensed under the MIT License.

## Contributing
Pull requests and contributions are welcome. Feel free to open an issue for suggestions or improvements.

## Author
Developed by **Sree Charan**. Feel free to reach out for collaboration!


Real-time Object Detection: Uses YOLOv8x for high-accuracy object detection.

Depth Estimation: Utilizes MiDaS (DPT-Large) for depth perception.

Measurement Calculation: Calculates object width, height, and depth in centimeters.

Dynamic Reference Selection: Click on an object to set it as the reference for scaling.

Optimized for Performance: Implements preprocessing for better contour detection.

Installation

Prerequisites

Ensure you have Python 3.8+ installed. Install dependencies using:

pip install -r requirements.txt

Required Dependencies

OpenCV

PyTorch

Ultralytics YOLO

MiDaS depth estimation

NumPy

Usage

Running the Script

Run the object measurement script with:

python object_dimensions.py

Controls

Click on the window to reset the reference object.

Press 'q' to exit the application.

How It Works

Captures video feed from a webcam.

Runs YOLOv8x to detect objects in each frame.

Applies MiDaS depth estimation to compute depth values.

Calculates real-world dimensions based on a reference object.

Displays bounding boxes and dimension labels on detected objects.

Troubleshooting

MiDaS shape mismatch error: Ensure proper tensor transformation in estimate_depth().

No depth values detected: Check if the camera input is clear and well-lit.

Reference object issues: Click on a stable object for accurate calibration.

Future Improvements

Stereo Camera Support for improved depth accuracy.

LiDAR Integration for advanced distance measurement.

Drone Compatibility to extend real-world use cases.

License

This project is licensed under the MIT License.

Contributing

Pull requests and contributions are welcome. Feel free to open an issue for suggestions or improvements.
