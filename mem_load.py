#!/usr/bin/env python

import time
import psutil
import blinkt
from config import get_config

Config = get_config()

blinkt.set_clear_on_exit()
blinkt.set_brightness(Config.brightness)

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
    v = psutil.virtual_memory().percent / 100.0
    show_graph(v, Config.r, Config.g, Config.b)
    time.sleep(0.01)