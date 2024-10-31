from tkinter import *
import pygame
import random
import threading
from PIL import Image, ImageTk  # Importa PIL para manejar imágenes
import socket
# Resto del código de la interfaz
jugadores = []
jugador_actual = None
puntaje_jugador1 = 0
puntaje_jugador2 = 0
puntaje_jugador1_1= 0 
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

                if data in [b'100', b'150', b'200', b'250']:
                    puntos = int(data.decode())
                    reproducir_sonido_botones()
                    mostrar_mensaje(puntos)

                if data == b"500":
                    puntos = int(data.decode())
                    reproducir_sonido_500()
                    mostrar_mensaje(puntos)
# Variables para almacenar los textos de puntaje en cada canvas
puntaje1_canvas1 = None
puntaje1_canvas2 = None
puntaje2_canvas1 = None
puntaje2_canvas2 = None
puntaje_1jugador = None

def actualizar_puntaje(puntos):
    global puntaje_jugador1, puntaje_jugador2, fondo_canvasa, fondo_canvasa2, jugador_seleccionado, canvas_actual
    global puntaje1_canvas1, puntaje1_canvas2, puntaje2_canvas1, puntaje2_canvas2,puntaje_jugador1_1,puntaje_1jugador

    if jugador1 == jugador_seleccionado:
        print("jug1")
        puntaje_jugador1 += puntos

        # Actualizar puntaje para jugador 1 en fondo_canvasa
        if canvas_actual == fondo_canvasa:
            print("canvas1 para jugador 1")
            if puntaje1_canvas1:
                fondo_canvasa.delete(puntaje1_canvas1)
            puntaje1_canvas1 = fondo_canvasa.create_text(140, 500, text=f'Puntos: {puntaje_jugador1}', font=("Aptos Black", 30),
                                                         fill='#FEF9F2', anchor='center')

        # Actualizar puntaje para jugador 1 en fondo_canvasa2
        elif canvas_actual == fondo_canvasa2:
            print("canvas2 para jugador 1")
            if puntaje1_canvas2:
                fondo_canvasa2.delete(puntaje1_canvas2)
            puntaje1_canvas2 = fondo_canvasa2.create_text(140, 500, text=f'Puntos: {puntaje_jugador1}', font=("Aptos Black", 30),
                                                          fill='#FEF9F2', anchor='center')

    elif jugador2 == jugador_seleccionado:
        print("jug2")
        puntaje_jugador2 += puntos

        # Actualizar puntaje para jugador 2 en fondo_canvasa
        if canvas_actual == fondo_canvasa:
            print("canvas1 para jugador 2")
            if puntaje2_canvas1:
                fondo_canvasa.delete(puntaje2_canvas1)
            puntaje2_canvas1 = fondo_canvasa.create_text(140, 500, text=f'Puntos: {puntaje_jugador2}', font=("Arial", 24),
                                                         fill='#FEF9F2', anchor='center')

        # Actualizar puntaje para jugador 2 en fondo_canvasa2
        elif canvas_actual == fondo_canvasa2:
            print("canvas2 para jugador 2")
            if puntaje2_canvas2:
                fondo_canvasa2.delete(puntaje2_canvas2)
            puntaje2_canvas2 = fondo_canvasa2.create_text(140, 500, text=f'Puntos: {puntaje_jugador2}', font=("Arial", 24),
                                                          fill='#FEF9F2', anchor='center')
    elif jugador1_1:
        print('jugador solo')
        puntaje_jugador1_1 += puntos

        if canvas_actual == fondo_canvasa1:
            print("canvas1 para jugador 2")
            if puntaje_1jugador:
                fondo_canvasa1.delete(puntaje_1jugador)
            puntaje_1jugador = fondo_canvasa.create_text(140, 500, text=f'Puntos: {puntaje_jugador1_1}', font=("Arial", 24),
                                                         fill='#FEF9F2', anchor='center')
        
def guardar_puntaje1():
    global puntaje_1jugador,puntaje_jugador1_1,jugador1_1
    with open('puntajes.txt', 'a') as file:
        file.write(f'{jugador1_1}: {puntaje_jugador1_1}\n')
        
def guardar_puntaje():
    global puntaje_jugador1, puntaje_jugador2,jugador1,jugador2
    with open('puntajes.txt', 'a') as file:
        file.write(f'{jugador1}: {puntaje_jugador1}\n')
        file.write(f'{jugador2}: {puntaje_jugador2}\n')

def mostrar_mensaje(puntos):
    print(f"Botón presionado, se suman {puntos} puntos.")

    actualizar_puntaje(puntos)


def start_socket_thread():
    socket_thread = threading.Thread(target=iniciar_socket)
    socket_thread.daemon = True  # Permite que el hilo se cierre al cerrar la aplicación
    socket_thread.start()

# Inicializa pygame y su funcion de musica
pygame.init()
pygame.mixer.init()


