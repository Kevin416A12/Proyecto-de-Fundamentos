def obtener_mejores_puntajes(lineas, mejores=None):
    if mejores is None:
        mejores = []

    if not lineas:
        return mejores[:3]  # Asegúrate de devolver solo los tres mejores

    try:
        nombre_actual, puntaje_actual = lineas[0].strip().split(':')
        puntaje_actual = int(puntaje_actual)
    except (ValueError, IndexError):
        return obtener_mejores_puntajes(lineas[1:], mejores)

    # Llama a la función que actualiza los mejores puntajes
    mejores = actualizar_mejores(nombre_actual, puntaje_actual, mejores)

    # Llamada recursiva con el resto de las líneas
    return obtener_mejores_puntajes(lineas[1:], mejores)


def actualizar_mejores(nombre, puntaje, mejores):
    # Agrega el nuevo puntaje a la lista de mejores si hay menos de 3
    if len(mejores) < 3:
        mejores.append((nombre, puntaje))
        mejores.sort(key=lambda x: x[1], reverse=True)
        return mejores

    # Si el nuevo puntaje es mayor que el más bajo en mejores
    if puntaje > mejores[-1][1]:
        mejores[-1] = (nombre, puntaje)
        mejores.sort(key=lambda x: x[1], reverse=True)

    return mejores


# Función para leer el archivo y obtener los tres mejores puntajes
def leer_puntajes():
    try:
        with open("puntajes.txt", "r") as f:
            lineas = f.readlines()
            mejores = obtener_mejores_puntajes(lineas)  # Obtener los mejores puntajes
            return completar_mejores(mejores)  # Llama a la función recursiva para completar
    except FileNotFoundError:
        return [("", 0), ("", 0), ("", 0)]  # Devuelve ceros si el archivo no existe


def completar_mejores(mejores):
    # Caso base: si hay 3 o más elementos, devuelve la lista actual
    if len(mejores) >= 3:
        return mejores

    # Caso recursivo: añade un puntaje vacío y llama de nuevo
    mejores.append(("", 0))
    return completar_mejores(mejores)  # Llama de nuevo a completar_mejores


# Función para actualizar el label de puntaje más alto
def actualizar_puntaje_mas_alto():
    global best_scores
    best_scores = leer_puntajes()

    # Actualiza el texto del label con los mejores puntajes
    indicadorm.config(
        text=f"BEST SCORES:\n1. {best_scores[0][0]}: {best_scores[0][1]}\n2. {best_scores[1][0]}: {best_scores[1][1]}\n3. {best_scores[2][0]}: {best_scores[2][1]}")