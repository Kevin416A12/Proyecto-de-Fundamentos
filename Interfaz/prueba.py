import random
from tkinter import *
from PIL import Image, ImageTk

caras = []  # Cambiamos el nombre a 'caras'
jugadores = ["Jugador 1", "Jugador 2"]  # Aquí puedes definir los nombres de los jugadores

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

def finalizar_animacion():
    # Detener la animación
    gif_label.config(image="")
    
    # Escoger un jugador aleatorio
    jugador_seleccionado = random.choice(jugadores)
    
    # Mostrar quién inicia
    resultado_label = Label(frame_animacion, text=f"Inicia: {jugador_seleccionado}", font=('Helvetica', 24), fg='black')
    resultado_label.place(relx=0.5, rely=0.5, anchor='center')

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
    gif_label = Label(frame_animacion, borderwidth=-2, width=500, height=500)
    gif_label.place(x=500, y=200)

    # Iniciar la animación del GIF
    update_gif(0)  # Llamada inicial a update_gif
    
    # Detener la animación después de 3 segundos y escoger un jugador
    inicio.after(3000, finalizar_animacion)

    frames['animacion'] = frame_animacion  
    if 'frame_2jugadores' in globals():
        frame_2jugadores.pack_forget()
    mostrar_pantalla(frame_animacion, frames)
