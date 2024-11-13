# rpi-docker-blinkt

sudo docker run --rm --privileged --device /dev/gpiomem rpi-docker-blinkt

> without privileged, RPi.GPIO complains about "RuntimeError: This module can only be run on a Raspberry Pi!"

default is cpu_load

Variants:
- mem_load

add python mem_load.py to the docker run command.

## load.py

sudo docker run --rm --privileged --device /dev/gpiomem \
-e BLINKT_MEM_RGBHEX_R=255 \
-e BLINKT_MEM_RGBHEX_G=0 \
-e BLINKT_MEM_RGBHEX_B=0 \
-e BLINKT_CPU_RGBHEX_R=0 \
-e BLINKT_CPU_RGBHEX_G=0 \
-e BLINKT_CPU_RGBHEX_B=255 \
rpi-docker-blinkt python load.py

## Simulate Load

### mem_load

```
sudo stress --vm 4 --vm-bytes 256M --vm-keep
```

### cpu_load

```
sudo stress --cpu 2
```