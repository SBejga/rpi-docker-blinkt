
import os
from collections import namedtuple

Config = namedtuple('Config', 'r g b brightness')

def get_config():
    r = int(os.getenv("BLINKT_RGBHEX_R", "255"))
    g = int(os.getenv("BLINKT_RGBHEX_G", "255"))
    b = int(os.getenv("BLINKT_RGBHEX_B", "255"))

    for c in [r, g, b]:
        if c < 0 or c > 255:
            exit('RGB values must be between 0 and 255')

    brightness = float(os.getenv("BLINKT_BRIGHTNESS", "0.05"))
    if brightness < 0 or brightness > 1:
        exit('Brightness must be float between 0 and 1. Lowest is 0.05')

    return Config(r, g, b, brightness)