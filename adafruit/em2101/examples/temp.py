import time
import board
from adafruit_emc2101 import EMC2101

i2c = board.I2C()
emc = EMC2101(i2c)

while True:
    print("Internal temperature:", emc.internal_temperature, "C")
    time.sleep(0.5)
