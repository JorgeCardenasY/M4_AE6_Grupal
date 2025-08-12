from leer import leer_inventario

def visualizar_producto():
    print("\nVISUALIZAR PRODUCTO")
    nombre_busqueda = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False

    lineas = leer_inventario() 
    if lineas:
        for linea in lineas:
            if nombre_busqueda.lower() in linea.lower():
                print("Detalles del producto:")
                print(linea.strip())
                encontrado = True
                break  
        if not encontrado:
            print(f"Producto '{nombre_busqueda}' no encontrado en el inventario.")
    else:
        print("El inventario está vacío o el archivo no existe.")

