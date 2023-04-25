# RealSense Camera Capture

A modular, object-oriented Python application for capturing images from Intel RealSense cameras.

## Features

- Capture from both infrared and color cameras
- Toggle laser emitter (for infrared mode)
- Save images with timestamped filenames
- Clean, modular codebase with OOP principles
- Configurable through command-line arguments

## Installation

1. Install Intel RealSense SDK: https://github.com/IntelRealSense/librealsense
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install as a package:
   ```bash
   python setup.py install
   ```

## Usage

Run the infrared camera:
```bash
python src/main.py --mode infrared
```

Run the color camera:
```bash
python src/main.py --mode color
```

Specify a custom save directory:
```bash
python src/main.py --mode infrared --save-dir /path/to/save/directory
```

## Controls

- Press 's' to save current frames
- Press 'e' to toggle laser emitter (infrared mode only)
- Press 'q' to quit the application

## Project Structure

```
realsense-capture/
├── src/                 # Source code
│   ├── cameras/        # Camera implementations
│   ├── utils/          # Utility functions
│   └── main.py         # Main application
├── config/             # Configuration files
├── scripts/            # Scripts and test images
├── requirements.txt    # Python dependencies
├── setup.py           # Package installation script
└── README.md          # Project documentation
```