from tkinter import *
import pygame
import random
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
    global frame_1jugador,imagen_perro,imagen_dinosaurio,imagen_panda,imagen_tigre,imagen_gato
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
    imagen_panda = PhotoImage(file="imagenes/panda .png")
    imagen_dinosaurio = PhotoImage(file="imagenes/dinosaurio.png")
    imagen_tigre = PhotoImage(file="imagenes/tigre.png")
    imagen_gato= PhotoImage(file="imagenes/gato.png")
    #botones para los perfiles 
    boton_perro= Button(frame_1jugador,image=imagen_perro)
    boton_panda= Button(frame_1jugador,image=imagen_panda)
    boton_dinosaurio= Button(frame_1jugador,image=imagen_dinosaurio)
    boton_tigre= Button(frame_1jugador,image=imagen_tigre)
    boton_gato= Button(frame_1jugador,image=imagen_gato)
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
    boton_play=Button(frame_1jugador,text='PLAY', bg='#243642',width=20,
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
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
    global frame_2jugadores,fondo_canvass
    frame_2jugadores= Frame(inicio)
    fondo_canvass = Canvas(frame_2jugadores)
    fondo_canvass.pack(fill=BOTH, expand=True)

    # Cargar la imagen de fondo
    imagen_fondo = Image.open('imagenes/fondo.png')  # Asegúrate de que esta ruta sea correcta
    # Redimensionar la imagen una vez que la ventana esté visible
    inicio.update()  # Actualiza la ventana para obtener el tamaño correcto
    imagen_fondo = imagen_fondo.resize((inicio.winfo_width(), inicio.winfo_height()))
    fondo_imagen = ImageTk.PhotoImage(imagen_fondo)
    #boton de regresar
    regresar=Button(frame_2jugadores,text='BACK', command=ir_a_jugadores, bg='#243642', 
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)  # Posición en la esquina inferior derecha)
    next= Button(frame_2jugadores, text='NEXT', command=animacion, bg='#243642', width=15,
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    next.place(x=620,y=760)
    #imagenes para botones 
    imagen_perro = PhotoImage(file="imagenes/perro.png")
    imagen_panda = PhotoImage(file="imagenes/panda .png")
    imagen_dinosaurio = PhotoImage(file="imagenes/dinosaurio.png")
    imagen_tigre = PhotoImage(file="imagenes/tigre.png")
    imagen_gato= PhotoImage(file="imagenes/gato.png")
    #botones para los perfiles 
    boton_perro1= Button(frame_2jugadores,image=imagen_perro)
    boton_panda1= Button(frame_2jugadores,image=imagen_panda)
    boton_dinosaurio1= Button(frame_2jugadores,image=imagen_dinosaurio)
    boton_tigre1= Button(frame_2jugadores,image=imagen_tigre)
    boton_gato1= Button(frame_2jugadores,image=imagen_gato)
    # Mantener la referencia a la imagen
    boton_perro1.image = imagen_perro
    boton_panda1.image = imagen_panda
    boton_dinosaurio1.image = imagen_dinosaurio
    boton_tigre1.image = imagen_tigre
    boton_gato1.image = imagen_gato
    #colocar los botones
    boton_perro1.place(x=10,y=100)
    boton_panda1.place(x=280,y=100)
    boton_dinosaurio1.place(x=560,y=100)
    boton_tigre1.place(x=840,y=100)
    boton_gato1.place(x=1250,y=100)
    #botones para los perfiles segundo jugador 
    boton_perro2= Button(frame_2jugadores,image=imagen_perro)
    boton_panda2= Button(frame_2jugadores,image=imagen_panda)
    boton_dinosaurio2= Button(frame_2jugadores,image=imagen_dinosaurio)
    boton_tigre2= Button(frame_2jugadores,image=imagen_tigre)
    boton_gato2= Button(frame_2jugadores,image=imagen_gato)
    # Mantener la referencia a la imagen
    boton_perro2.image = imagen_perro
    boton_panda2.image = imagen_panda
    boton_dinosaurio2.image = imagen_dinosaurio
    boton_tigre2.image = imagen_tigre
    boton_gato2.image = imagen_gato
    #colocar los botones
    boton_perro2.place(x=10,y=500)
    boton_panda2.place(x=280,y=500)
    boton_dinosaurio2.place(x=560,y=500)
    boton_tigre2.place(x=840,y=500)
    boton_gato2.place(x=1250,y=500)

    # Dibuja la imagen en el canvas
    fondo_canvass.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvass.image = fondo_imagen  # Mantén una referencia a la imagen
    #label de nickname
    fondo_canvass.create_text(100, 50, text="PLAYER1:", font=("Arial", 24), fill="#FEF9F2")   
    fondo_canvass.create_text(100, 450, text="PLAYER2:", font=("Arial", 24), fill="#FEF9F2")   
    nombre_jugador1 = Entry(frame_2jugadores)
    nombre_jugador1.place(x=200,y=40)
    nombre_jugador2 = Entry(frame_2jugadores)
    nombre_jugador2.place(x=200,y=440)
    #eliminar pantallas no deseadas
    if 'frame_jugadores' in globals():
        frame_jugadores.pack_forget()
    if 'frame_animacion'in globals():
        frame_animacion.pack_forget()
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
    regresar = Button(frame_scores, text='BACK', command=ir_a_inicio, bg='#243642', 
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
    regresar.place(relx=1.0, rely=1.0, anchor='se', x=-10, y=-10)

    # Dibuja la imagen en el canvas
    fondo_canvass.create_image(0, 0, anchor='nw', image=fondo_imagen)
    fondo_canvass.image = fondo_imagen

    frames['marcadores'] = frame_scores  # Añade el nuevo frame al diccionario
    mostrar_pantalla(frame_scores, frames)

caras = []
jugadores=['jugador1','jugador2']
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
    if caras:  # Verifica que la lista de caras no esté vacía
        gif_label.config(image=caras[frame_num])
        frame_num += 1
        if frame_num >= len(caras):
            frame_num = 0
        inicio.after(90, update_gif, frame_num)  # Llama de nuevo a update_gif
#una funcion que gener el primer jugador 
def finalizar_animacion():
    global resultado_label
    # Detener la animación
    gif_label.pack_forget()
    
    # Escoger un jugador aleatorio
    jugador_seleccionado = random.choice(jugadores)
    
    # Mostrar quién inicia
    resultado_label = fondo_canvass.create_text(100, 50, text=f"Inicia: {jugador_seleccionado}", font=("Arial", 24), fill="#FEF9F2")
    

def animacion():
    global frame_animacion, gif_label
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
    gif_label = Label(frame_animacion,borderwidth=-2,width=500, height=500)
    gif_label.place(x=500,y=200)

    # Iniciar la animación del GIF
    update_gif(0)  # Llamada inicial a update_gif
    # Detener la animación después de 3 segundos y escoger un jugador
    inicio.after(20, finalizar_animacion)

    frames['animacion'] = frame_animacion  
    if 'frame_2jugadores' in globals():
        frame_2jugadores.pack_forget()
    mostrar_pantalla(frame_animacion, frames)

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
    regresar = Button(frame_info, text='BACK', command=ir_a_inicio, bg='#243642', 
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
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
    exit=Button(frame_inicio,text='EXIT', command=cerrar_aplicacion, bg='#243642', 
                    borderwidth=8, highlightbackground='#257180', highlightcolor='#257180', font=('Helvetica', 17), fg='white')
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