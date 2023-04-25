import os
from datetime import datetime

def ensure_directory(directory_path):
    """Create directory if it doesn't exist"""
    os.makedirs(directory_path, exist_ok=True)
    return directory_path

def generate_filename(directory, base_name, extension="jpg"):
    """Generate a timestamped filename"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    return f"{directory}/{base_name}_{timestamp}.{extension}"