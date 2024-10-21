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
boton_100 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN)  # A
boton_150 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN)  # G
boton_200 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)  # B
boton_250 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)  # C
boton_500 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)  # D

potenciometro = machine.ADC(machine.Pin(26))
lista_prueba = [0, 0, 0, 0, 0, 0, 0, 1]
lista_100 = [0, 0, 0, 0, 0, 0, 0, 1]
lista_150 = [0, 1, 1, 1, 0, 0, 0, 0]
lista_200 = [0, 0, 0, 0, 0, 0, 1, 0]
lista_250 = [0, 0, 0, 0, 0, 1, 0, 0]
lista_500 = [0, 0, 0, 0, 1, 0, 0, 0]


def clock_pulse():
    CLK.on()
    time.sleep(0.01)  # Pequeño retardo para permitir el cambio
    CLK.off()


def shift_bit(bit):
    if bit == 1:
        AB.on()  # Ambas entradas en 1 para desplazar un 1
    elif bit == 0:
        AB.off()  # Ambas entradas en 0 para desplazar un 0
    clock_pulse()  # Enviar pulso de reloj para desplazar el bit


def boton_pulsado(lista):
    print("si")
    for i in lista:
        shift_bit(i)  # Desplaza un bit '1' al registro
        time.sleep(0.01)  # Espera medio segundo entre cada LED
    time.sleep(2)
    limpiar()


def limpiar():
    for i in range(8):
        shift_bit(0)  # Desplaza un bit '0' al registro
        # Espera medio segundo entre cada LED
    print("Limpio")


limpiar()
while True:
    if boton_cambio.value() == 1:
        boton_pulsado(lista_150)
        led_jugador_1.off()
        time.sleep(1)
    if boton_100.value() == 1:
        boton_pulsado(lista_100)
        led_jugador_1.off()
        time.sleep(1)
    if boton_150.value() == 1:
        boton_pulsado(lista_150)
        led_jugador_1.off()
        time.sleep(1)
    if boton_200.value() == 1:
        boton_pulsado(lista_200)
        led_jugador_1.off()
        time.sleep(1)
    if boton_250.value() == 1:
        boton_pulsado(lista_250)
        led_jugador_1.off()
        time.sleep(1)
    if boton_500.value() == 1:
        boton_pulsado(lista_500)
        led_jugador_1.off()

        time.sleep(1)
    else:
        led_jugador_1.on()