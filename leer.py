def leer_inventario():
    try:
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            return archivo.readlines()
    except FileNotFoundError:
        print("El archivo 'inventario.txt' no existe.")
        return []


def leer_inventario_completo():
    print("\nINVENTARIO COMPLETO")
    lineas = leer_inventario()  
    if lineas:
        for linea in lineas:
            print(linea.strip())  
    else:
        print("El inventario está vacío o el archivo no existe.")


