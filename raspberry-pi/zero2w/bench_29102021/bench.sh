#!/bin/bash

for i in {1..5}; do
  sysbench --test=cpu --cpu-max-prime=1000 --num-threads=4 run > /home/pi/measurements_${i}.txt
done