# Función para reproducir música en bucle
def reproducir_musica():
    pygame.mixer.music.load('musica y sonidos/Williams  Star Trek the next generation  pinball soundtrack.mp3')
    pygame.mixer.music.play(-1)

def cargar_sonido_botones():
    return pygame.mixer.Sound('musica y sonidos/Sonido de Victoria de un Juego para tus vídeos - Efecto de Sonido.mp3')

sonido_botones = cargar_sonido_botones()

def reproducir_sonido_botones():
    sonido_botones.play()

def cargar_sonido_500():
    return pygame.mixer.Sound('musica y sonidos/musica 500.mp3')

sonido_500 = cargar_sonido_500()

def reproducir_sonido_500():
    sonido_500.play()

     
# Función para detener la música
def detener_musica():
    pygame.mixer.music.stop()
#funcion para mostrar pantallas dentro de la ventana prin
# Función para mostrar pantallas dentro de la ventana principal
def mostrar_pantalla(pantalla, frames, indices=None):
    if indices is None:
        indices = list(frames.keys())
    
    if not indices:
        pantalla.pack(fill='both', expand=True)
        return
    
    frame_actual = indices[0]
    frames[frame_actual].pack_forget()
    
    mostrar_pantalla(pantalla, frames, indices[1:])
#funcion para cerrar la apllicacion 
def cerrar_aplicacion():
    pygame.mixer.music.stop()  # Detiene la música si está sonando
    inicio.destroy()  # Cierra la ventana principal
#funcion para escoger jugadores
def ir_a_jugadores():
    global frame_jugadores
    frame_jugadores= Frame(inicio)
    fondo_canvasj = Canvas(frame_jugadores)
    fondo_canvasj.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')  # Asegúrate de que esta ruta sea correcta
    # Redimensionar la imagen una vez que la ventana esté visible
    inicio.update()  # Actualiza la ventana para obtener el tamaño correcto
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)
    #boton de regresar
    regresar=Button(frame_jugadores,text='BACK', command=ir_a_inicio, bg='#243642',
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Posición en la esquina inferior derecha)

    # Dibuja la imagen en el canvas
    fondo_canvasj.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasj.image = fondo_imagen  # Mantén una referencia a la imagen
    #que habra opciones de jugadores
    un_jugador=Button(frame_jugadores,text='1 PLAYER',command= un_jugador1,bg='#243642', width=20,
                          borderwidth=8, highlightbackground='#257180', highlightcolor='#257180',font=('Helvetica', 17),fg='white')
    un_jugador.place(x=600,y=300)
    dos_jugadores=Button(frame_jugadores,text='2 PLAYERS',command=dos_jugadores2,bg='#243642', width=20,
                          borderwidth=8, highlightbackground='#257180', highlightcolor='#257180',font=('Helvetica', 17),fg='white')
    dos_jugadores.place(x=600,y=500)
    #cerrar pantalla no deseadas
    if 'frame_1jugador' in globals():
        frame_1jugador.pack_forget()
    if 'frame_2jugadores' in globals():
        frame_2jugadores.pack_forget()

    
    mostrar_pantalla(frame_jugadores,frames)
    
# Definición global de imágenes
imagenes = {}

# Cargar imágenes de perfil
def cargar_imagenes():
    try:
        imagenes["perro"] = PhotoImage(file="imagenes/perro.png")
        imagenes["panda"] = PhotoImage(file="imagenes/panda.png")
        imagenes["dinosaurio"] = PhotoImage(file="imagenes/dinosaurio.png")
        imagenes["tigre"] = PhotoImage(file="imagenes/tigre.png")
        imagenes["gato"] = PhotoImage(file="imagenes/gato.png")
    except Exception as e:
        print(f"Error al cargar imágenes: {e}")

# Llama a la función de cargar imágenes después de crear la ventana


# Inicialización de variables
perfil_jugador1 = None
perfil_jugador2 = None
perfil_jugador1_1=None
def seleccionar_perfil_jugador1_1(imagen):
    global perfil_jugador1_1
    perfil_jugador1_1 = imagen
    boton_play.config(state='normal')
    
def seleccionar_perfil_jugador1(imagen):
    global perfil_jugador1
    perfil_jugador1 = imagen
    habilitar_personajes2()

def seleccionar_perfil_jugador2(imagen):
    global perfil_jugador2
    perfil_jugador2 = imagen
    next2.config(state='normal')



