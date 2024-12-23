#!/usr/bin/env python

import time
import psutil
import blinkt
from config import get_config
from show_graph import show_graph

Config = get_config('BLINKT_MEM')

blinkt.set_clear_on_exit()
blinkt.set_brightness(Config.brightness)

while True:
    v = psutil.virtual_memory().percent / 100.0
    show_graph(v, Config.r, Config.g, Config.b)
    time.sleep(0.01)