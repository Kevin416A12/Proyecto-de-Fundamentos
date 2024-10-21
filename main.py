import machine
import time
import utime

# Pines de Salida
led = machine.Pin("LED", machine.Pin.OUT)
led_jugador_1 = machine.Pin(22, machine.Pin.OUT)
led_jugador_2 = machine.Pin(27, machine.Pin.OUT)
AB = machine.Pin(18, machine.Pin.OUT)
CLK = machine.Pin(19, machine.Pin.OUT)

# Pines de entrada
boton_cambio = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_100 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_150 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_200 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_250 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_500 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)

potenciometro = machine.ADC(machine.Pin(26))


def clock_pulse():
    CLK.on()
    time.sleep(0.01)  # Pequeño retardo para permitir el cambio
    CLK.off()


def shift_bit(bit):
    if bit == 1:
        AB.on()  # Ambas entradas en 1 para desplazar un 1
    else:
        AB.off()  # Ambas entradas en 0 para desplazar un 0
    clock_pulse()  # Enviar pulso de reloj para desplazar el bit

lista = [0,1,0,1,1,0,1,1]

def boton_pulsado():
    for i in lista:
        shift_bit(i)  # Desplaza un bit '1' al registro
        time.sleep(0.5)  # Espera medio segundo entre cada LED
    limpiar()


def limpiar(): # la funcion llena el registro de ceros para apagar todos los led
    for i in range(8):
        shift_bit(0)  # Desplaza un bit '0' al registro
        time.sleep(0.5)  # Espera medio segundo entre cada LED


limpiar()
while True:
    if boton_500.value() == 1:

        boton_pulsado()
        led_jugador_1.off()
        time.sleep(4)

    else:
        led_jugador_1.on()