def un_jugador1():
    global frame_1jugador,imagen_perro,imagen_dinosaurio,imagen_panda,imagen_tigre,imagen_gato,jugador1_1,nombre_jugador,boton_play
    frame_1jugador= Frame(inicio)
    fondo_canvasj = Canvas(frame_1jugador)
    fondo_canvasj.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')  # Asegúrate de que esta ruta sea correcta
    # Redimensionar la imagen una vez que la ventana esté visible
    inicio.update()  # Actualiza la ventana para obtener el tamaño correcto
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)
    #boton de regresar
    regresar=Button(frame_1jugador,text='BACK', command=ir_a_jugadores, bg='#243642',
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Posición en la esquina inferior derecha)
    #imagenes para botones 
    imagen_perro = PhotoImage(file="imagenes/perro.png")
    imagen_panda = PhotoImage(file="imagenes/panda.png")
    imagen_dinosaurio = PhotoImage(file="imagenes/dinosaurio.png")
    imagen_tigre = PhotoImage(file="imagenes/tigre.png")
    imagen_gato= PhotoImage(file="imagenes/gato.png")
    # Botones para los perfiles 
    boton_perro = Button(frame_1jugador, image=imagen_perro,command=lambda: seleccionar_perfil_jugador1_1(imagen_perro))
    boton_panda = Button(frame_1jugador, image=imagen_panda,command=lambda: seleccionar_perfil_jugador1_1(imagen_panda))
    boton_dinosaurio = Button(frame_1jugador, image=imagen_dinosaurio,command=lambda: seleccionar_perfil_jugador1_1(imagen_dinosaurio))
    boton_tigre = Button(frame_1jugador, image=imagen_tigre,command=lambda: seleccionar_perfil_jugador1_1(imagen_tigre))
    boton_gato = Button(frame_1jugador, image=imagen_gato,command=lambda: seleccionar_perfil_jugador1_1(imagen_gato))
    # Mantener la referencia a la imagen
    boton_perro.image = imagen_perro
    boton_panda.image = imagen_panda
    boton_dinosaurio.image = imagen_dinosaurio
    boton_tigre.image = imagen_tigre
    boton_gato.image = imagen_gato
    #colocar los botones
    boton_perro.place(x=10,y=300)
    boton_panda.place(x=280,y=300)
    boton_dinosaurio.place(x=560,y=300)
    boton_tigre.place(x=840,y=300)
    boton_gato.place(x=1250,y=300)
    #boton para empezar el juego
    boton_play=Button(frame_1jugador,text='PLAY', bg='#243642',width=20,command=ventana_juego1,
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    boton_play.config(state='disabled')
    boton_play.place(x=600,y=700)
    # Dibuja la imagen en el canvas
    fondo_canvasj.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasj.image = fondo_imagen  # Mantén una referencia a la imagen
    #label de nickname
    fondo_canvasj.create_text(200, 150, text="NICKNAME:", font=("Arial", 24), fill="#FEF9F2")   
    nombre_jugador = Entry(frame_1jugador)
    nombre_jugador.place(x=300,y=140)
    
    #eliminar pantallas no deseadas
    if 'frame_jugadores' in globals():
        frame_jugadores.pack_forget()

    mostrar_pantalla(frame_1jugador,frames)




def dos_jugadores2():
    global frame_2jugadores, fondo_canvass, nombre_jugador1, nombre_jugador2,imagen_gato,imagen_dinosaurio,imagen_panda,imagen_perro,imagen_tigre
    global boton_dinosaurio2, boton_gato2,boton_panda2,boton_perro2,boton_tigre2,next2
    frame_2jugadores = Frame(inicio)
    fondo_canvass = Canvas(frame_2jugadores)
    fondo_canvass.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    inicio.update()  # Actualiza la ventana para obtener el tamaño correcto
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botón de regresar
    regresar = Button(frame_2jugadores, text='BACK', command=ir_a_jugadores, bg='#243642', 
                      borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)
    
    next2 = Button(frame_2jugadores, text='NEXT', command=animacion, bg='#243642', width=15,
                  borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    next2.config(state='disabled')
    next2.place(x=620, y=760)

    # Imágenes para botones 
    imagen_perro = PhotoImage(file="imagenes/perro.png")
    imagen_panda = PhotoImage(file="imagenes/panda.png")
    imagen_dinosaurio = PhotoImage(file="imagenes/dinosaurio.png")
    imagen_tigre = PhotoImage(file="imagenes/tigre.png")
    imagen_gato = PhotoImage(file="imagenes/gato.png")

    # Botones para los perfiles 
    boton_perro1 = Button(frame_2jugadores, image=imagen_perro,command=lambda: seleccionar_perfil_jugador1(imagen_perro))
    boton_panda1 = Button(frame_2jugadores, image=imagen_panda,command=lambda: seleccionar_perfil_jugador1(imagen_panda))
    boton_dinosaurio1 = Button(frame_2jugadores, image=imagen_dinosaurio,command=lambda: seleccionar_perfil_jugador1(imagen_dinosaurio))
    boton_tigre1 = Button(frame_2jugadores, image=imagen_tigre,command=lambda: seleccionar_perfil_jugador1(imagen_tigre))
    boton_gato1 = Button(frame_2jugadores, image=imagen_gato,command=lambda: seleccionar_perfil_jugador1(imagen_gato))

    # Mantener la referencia a la imagen
    boton_perro1.image = imagen_perro
    boton_panda1.image = imagen_panda
    boton_dinosaurio1.image = imagen_dinosaurio
    boton_tigre1.image = imagen_tigre
    boton_gato1.image = imagen_gato

    # Colocar los botones
    boton_perro1.place(x=10, y=100)
    boton_panda1.place(x=280, y=100)
    boton_dinosaurio1.place(x=560, y=100)
    boton_tigre1.place(x=840, y=100)
    boton_gato1.place(x=1250, y=100)

    # Botones para los perfiles segundo jugador 
    boton_perro2 = Button(frame_2jugadores, image=imagen_perro,command=lambda: seleccionar_perfil_jugador2(imagen_perro))
    boton_panda2 = Button(frame_2jugadores, image=imagen_panda,command=lambda: seleccionar_perfil_jugador2(imagen_panda))
    boton_dinosaurio2 = Button(frame_2jugadores, image=imagen_dinosaurio,command=lambda: seleccionar_perfil_jugador2(imagen_dinosaurio))
    boton_tigre2 = Button(frame_2jugadores, image=imagen_tigre,command=lambda: seleccionar_perfil_jugador2(imagen_tigre))
    boton_gato2 = Button(frame_2jugadores, image=imagen_gato,command=lambda: seleccionar_perfil_jugador2(imagen_gato))
    #deshabilitar botones de segundos personajes
    boton_perro2.config(state='disabled')
    boton_panda2.config(state='disabled')
    boton_dinosaurio2.config(state='disabled')
    boton_tigre2.config(state='disabled')
    boton_gato2.config(state='disabled')
    
    # Mantener la referencia a la imagen
    boton_perro2.image = imagen_perro
    boton_panda2.image = imagen_panda
    boton_dinosaurio2.image = imagen_dinosaurio
    boton_tigre2.image = imagen_tigre
    boton_gato2.image = imagen_gato

    # Colocar los botones
    boton_perro2.place(x=10, y=500)
    boton_panda2.place(x=280, y=500)
    boton_dinosaurio2.place(x=560, y=500)
    boton_tigre2.place(x=840, y=500)
    boton_gato2.place(x=1250, y=500)

    # Dibuja la imagen en el canvas
    fondo_canvass.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvass.image = fondo_imagen  # Mantén una referencia a la imagen

    # Label de nickname
    fondo_canvass.create_text(100, 50, text="PLAYER1:", font=("Arial", 24), fill="#FEF9F2")
    fondo_canvass.create_text(100, 450, text="PLAYER2:", font=("Arial", 24), fill="#FEF9F2")
    
    nombre_jugador1 = Entry(frame_2jugadores)
    nombre_jugador1.place(x=200, y=40)
    nombre_jugador2 = Entry(frame_2jugadores)
    nombre_jugador2.config(state='disabled')
    nombre_jugador2.place(x=200, y=440)


    # Eliminar pantallas no deseadas
    if 'frame_jugadores' in globals():
        frame_jugadores.pack_forget()
    if 'frame_animacion' in globals():
        frame_animacion.pack_forget()
    
    mostrar_pantalla(frame_2jugadores, frames)
def actualizar_jugadores():
    global jugadores,jugador1,jugador2
    jugador1 = nombre_jugador1.get()  # Obtener el texto del primer Entry
    jugador2 = nombre_jugador2.get()  # Obtener el texto del segundo Entry
    jugadores = [jugador1, jugador2]   # Actualizar la lista de jugadores

caras = []
animacion_activa= True
def cargar_gif(gif_path):
    global caras
    caras.clear()
    gif = Image.open(gif_path)
    for i in range(gif.n_frames):
        gif.seek(i)
        cara = gif.copy().rotate(90)  # Rotar 90 grados
        cara = cara.resize((700, 700))  
        cara = ImageTk.PhotoImage(cara)
        caras.append(cara)
    print(f"Cargados {len(caras)} frames.")  # Verifica cuántos frames se cargaron

def update_gif(frame_num):
    global animacion_activa
    if animacion_activa and caras:  # Verifica que la animación esté activa y que la lista no esté vacía
        gif_label.config(image=caras[frame_num])
        frame_num += 1
        if frame_num >= len(caras):
            frame_num = 0
        inicio.after(90, update_gif, frame_num)  # Llama de nuevo a update_gif
def obtener_imagen_perfil(jugador):
    if jugador == jugadores[0]:
        return perfil_jugador1
    elif jugador == jugadores[1]:
        return perfil_jugador2
    return None


perfil_jugador1 = None  # Carga la imagen de perfil correspondiente
perfil_jugador2 = None  # Carga la imagen de perfil correspondiente

# Variable global para almacenar el jugador seleccionado
global jugador_seleccionado
jugador_seleccionado = None



def finalizar_animacion():
    global animacion_activa, imagen_perfil_jugador1, imagen_perfil_jugador2, jugador_seleccionado,jugadores,imagen_perfil_jugador2
    animacion_activa = False  # Detener la animación
    gif_label.place_forget()   # Ocultar el gif_label
    actualizar_jugadores()
    # Escoger un jugador aleatorio
    jugador_seleccionado = random.choice(jugadores)

    # Asignar las imágenes de perfil de los jugadores
    imagen_perfil_jugador1 = obtener_imagen_perfil(jugadores[0])
    imagen_perfil_jugador2 = obtener_imagen_perfil(jugadores[1])
    
    # Llamar a mostrar_resultado
    inicio.after(0, mostrar_resultado, jugador_seleccionado)

def mostrar_resultado(jugador_seleccionado):
    global imagen_perfil_jugador1, imagen_perfil_jugador2

    # Obtener las dimensiones del canvas
    canvas_width = fondo_canvass.winfo_width()
    canvas_height = fondo_canvass.winfo_height()

    # Calcular las coordenadas para centrar el texto y la imagen
    x_texto = canvas_width / 2
    y_texto_texto = canvas_height / 2 - 110  # Para el texto
    y_texto_imagen = canvas_height / 2 + 50  # Para la imagen (más espacio)

    # Mostrar el texto
    fondo_canvass.create_text(
        x_texto,
        y_texto_texto,
        text=f"¡START: {jugador_seleccionado}! ",
        font=("Arial", 24),
        fill="#FEF9F2",
        anchor='center'
    )
    
    # Obtener y mostrar la imagen del perfil
    imagen_perfil = obtener_imagen_perfil(jugador_seleccionado)
    if imagen_perfil:
        fondo_canvass.create_image(
            x_texto,
            y_texto_imagen,
            image=imagen_perfil,
            anchor='center'
        )
    else:
        print(f"No se encontró imagen para {jugador_seleccionado}")  # Para depuración
global texto_temporizador
texto_temporizador = None  # Inicializar texto_temporizador como None
texto_temporizador1 = None
canvas_actual = None  # Variable para el canvas activo
def ventana_juego1():
    global frame_juego1, fondo_canvasa1, boton_start1, canvas_actual, boton_scores, jugador1_1
    frame_juego1 = Frame(inicio)
    fondo_canvasa1 = Canvas(frame_juego1)
    fondo_canvasa1.pack(fill=BOTH, expand=True)
    

    canvas_actual = fondo_canvasa1  # Establecer el canvas activo
    jugador1_1 = nombre_jugador.get()
    
    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botón de regresar
    regresar = Button(frame_juego1, text='BACK', command=ir_a_inicio, 
                      bg='#243642', borderwidth=8, highlightbackground='#257180', 
                      highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvasa1.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasa1.image = fondo_imagen

    # Botón de inicio
    boton_start1 = Button(frame_juego1, text='START', command=lambda: iniciar_temporizador1(15), width=20,
                          bg='#B6FFA1', borderwidth=8, highlightbackground='#257180', 
                          highlightcolor='#257180', font=('Aptos Black', 20), fg='black')
    boton_start1.place(x=650, y=500, anchor='center')

    # Label para los puntos
    

    

    boton_scores = Button(frame_juego1, text='SCORES', command=lambda:(guardar_puntaje1(),ir_a_marcadores()), width=20,
                          bg='#B6FFA1', borderwidth=8, highlightbackground='#257180', 
                          highlightcolor='#257180', font=('Aptos Black', 20), fg='black')
    
    fondo_canvasa1.create_text(140, 100, text=f'Jugando: {jugador1_1}!', font=("Arial", 24), fill='#FEF9F2', anchor='center')
    fondo_canvasa1.create_image(50, 150, image=perfil_jugador1_1, anchor='nw')

    frames['ventana juego1'] = frame_juego1
    if 'frame_1jugador' in globals():
        frame_1jugador.pack_forget()
    mostrar_pantalla(frame_juego1, frames)
    print('Ventana de juego 1 cargada')



def ventana_juego():
    global frame_juego, fondo_canvasa, boton_start, boton_siguiente, canvas_actual,fondo_canvasa, jugador_seleccionado
    frame_juego = Frame(inicio)
    fondo_canvasa = Canvas(frame_juego)
    fondo_canvasa.pack(fill=BOTH, expand=True)


    canvas_actual = fondo_canvasa  # Establecer el canvas activo

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botón de regresar
    regresar = Button(frame_juego, text='BACK', command=ir_a_inicio, 
                      bg='#243642', borderwidth=8, highlightbackground='#257180', 
                      highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvasa.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasa.image = fondo_imagen

    # Botón de inicio
    boton_start = Button(frame_juego, text='START', command=lambda: iniciar_temporizador(2), width=20,
                         bg='#B6FFA1', borderwidth=8, highlightbackground='#257180', 
                         highlightcolor='#257180', font=('Aptos Black', 20), fg='black')
    boton_start.place(x=630, y=500, anchor='center')
    

    # Botón siguiente
    boton_siguiente = Button(frame_juego, text='NEXT', command=ventana_juego2, width=20,
                             bg='#B6FFA1', borderwidth=8, highlightbackground='#257180', 
                             highlightcolor='#257180', font=('Aptos Black', 20), fg='black')
    boton_siguiente.place(x=-630, y=700)  # Colocar el botón en la posición deseada

    # Mostrar información del jugador que está jugando
    if jugador_seleccionado:
        fondo_canvasa.create_text(140, 100, text=f'Jugando: {jugador_seleccionado}!', font=("Arial", 24), fill='#FEF9F2', anchor='center')
        imagen_perfil_jugador = obtener_imagen_perfil(jugador_seleccionado)
        if imagen_perfil_jugador:
            fondo_canvasa.create_image(50, 150, image=imagen_perfil_jugador, anchor='nw')

    frames['ventana juego'] = frame_juego 
    if 'frame_animacion' in globals():
        frame_animacion.pack_forget()
    mostrar_pantalla(frame_juego, frames)
    print('Ventana de juego cargada correctamente')
no_selecionado= None
def ventana_juego2():
    global frame_juego2, fondo_canvasa2, boton_start2, canvas_actual,boton_scores,fondo_canvasa2, jugador_seleccionado
    global jugadores
    frame_juego2 = Frame(inicio)
    fondo_canvasa2 = Canvas(frame_juego2)
    fondo_canvasa2.pack(fill=BOTH, expand=True)
    if jugador_seleccionado == jugador1:
        jugador_seleccionado = jugador2
    elif jugador_seleccionado == jugador2:
        jugador_seleccionado = jugador1

    canvas_actual = fondo_canvasa2  # Establecer el canvas activo

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botón de regresar
    regresar = Button(frame_juego2, text='BACK', command=ir_a_inicio, 
                      bg='#243642', borderwidth=8, highlightbackground='#257180', 
                      highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvasa2.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasa2.image = fondo_imagen
   
    # Botón de inicio
    boton_start2 = Button(frame_juego2, text='START', command=lambda: iniciar_temporizador(2), width=20,
                          bg='#B6FFA1', borderwidth=8, highlightbackground='#257180', 
                          highlightcolor='#257180', font=('Aptos Black', 20), fg='black')
    boton_start2.place(x=650, y=500, anchor='center')

    # Mostrar información del jugador que está jugando
    
    boton_scores= Button(frame_juego2, text='SCORES', command=lambda:(guardar_puntaje(),ir_a_marcadores()), width=20,
                          bg='#B6FFA1', borderwidth=8, highlightbackground='#257180', 
                          highlightcolor='#257180', font=('Aptos Black', 20), fg='black')

    
    if jugador_seleccionado:
        fondo_canvasa2.create_text(140, 100, text=f'Jugando: {jugador_seleccionado}!', font=("Arial", 24), fill='#FEF9F2', anchor='center')
        imagen_perfil_jugador = obtener_imagen_perfil(jugador_seleccionado)
        if imagen_perfil_jugador:
            fondo_canvasa2.create_image(50, 150, image=imagen_perfil_jugador, anchor='nw')

    frames['ventana juego2'] = frame_juego2
    if 'ventana juego' in globals():
        frame_juego.pack_forget()
    mostrar_pantalla(frame_juego2, frames)
    print('Ventana de juego 2 cargada correctamente')

def iniciar_temporizador(segundos):
    global tiempo_restante, texto_temporizador
    tiempo_restante = segundos
    actualizar_temporizador()
    # Ocultar el botón de inicio en la ventana correspondiente
    if 'boton_start2' in globals():
        boton_start2.place_forget()  
    
    else:
        boton_start.place(x=5000, y=5000)
        

def actualizar_temporizador():
    global tiempo_restante, texto_temporizador
    if tiempo_restante > 0:
        minutos, segundos = divmod(tiempo_restante, 60)
        tiempo_formateado = f"¡{minutos:02}:{segundos:02}!"

        # Borrar el texto anterior si existe en el canvas activo
        if texto_temporizador:
            canvas_actual.delete(texto_temporizador)

        # Crear el nuevo texto del temporizador en el canvas activo
        texto_temporizador = canvas_actual.create_text(700, 90, text=tiempo_formateado, font=("Aptos Black", 80), fill='#00FF9C', anchor='center')
        
        tiempo_restante -= 1
        inicio.after(1000, actualizar_temporizador)  # Actualizar cada segundo
    else:
        boton_siguiente.place(x=630, y=700)  # Asegúrate de que el botón sea visible
        canvas_actual.delete(texto_temporizador)
        canvas_actual.create_text(680, 300, text="¡Tiempo agotado! ", font=("Aptos Black", 50), fill='red', anchor='center')
        if 'boton_scores'in globals():
            boton_scores.place(x=650,y=750)
def iniciar_temporizador1(segundos):
    global tiempo_restante1, texto_temporizador1
    tiempo_restante1 = segundos
    actualizar_temporizador1()
    # Ocultar el botón de inicio en la ventana correspondiente
    if 'boton_start1' in globals():
        boton_start1.place_forget()  #
    
    
        

def actualizar_temporizador1():
    global tiempo_restante1, texto_temporizador1
    if tiempo_restante1 > 0:
        minutos, segundos = divmod(tiempo_restante1, 60)
        tiempo_formateado1 = f"¡{minutos:02}:{segundos:02}!"

        # Borrar el texto anterior si existe en el canvas activo
        if texto_temporizador1:
            fondo_canvasa1.delete(texto_temporizador1)

        # Crear el nuevo texto del temporizador en el canvas activo
        texto_temporizador1 = fondo_canvasa1.create_text(700, 90, text=tiempo_formateado1, font=("Aptos Black", 80), fill='#00FF9C', anchor='center')
        
        tiempo_restante1 -= 1
        inicio.after(1000, actualizar_temporizador1)  # Actualizar cada segundo
    else:
        fondo_canvasa1.delete(texto_temporizador1)
        fondo_canvasa1.create_text(680, 300, text="¡Tiempo agotado! ", font=("Aptos Black", 50), fill='red', anchor='center')
        if 'boton_scores'in globals():
            boton_scores.place(x=650,y=750)



def animacion():
    global frame_animacion, gif_label, fondo_canvass
    frame_animacion = Frame(inicio)
    fondo_canvass = Canvas(frame_animacion)
    fondo_canvass.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botón de regresar
    regresar = Button(frame_animacion, text='BACK', command=dos_jugadores2, 
                      bg='#243642', borderwidth=8, highlightbackground='#257180', 
                      highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvass.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvass.image = fondo_imagen

    # Cargar y mostrar el GIF
    cargar_gif('imagenes/monedagirando.gif') 
    gif_label = Label(frame_animacion, borderwidth=-2, width=500, height=500)
    gif_label.place(x=500, y=200)

    # Iniciar la animación del GIF
    update_gif(0)  # Llamada inicial a update_gif
    # Detener la animación después de 3 segundos y escoger un jugador
    inicio.after(3000, finalizar_animacion)
    inicio.after(5000, ventana_juego)

    frames['animacion'] = frame_animacion  
    if 'frame_2jugadores' in globals():
        frame_2jugadores.pack_forget()
    mostrar_pantalla(frame_animacion, frames)
# una funcion que me habilite los botones antes de ir a la pantalla de juego 
def habilitar_personajes2 ():
    global boton_dinosaurio2, boton_gato2,boton_panda2,boton_perro2,boton_tigre2,nombre_jugador2
    nombre_jugador2.config(state='normal')
    # Colocar los botones
    boton_perro2.config(state='normal')
    boton_panda2.config(state='normal')
    boton_dinosaurio2.config(state='normal')
    boton_tigre2.config(state='normal')
    boton_gato2.config(state='normal')

def ir_a_marcadores():
    global frame_scores

    frame_scores = Frame(inicio)
    fondo_canvass = Canvas(frame_scores)
    fondo_canvass.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    inicio.update()
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botón de regresar
    regresar = Button(frame_scores, text='BACK', command=ir_a_inicio, bg='#243642', 
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvass.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvass.image = fondo_imagen
    fondo_canvass.create_text(500, 200, text="BEST SCORES", font=('Aptos Black', 40), fill='green', anchor='w')

    # Leer puntajes del archivo y mostrar en el Canvas
    try:
        with open('puntajes.txt', 'r') as file:
            puntajes = []
            for linea in file:
                datos = linea.strip().split(maxsplit=1)
                if len(datos) == 2:
                    nombre, score = datos
                    try:
                        score = int(score)
                        puntajes.append((nombre, score))
                    except ValueError:
                        print(f"Formato de puntaje incorrecto en la línea: {linea.strip()}")

            # Ordena los puntajes en orden descendente y toma los 3 más altos
            mejores_puntajes = sorted(puntajes, key=lambda x: x[1], reverse=True)[:3]

            y_position = 400
            for nombre, score in mejores_puntajes:
                texto = f"{nombre}: {score} puntos"
                fondo_canvass.create_text(500, y_position, text=texto, font=('Helvetica', 40), fill='white', anchor='w')
                y_position += 80
    except FileNotFoundError:
        fondo_canvass.create_text(200, 100, text="No se encontraron puntajes.", font=('Helvetica', 16), fill='white',
                                  anchor='w')


    frames['marcadores'] = frame_scores  # Añade el nuevo frame al diccionario
    mostrar_pantalla(frame_scores, frames)

#funcion que muestra la informacion de creadores y del juego
def ir_a_info():
    global frame_info
    frame_info = Frame(inicio)
    fondo_canvas = Canvas(frame_info)
    fondo_canvas.pack(fill=BOTH, expand=True)

    # Cargar imágenes
    imagen_autor = Image.open("imagenes/foto_jacob.png")
    imagen_autor_2 = Image.open("imagenes/foto_kevin.png")
    imagen_fondo = Image.open('imagenes/fondo.png')
    inicio.update()

    # Redimensionar imagen de fondo según el tamaño de la ventana
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))

    # Convertir las imágenes para ser usadas en Tkinter
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)
    autor_imagen = ImageTk.PhotoImage(imagen_autor)
    autor_imagen_2 = ImageTk.PhotoImage(imagen_autor_2)

    # Botón de regresar
    regresar = Button(frame_info, text='BACK', bg='#605678', command=ir_a_inicio, font=('Helvetica', 17))
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen de fondo en el canvas
    fondo_canvas.create_image(0, 0, anchor='nw', image=fondo_imagen)

    # Dibuja la imagen del autor en el canvas
    x_autor = 50
    y_autor = 25
    fondo_canvas.create_image(x_autor+600, y_autor, anchor='nw', image=autor_imagen)
    fondo_canvas.create_image(x_autor , y_autor + 40, anchor='nw', image=autor_imagen_2)
    # Añadir la información del autor y del programa


    label_autor = Label(frame_info, text="Nombre: Jacob Zumbado Cubero\nID: 2024088988", bg="#e0e0e0", font=("Helvetica", 12))
    label_autor.place(x=x_autor + 700, y=y_autor + 500)  # Posiciona la etiqueta junto a la imagen del autor



    label_autor = Label(frame_info, text="Nombre: Kevin Castro Perez\nID: 2024182200", bg="#e0e0e0", font=("Helvetica", 12))
    label_autor.place(x=x_autor + 150, y=y_autor + 500)

    # Información del programa
    label_info = Label(frame_info, text="Asignatura: Fundamentos de sistemas computacionales\nCarrera: Ingenieria en Computadores\n"
                                        "Año: 2024\nProfesor: Ing. Luis Alberto Chavarria Zamora\nPaís: Costa Rica\nVersión: 1.0.0",
                       bg="#e0e0e0", font=("Helvetica", 12))
    label_info.place(x=x_autor + 400, y=y_autor + 600)


    # Guardar referencias a las imágenes para evitar que el recolector de basura las elimine
    fondo_canvas.fondo_imagen = fondo_imagen
    fondo_canvas.autor_imagen = autor_imagen
    fondo_canvas.autor_imagen_2 = autor_imagen_2

    frames['info'] = frame_info  # Añade el nuevo frame al diccionario
    mostrar_pantalla(frame_info, frames)
# Función para regresar a inicio
def ir_a_inicio():
    if 'frame_jugadores' in globals():
        frame_jugadores.pack_forget()
    if 'frame_scores' in globals():
        frame_scores.pack_forget()
    if 'frame_info' in globals():
        frame_info.pack_forget()
    if ' frame_juego' in globals():
        frame_juego.pack_forget()
    mostrar_pantalla(frame_inicio, frames)



inicio = None

def ventana_prin():
    global inicio, frame_inicio, frames
    reproducir_musica()
    inicio = Tk()
    inicio.title('PINBALL')
    inicio.attributes('-fullscreen', True)
    inicio.configure(bg='black')



    # Define las características de la pantalla de inicio
    frame_inicio = Frame(inicio, bg='black')
    fondo_canvas = Canvas(frame_inicio)
    fondo_canvas.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    inicio.update()  # Actualiza la ventana para obtener el tamaño correcto
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botones
    exit = Button(frame_inicio, text='EXIT', command=cerrar_aplicacion, bg='#243642',
                  borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    exit.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    jugadores = Button(frame_inicio, text='PLAYERS', command=ir_a_jugadores, bg='#243642', width=20,
                       borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    jugadores.place(x=200, y=600)

    scores = Button(frame_inicio, text='SCORES', command=ir_a_marcadores, bg='#243642', width=20,
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    scores.place(x=600, y=600)

    info = Button(frame_inicio, text='ABOUT', command=ir_a_info, bg='#243642', width=20,
                  borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    info.place(x=1000, y=600)

    fondo_canvas.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvas.image = fondo_imagen  # Mantén una referencia a la imagen

    logo = Image.open('imagenes/logosi.png')
    logo_imagen = ImageTk.PhotoImage(logo)
    fondo_canvas.create_image(400, 100, anchor='nw', image=logo_imagen)

    frames = {'inicio': frame_inicio}
    mostrar_pantalla(frame_inicio, frames)

    cargar_imagenes()
    start_socket_thread()
    inicio.mainloop()
ventana_prin()
