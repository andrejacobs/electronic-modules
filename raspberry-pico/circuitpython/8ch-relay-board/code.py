# Test to control an 8Ch relay module from a Raspberry Pi Pico
# Copyright (C) 2023. Andre Jacobs. All rights reserved.
# License: MIT
# CircuitPython (v8)
import board
import time
from digitalio import DigitalInOut, Direction #, Pull

def setup_relay_pin(pin):
    gpio = DigitalInOut(pin)
    gpio.direction = Direction.OUTPUT
    # gpio.pull = Pull.UP (not used when OUTPUT)
    return gpio

def toggle(gpio, id):
    newValue = not gpio.value
    print(f"switching {id} from {gpio.value} to {newValue}")
    gpio.value = newValue

# Note, I am only testing 4 channels at the moment via a 5v <-> 3.3v logic level converter (Sparkfun BOB-12009)
r1 = setup_relay_pin(board.GP16)
r2 = setup_relay_pin(board.GP17)
r3 = setup_relay_pin(board.GP18)
r4 = setup_relay_pin(board.GP19)

while True:
    toggle(r1, "Channel 1")
    time.sleep(1)
    toggle(r2, "Channel 2")
    time.sleep(1)
    toggle(r3, "Channel 3")
    time.sleep(1)
    toggle(r4, "Channel 4")
    time.sleep(1)
