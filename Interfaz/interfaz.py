from tkinter import *
import pygame
from PIL import Image, ImageTk  # Importa PIL para manejar imágenes
# Inicializa pygame y su funcion de musica
pygame.init()
pygame.mixer.init()

# Función para reproducir música en bucle
def reproducir_musica():
    pygame.mixer.music.load('musica y sonidos/Williams  Star Trek the next generation  pinball soundtrack.mp3')
    pygame.mixer.music.play(-1)

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
    regresar=Button(frame_jugadores,text='BACK',bg='#605678',command= ir_a_inicio,font=('Helvetica', 17))
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Posición en la esquina inferior derecha)

    # Dibuja la imagen en el canvas
    fondo_canvasj.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasj.image = fondo_imagen  # Mantén una referencia a la imagen
    #que habra opciones de jugadores
    un_jugador=Button(frame_jugadores,text='1 PLAYER',command= un_jugador1,bg='#243642', width=20,
                          borderwidth=8, highlightbackground='#257180', highlightcolor='#257180',font=('Helvetica', 17),fg='white')
    un_jugador.place(x=600,y=300)
    dos_jugadores=Button(frame_jugadores,text='2 PLAYERS',command= dos_jugadores2,bg='#243642', width=20,
                          borderwidth=8, highlightbackground='#257180', highlightcolor='#257180',font=('Helvetica', 17),fg='white')
    dos_jugadores.place(x=600,y=500)
    #cerrar pantalla no deseadas
    if 'frame_1jugador' in globals():
        frame_1jugador.pack_forget()
    if 'frame_2jugadores' in globals():
        frame_2jugadores.pack_forget()

    
    mostrar_pantalla(frame_jugadores,frames)
def un_jugador1():
    global frame_1jugador
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
    regresar=Button(frame_1jugador,text='BACK',bg='#605678',command= ir_a_jugadores,font=('Helvetica', 17))
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Posición en la esquina inferior derecha)

    # Dibuja la imagen en el canvas
    fondo_canvasj.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasj.image = fondo_imagen  # Mantén una referencia a la imagen
    #eliminar pantallas no deseadas
    if 'frame_jugadores' in globals():
        frame_jugadores.pack_forget()

    mostrar_pantalla(frame_1jugador,frames)
def dos_jugadores2():
    global frame_2jugadores
    frame_2jugadores= Frame(inicio)
    fondo_canvasj = Canvas(frame_2jugadores)
    fondo_canvasj.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')  # Asegúrate de que esta ruta sea correcta
    # Redimensionar la imagen una vez que la ventana esté visible
    inicio.update()  # Actualiza la ventana para obtener el tamaño correcto
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)
    #boton de regresar
    regresar=Button(frame_2jugadores,text='BACK',bg='#605678',command= ir_a_jugadores,font=('Helvetica', 17))
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Posición en la esquina inferior derecha)

    # Dibuja la imagen en el canvas
    fondo_canvasj.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvasj.image = fondo_imagen  # Mantén una referencia a la imagen
    #eliminar pantallas no deseadas
    if 'frame_jugadores' in globals():
        frame_jugadores.pack_forget()
    mostrar_pantalla(frame_2jugadores,frames)
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
    regresar = Button(frame_scores, text='BACK', bg='#605678', command=ir_a_inicio, font=('Helvetica', 17))
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvass.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvass.image = fondo_imagen

    frames['marcadores'] = frame_scores  # Añade el nuevo frame al diccionario
    mostrar_pantalla(frame_scores, frames)
#funcion que muestra la informacion de creadores y del juego
def ir_a_info():
    global frame_info
    frame_info = Frame(inicio)
    fondo_canvass = Canvas(frame_info)
    fondo_canvass.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')
    inicio.update()
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)

    # Botón de regresar
    regresar = Button(frame_info, text='BACK', bg='#605678', command=ir_a_inicio, font=('Helvetica', 17))
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvass.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvass.image = fondo_imagen

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
    mostrar_pantalla(frame_inicio, frames)



def ventana_prin():
    global inicio,frame_inicio,frames
    reproducir_musica()
    inicio = Tk()
    inicio.title('PINBALL')
    inicio.attributes('-fullscreen',True)
    inicio.configure(bg='black') 
 #################################################333
  # Define las características de la pantalla de inicio
    frame_inicio = Frame(inicio, bg='black')
    fondo_canvas = Canvas(frame_inicio)
    fondo_canvas.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')  # Asegúrate de que esta ruta sea correcta
    # Redimensionar la imagen una vez que la ventana esté visible
    inicio.update()  # Actualiza la ventana para obtener el tamaño correcto
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)
    ###############################3
    exit=Button(frame_inicio,text='EXIT',bg='#605678',command= cerrar_aplicacion,font=('Helvetica', 17))
    exit.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Posición en la esquina inferior derecha)

    jugadores= Button(frame_inicio,text='PLAYERS',command= ir_a_jugadores,bg='#243642', width=20,
                          borderwidth=8, highlightbackground='#257180', highlightcolor='#257180',font=('Helvetica', 17),fg='white')
    jugadores.place(x=200,y=600)
    scores = Button(frame_inicio, text='SCORES', command=ir_a_marcadores, bg='#243642', width=20,
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    scores.place(x=600, y=600)
    info=Button(frame_inicio,text='INFO', command=ir_a_info, bg='#243642', width=20,
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    info.place(x=1000, y=600)
    # Dibuja la imagen en el canvas
    fondo_canvas.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvas.image = fondo_imagen  # Mantén una referencia a la imagen
    logo = Image.open('imagenes/logosi.png')  # Asegúrate de que esta ruta sea correcta
    logo_imagen = ImageTk.PhotoImage(logo)

    # Dibuja el logo en el canvas
    fondo_canvas.create_image(400, 100, anchor='nw', image=logo_imagen)

    frames={'inicio':frame_inicio}
     #llama a la pantalla deseada inicial
    mostrar_pantalla(frame_inicio, frames)
    inicio.mainloop()
ventana_prin()