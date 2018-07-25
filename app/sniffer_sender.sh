#!/bin/sh
echo "send $1" | nc raspberrypi.local 6666 -c
