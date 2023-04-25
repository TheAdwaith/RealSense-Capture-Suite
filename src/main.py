import argparse
from cameras.infrared_camera import InfraredCamera
from cameras.color_camera import ColorCamera
from config.camera_config import INFRARED_CONFIG, COLOR_CONFIG

def main():
    parser = argparse.ArgumentParser(description='RealSense Camera Capture')
    parser.add_argument('--mode', type=str, choices=['infrared', 'color'], 
                       default='infrared', help='Camera mode')
    parser.add_argument('--save-dir', type=str, 
                       default='scripts/test_images_rr', help='Directory to save images')
    
    args = parser.parse_args()
    
    if args.mode == 'infrared':
        camera = InfraredCamera(INFRARED_CONFIG, args.save_dir)
        print("Starting infrared camera. Press 's' to save, 'e' to toggle emitter, 'q' to quit")
    else:
        camera = ColorCamera(COLOR_CONFIG, args.save_dir)
        print("Starting color camera. Press 's' to save, 'q' to quit")
    
    camera.run()

if __name__ == "__main__":
    main()