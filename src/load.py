#!/usr/bin/env python

import time
import psutil
import blinkt
from config import get_config
from show_graph import show_graph

Config = get_config()
ConfigMem = get_config('BLINKT_MEM')
ConfigCpu = get_config('BLINKT_CPU')

blinkt.set_clear_on_exit()
blinkt.set_brightness(Config.brightness)

while True:
    for i in range(1, 101):
        mem = psutil.virtual_memory().percent / 100.0
        show_graph(mem, ConfigMem.r, ConfigMem.g, ConfigMem.b)
        time.sleep(0.01)
    for i in range(1, 101):
        cpu = psutil.cpu_percent() / 100.0
        show_graph(cpu, ConfigCpu.r, ConfigCpu.g, ConfigCpu.b)
        time.sleep(0.01)