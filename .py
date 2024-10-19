import tkinter as tk

def crear_ventana():
    ventana = tk.Tk()
    ventana.title("Ventana con márgenes")

    # Configura el tamaño mínimo de la ventana
    ventana.minsize(300, 200)

    # Configura los márgenes de las columnas y filas
    ventana.grid_columnconfigure(0, weight=1)  # Permite que la columna se expanda
    ventana.grid_rowconfigure(0, weight=1)     # Permite que la fila se expanda

    # Crea un botón con márgenes
    boton1 = tk.Button(ventana, text="Botón 1")
    boton1.grid(row=0, column=0, padx=10, pady=10, sticky="ew")

    boton2 = tk.Button(ventana, text="Botón 2")
    boton2.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

    ventana.mainloop()

crear_ventana()
