def leer_inventario_completo():
    try:
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            lineas = archivo.readlines()
        
        if not lineas:
            print("El inventario está vacío.")
            return
        
        print("\nINVENTARIO COMPLETO:")
        for linea in lineas:
            print(linea.strip())
    except FileNotFoundError:
        print("El archivo 'inventario.txt' no existe.")
    except Exception as e:
        print(f"Error inesperado: {e}")