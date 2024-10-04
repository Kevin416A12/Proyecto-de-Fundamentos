import time
from machine import Pin

led = Pin(25, Pin.OUT)

while 1:
    led.low()
    time.sleep(0.25)
    led.high()
    time.sleep(0.25)