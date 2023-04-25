import pyrealsense2 as rs
import numpy as np
import cv2
from abc import ABC, abstractmethod
import os
from datetime import datetime

class BaseCamera(ABC):
    def __init__(self, config, save_dir="scripts/test_images_rr"):
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.frame_count = 0
        self.save_dir = save_dir
        self.setup_config(config)
        
        # Create save directory if it doesn't exist
        os.makedirs(save_dir, exist_ok=True)
        
    def setup_config(self, config):
        """Setup the camera configuration"""
        for stream_config in config['streams']:
            self.config.enable_stream(
                getattr(rs.stream, stream_config['type']),
                stream_config.get('index', 0),
                stream_config['width'],
                stream_config['height'],
                getattr(rs.format, stream_config['format']),
                stream_config['fps']
            )
    
    def start(self):
        """Start the camera pipeline"""
        self.profile = self.pipeline.start(self.config)
        self.setup_sensor_options()
        
    def setup_sensor_options(self):
        """Setup sensor options like emitter"""
        try:
            device = self.profile.get_device()
            self.depth_sensor = device.first_depth_sensor()
            if self.depth_sensor:
                self.depth_sensor.set_option(rs.option.emitter_enabled, 0)
                self.emitter_enabled = False
                print("Laser sensor disabled.")
        except RuntimeError:
            self.depth_sensor = None
            print("No depth sensor available for emitter control")
    
    def toggle_emitter(self):
        """Toggle the emitter state"""
        if self.depth_sensor:
            self.emitter_enabled = not self.emitter_enabled
            self.depth_sensor.set_option(
                rs.option.emitter_enabled, 
                1 if self.emitter_enabled else 0
            )
            print(f"Laser sensor {'enabled' if self.emitter_enabled else 'disabled'}")
        else:
            print("Emitter control not available")
    
    @abstractmethod
    def process_frames(self, frames):
        """Process frames - to be implemented by subclasses"""
        pass
    
    @abstractmethod
    def display_frames(self, processed_data):
        """Display frames - to be implemented by subclasses"""
        pass
    
    def run(self):
        """Main run loop"""
        self.start()
        
        try:
            while True:
                frames = self.pipeline.wait_for_frames()
                processed_data = self.process_frames(frames)
                
                if processed_data:
                    self.display_frames(processed_data)
                
                key = cv2.waitKey(1) & 0xFF
                self.handle_key_input(key, processed_data)
                
                if key == ord('q'):
                    break
                    
        finally:
            self.cleanup()
    
    def handle_key_input(self, key, processed_data):
        """Handle keyboard input"""
        if key == ord('s') and processed_data:
            self.save_frames(processed_data)
        elif key == ord('e'):
            self.toggle_emitter()
    
    @abstractmethod
    def save_frames(self, processed_data):
        """Save frames - to be implemented by subclasses"""
        pass
    
    def cleanup(self):
        """Cleanup resources"""
        cv2.destroyAllWindows()
        self.pipeline.stop()
        print("Camera resources released.")