import tkinter as tk

# Crear la ventana principal
root = tk.Tk()
root.title("Ejemplo de GIF en Tkinter")

# Cargar el GIF
gif_image = tk.PhotoImage(file="imagenes/monedagirando.gif")  # Asegúrate de que la ruta sea correcta

# Crear un label y asignar el GIF
label = tk.Label(root, image=gif_image)
label.pack()

# Iniciar el bucle principal
root.mainloop()
