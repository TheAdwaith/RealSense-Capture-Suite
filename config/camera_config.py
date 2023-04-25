# Camera configuration settings
INFRARED_CONFIG = {
    'streams': [
        {
            'type': 'infrared',
            'index': 1,
            'width': 640,
            'height': 480,
            'format': 'y8',
            'fps': 30
        },
        {
            'type': 'infrared',
            'index': 2,
            'width': 640,
            'height': 480,
            'format': 'y8',
            'fps': 30
        }
    ]
}

COLOR_CONFIG = {
    'streams': [
        {
            'type': 'color',
            'width': 640,
            'height': 480,
            'format': 'bgr8',
            'fps': 30
        }
    ]
}