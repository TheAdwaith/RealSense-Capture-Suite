from .base_camera import BaseCamera
import cv2
import numpy as np
from datetime import datetime

class InfraredCamera(BaseCamera):
    def process_frames(self, frames):
        """Process infrared frames"""
        infrared_frame1 = frames.get_infrared_frame(1)
        infrared_frame2 = frames.get_infrared_frame(2)
        
        if infrared_frame1 and infrared_frame2:
            infrared_image1 = np.asanyarray(infrared_frame1.get_data())
            infrared_image2 = np.asanyarray(infrared_frame2.get_data())
            concatenated = np.concatenate((infrared_image1, infrared_image2), axis=1)
            return {
                'frame1': infrared_image1,
                'frame2': infrared_image2,
                'concatenated': concatenated
            }
        return None
    
    def display_frames(self, processed_data):
        """Display infrared frames"""
        if processed_data:
            cv2.imshow('Infrared Streams', processed_data['concatenated'])
    
    def save_frames(self, processed_data):
        """Save infrared frames"""
        if processed_data:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            frame_filename1 = f"{self.save_dir}/infrared_frame1_{timestamp}.jpg"
            frame_filename2 = f"{self.save_dir}/infrared_frame2_{timestamp}.jpg"
            
            cv2.imwrite(frame_filename1, processed_data['frame1'])
            cv2.imwrite(frame_filename2, processed_data['frame2'])
            
            print(f"Saved infrared frame 1: {frame_filename1}")
            print(f"Saved infrared frame 2: {frame_filename2}")
            
            self.frame_count += 1