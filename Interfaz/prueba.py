# Iniciar el socket en un hilo separado
""""
import threading
socket_thread = threading.Thread(target=iniciar_socket, daemon=True)
socket_thread.start()
def iniciar_socket():
    host = '0.0.0.0'
    port = 12345

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()

        print("Esperando conexión...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Conectado a {addr}")
                data = conn.recv(1024)

                if data == b'cambio':
                    guardar_puntaje()
                    global jugadores
                    jugador_actual = jugadores[1] if jugador_actual == jugadores[0] else jugadores[0]
                    print(f"Cambiando a jugador {jugador_actual}")

                if data in [b'100', b'150', b'200', b'250', b'500']:
                    puntos = int(data.decode())
                    mostrar_mensaje(puntos)
def actualizar_puntaje(puntos):
    global puntaje_jugador1, puntaje_jugador2, fondo_canvasa, fondo_canvasa2
    if jugador_actual == 1:
        puntaje_jugador1 += puntos
        if fondo_canvasa:
            fondo_canvasa.create_text(140, 150, text=f'Puntos: {puntaje_jugador1}', font=("Arial", 24), fill='#FEF9F2', anchor='center')
    else:
        puntaje_jugador2 += puntos
        if fondo_canvasa2:
            fondo_canvasa2.create_text(140, 150, text=f'Puntos: {puntaje_jugador2}', font=("Arial", 24), fill='#FEF9F2', anchor='center')

def guardar_puntaje():
    global puntaje_jugador1, puntaje_jugador2
    with open('puntajes.txt', 'a') as file:
        file.write(f'Jugador 1: {puntaje_jugador1}\n')
        file.write(f'Jugador 2: {puntaje_jugador2}\n')

def mostrar_mensaje(puntos):
    print(f"Botón presionado, se suman {puntos} puntos.")
    actualizar_puntaje(puntos)

###################################################################################33
    def sumar_puntos(jugador, cantidad):
    global puntos_jugador1, puntos_jugador2
    if jugador == 1:
        puntos_jugador1 += cantidad
    elif jugador == 2:
        puntos_jugador2 += cantidad
    actualizar_puntos_display()

label_puntos1 = Label(frame_juego1, text=f'Puntos: {puntos_jugador1}', font=("Arial", 24), fg='white', bg='#243642')
label_puntos1.place(x=50, y=200)

def actualizar_puntos_display():
    label_puntos1.config(text=f'Puntos: {puntos_jugador1}')

label_puntos2 = Label(frame_juego, text=f'Puntos: {puntos_jugador2}', font=("Arial", 24), fg='white', bg='#243642')
label_puntos2.place(x=50, y=200)

def actualizar_puntos_display():
    label_puntos2.config(text=f'Puntos: {puntos_jugador2}')
def guardar_puntos():
    with open("puntajes.txt", "a") as file:
        file.write(f'Jugador 1: {puntos_jugador1}, Jugador 2: {puntos_jugador2}\n')
"""

import tkinter as tk

root = tk.Tk()

button = tk.Button(root, text="Botón",
                   highlightcolor="red",      # Cambia el color del borde de enfoque
                   highlightthickness=10)       # Cambia el grosor del borde de enfoque
button.pack(pady=20, padx=20)
import tkinter as tk

def on_focus(event):
    event.widget.config(borderwidth=3, relief="solid", highlightbackground="blue")

def on_focus_lost(event):
    event.widget.config(borderwidth=1, relief="raised", highlightbackground="grey")

root = tk.Tk()

button = tk.Button(root, text="Botón")
button.bind("<FocusIn>", on_focus)
button.bind("<FocusOut>", on_focus_lost)

button.pack(pady=20, padx=20)

root.mainloop()

root.mainloop()
