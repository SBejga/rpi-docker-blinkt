#!/usr/bin/env python

import time
import psutil
import blinkt
import os
from config import get_config
from show_graph import show_graph

ConfigMem = get_config('BLINKT_MEM')
ConfigCpu = get_config('BLINKT_CPU')

blinkt.set_clear_on_exit()

mode_cycle_cound = int(os.getenv('BLINKT_MODE_CYCLE_COUNT', 100))+1

while True:
    blinkt.set_brightness(ConfigMem.brightness)
    for i in range(1, mode_cycle_cound):
        mem = psutil.virtual_memory().percent / 100.0
        show_graph(mem, ConfigMem.r, ConfigMem.g, ConfigMem.b)
        time.sleep(0.01)
    
    blinkt.set_brightness(ConfigCpu.brightness)
    for i in range(1, mode_cycle_cound):
        cpu = psutil.cpu_percent(interval=ConfigCpu.interval) / 100.0
        show_graph(cpu, ConfigCpu.r, ConfigCpu.g, ConfigCpu.b)
        time.sleep(0.01)