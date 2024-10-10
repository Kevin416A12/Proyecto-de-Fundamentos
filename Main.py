import machine
import time


led = machine.Pin(25, machine.Pin.OUT)


boton_pines = [machine.Pin(pin, machine.Pin.IN, machine.Pin.PULL_DOWN) for pin in [2, 3, 4, 5, 6]]

while True:

    for boton in boton_pines:
        if boton.value() == 1:
            led.on()
            time.sleep(5)
        else:
            led.off()
    time.sleep(6)

    