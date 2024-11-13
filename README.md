# rpi-docker-blinkt

sudo docker run --rm --privileged --device /dev/gpiomem rpi-docker-blinkt

> without privileged, RPi.GPIO complains about "RuntimeError: This module can only be run on a Raspberry Pi!"