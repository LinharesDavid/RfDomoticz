#!/bin/sh
echo "send $1" | nc raspsignals.home 6666 -c
