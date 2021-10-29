#!/usr/bin/env python3

import sys
import os
import time
from vcgencmd import Vcgencmd

def main():
    start_time = time.time()
    f = open("/home/pi/measurements.txt","a+")
    print("Elapsed Time (s),Temperature (°C),Clock Speed (MHz),Voltage Core (V)")
    f.write("Elapsed Time (s),Temperature (°C),Clock Speed (MHz),Voltage Core (V)\n")
    vc = Vcgencmd()
    while True:
        clock = int(vc.measure_clock('arm')/1000000)
        string = '%.0f,%s,%s,%s\n' % ((time.time() - start_time),vc.measure_temp(),clock,vc.measure_volts('core'))
        print(string, end='')
        f.write(string)
        time.sleep(1)

if __name__ == '__main__':
    main()
