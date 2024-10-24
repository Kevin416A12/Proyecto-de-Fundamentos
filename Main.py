import machine
import network
import socket
import time
import utime
# Pines de Salida
led = machine.Pin("LED", machine.Pin.OUT)
led_jugador_1 = machine.Pin(22, machine.Pin.OUT)
led_jugador_2 = machine.Pin(27, machine.Pin.OUT)
AB = machine.Pin(18, machine.Pin.OUT)
CLK = machine.Pin(19, machine.Pin.OUT)

#Pines de entrada
boton_cambio = machine.Pin(5, machine.Pin.IN, machine.Pin.PULL_DOWN)
boton_100 = machine.Pin(8, machine.Pin.IN, machine.Pin.PULL_DOWN) # A
boton_150 = machine.Pin(9, machine.Pin.IN, machine.Pin.PULL_DOWN) # G
boton_200 = machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN) # B
boton_250 = machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN) # C
boton_500 = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN) # D
potenciometro = machine.ADC(machine.Pin(26))
#Informacion del internet
SSDI = 'Tilin'
Password = '12345678KFJ'
#conectarse a la red
wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(SSDI, Password)# conectar la bichota
while not wlan.isconnected():    
     time.sleep(1)

print("Conectado a Wi-Fi", wlan.ifconfig())#configurar el socket para la conexion
host = '192.168.43.55'
port = 12345

# Listas con los codigos
lista_prueba = [0,0,0,0,0,0,0,1]
lista_100 = [0,0,0,0,0,0,0,1]
lista_150 = [0,1,1,1,0,0,0,0]
lista_200 = [0,0,0,0,0,0,1,0]
lista_250 = [0,0,0,0,0,1,0,0]
lista_500 = [0,0,0,0,1,0,0,0]
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
    leer_potenciometro()   
    limpiar()
    
def leer_potenciometro():
        valor_actual = potenciometro.read_u16() / 65535 *3.3
        print(valor_actual)   
        if valor_actual < 0.20:
         led_jugador_2.on ()        
         led_jugador_1.off()
        elif valor_actual  >2.20:       
             led_jugador_2.off()
             led_jugador_1.on()        
        
def limpiar():   
    for i in range(8):
        shift_bit(0)  # Desplaza un bit '0' al registro          # Espera medio segundo entre cada LED
    print("Limpio")        
    limpiar()     
while True:    
    if boton_cambio.value() == 1:        
        leer_potenciometro()
         # Crea un socke       
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:            
            s.connect((host, port))
            s.send(b'100')       
        except OSError as e:
            print("Error de conexión:", e)        
        finally:
            s.close()  # Cierra el socket manualmente        
            time.sleep(0.5)  # Anti-rebote 
            print("Si, funciona Tilin")
    if boton_100.value() == 1:        
        boton_pulsado(lista_100)
        led_jugador_1.off()        
        time.sleep(1)
        keyb.bind("w")    
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