#!/bin/sh
echo "sniffer" | nc raspsignals.home 6666 -c
nc -l raspsignals.home -p 6666
