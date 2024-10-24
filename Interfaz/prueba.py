from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk

# Crear la ventana principal
root = Tk()
root.geometry("800x600")

# Crear un Canvas
canvas = Canvas(root, width=800, height=600,bg='blue')
canvas.pack()

# Lista de imágenes para los botones
imagenes = {
    'boton1': 'imagenes/gato.png',
    'boton2': 'imagenes/dinosaurio.png',
    'boton3': 'imagenes/panda .png',
}

# Función para insertar la imagen en el Canvas
def insertar_imagen(boton):
    ruta_imagen = imagenes[boton]
    imagen = Image.open(ruta_imagen)
    imagen = imagen.resize((100, 100))  # Ajusta el tamaño según sea necesario
    foto = ImageTk.PhotoImage(imagen)
    canvas.create_image(400, 300, image=foto)  # Cambia las coordenadas según sea necesario
    canvas.image = foto  # Mantener una referencia de la imagen

# Crear botones que llamen a insertar_imagen
boton1 = Button(root, text='Insertar Imagen 1', command=lambda: insertar_imagen('boton1'))
boton1.pack()

boton2 = Button(root, text='Insertar Imagen 2', command=lambda: insertar_imagen('boton2'))
boton2.pack()

boton3 = Button(root, text='Insertar Imagen 3', command=lambda: insertar_imagen('boton3'))
boton3.pack()

# Ejecutar el bucle principal
root.mainloop()
