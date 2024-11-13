
import os
from collections import namedtuple

Config = namedtuple('Config', 'r g b brightness interval')

def get_config(prefix="BLINKT"):
    r = int(os.getenv(prefix+"_RGBHEX_R", "255"))
    g = int(os.getenv(prefix+"_RGBHEX_G", "255"))
    b = int(os.getenv(prefix+"_RGBHEX_B", "255"))

    for c in [r, g, b]:
        if c < 0 or c > 255:
            exit('RGB values must be between 0 and 255')

    brightness = float(os.getenv(prefix+"_BRIGHTNESS", "0.05"))
    if brightness < 0 or brightness > 1:
        exit('Brightness must be float between 0 and 1. Lowest is 0.05')

    interval = float(os.getenv(prefix+"_INTERVAL", "0.0"))
    if interval < 0 or interval > 1:
        exit('Interval must be float greater than 0 and less than 1')

    return Config(r, g, b, brightness, interval)