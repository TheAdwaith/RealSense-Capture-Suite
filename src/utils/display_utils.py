import cv2

def display_image(window_name, image):
    """Display an image in a window"""
    cv2.imshow(window_name, image)

def handle_keypress():
    """Handle keyboard input and return the key pressed"""
    return cv2.waitKey(1) & 0xFF