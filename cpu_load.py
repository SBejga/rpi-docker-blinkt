#!/usr/bin/env python
import time
import os
from sys import exit

try:
    import psutil
except ImportError:
    exit('This script requires the psutil module\nInstall with: sudo apt install python3-psutil')

r = int(os.getenv("BLINKT_RGBHEX_R", "255"))
g = int(os.getenv("BLINKT_RGBHEX_G", "255"))
b = int(os.getenv("BLINKT_RGBHEX_B", "255"))

for c in [r, g, b]:
    if c < 0 or c > 255:
        exit('RGB values must be between 0 and 255')

brightness = float(os.getenv("BLINKT_BRIGHTNESS", "0.05"))
if brightness < 0 or brightness > 1:
    exit('Brightness must be float between 0 and 1. Lowest is 0.05')

import blinkt

blinkt.set_clear_on_exit()
blinkt.set_brightness(brightness)


def show_graph(v, r, g, b):
    v *= blinkt.NUM_PIXELS
    for x in range(blinkt.NUM_PIXELS):
        if v < 0:
            r, g, b = 0, 0, 0
        else:
            r, g, b = [int(min(v, 1.0) * c) for c in [r, g, b]]
        blinkt.set_pixel(x, r, g, b)
        v -= 1

    blinkt.show()

while True:
    v = psutil.cpu_percent() / 100.0
    show_graph(v, r, g, b)
    time.sleep(0.01)
