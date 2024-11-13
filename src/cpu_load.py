#!/usr/bin/env python
import time
import psutil
import blinkt
from config import get_config
from show_graph import show_graph

ConfigCpu = get_config('BLINKT_CPU')

blinkt.set_clear_on_exit()
blinkt.set_brightness(ConfigCpu.brightness)

while True:
    v = psutil.cpu_percent(interval=ConfigCpu.interval) / 100.0
    show_graph(v, ConfigCpu.r, ConfigCpu.g, ConfigCpu.b)
    time.sleep(0.01)
