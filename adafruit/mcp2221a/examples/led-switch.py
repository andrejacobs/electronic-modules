import board
import digitalio

led = digitalio.DigitalInOut(board.G0)
led.direction = digitalio.Direction.OUTPUT

button = digitalio.DigitalInOut(board.G1)
button.direction = digitalio.Direction.INPUT

while True:
    led.value = button.value