# rpi-docker-blinkt

sudo docker run --rm --privileged --device /dev/gpiomem rpi-docker-blinkt

> without privileged, RPi.GPIO complains about "RuntimeError: This module can only be run on a Raspberry Pi!"

default is cpu_load

Variants:
- mem_load.py

add variant to the docker run command.

## cpu_load.py

sudo docker run --rm --privileged --device /dev/gpiomem \
-e BLINKT_CPU_RGBHEX_R=0 \
-e BLINKT_CPU_RGBHEX_G=0 \
-e BLINKT_CPU_RGBHEX_B=255 \
-e BLINKT_CPU_INTERVAL=0.1 \
rpi-docker-blinkt

## mem_load.py

```
sudo docker run --rm --privileged --device /dev/gpiomem \
-e BLINKT_MEM_RGBHEX_R=255 \
-e BLINKT_MEM_RGBHEX_G=0 \
-e BLINKT_MEM_RGBHEX_B=0 \
rpi-docker-blinkt python mem_load.py
```

## load.py

sudo docker run --rm --privileged --device /dev/gpiomem \
-e BLINKT_MEM_RGBHEX_R=255 \
-e BLINKT_MEM_RGBHEX_G=0 \
-e BLINKT_MEM_RGBHEX_B=0 \
-e BLINKT_CPU_RGBHEX_R=0 \
-e BLINKT_CPU_RGBHEX_G=0 \
-e BLINKT_CPU_RGBHEX_B=255 \
-e BLINKT_MODE_CYCLE_COUNT=50 \
-e BLINKT_CPU_INTERVAL=0.2 \
rpi-docker-blinkt python load.py

## Simulate Load

### mem_load

```
sudo stress --vm 1 --vm-bytes 756M --vm-keep
```

### cpu_load

```
sudo stress --cpu 2
```