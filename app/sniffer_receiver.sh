#!/bin/sh
echo "sniffer" | nc raspberrypi.local 6666 -c
nc -l raspberrypi.local -p 6666
