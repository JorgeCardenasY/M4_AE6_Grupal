#Leer los datos de un producto específico.

def Leer_producto_especifico():
    
    # 1. Preguntar al usuario por el nombre del producto que quiere buscar.
    nombre_producto = input("Ingrese el nombre del producto que desea buscar: ")
    encontrado = False

    try:
        with open("inventario.txt", "r", encoding="utf-8") as file:
            # 3. Leer el archivo línea por línea.
            for linea in file:
                # 4. Procesar cada línea.
                #    .strip() elimina espacios en blanco y saltos de línea.
                #    .split(',') separa la línea en una lista por las comas.
                datos_producto = linea.strip().split(',')
                # Obtener el nombre del producto (es el primer elemento de la lista).
                nombre_en_inventario = datos_producto[0].strip()

                # 5. Comparar el nombre buscado con el nombre del inventario.
                if nombre_en_inventario.lower() == nombre_buscado.lower():
                    print("\n--- Detalles del Producto ---")
                    print(f"Nombre: {datos_producto[0].strip()}")
                    print(f"Precio: {datos_producto[1].strip()}")
                    print(f"Cantidad: {datos_producto[2].strip()}")
                    print(f"Tamaño: {datos_producto[3].strip()}")
                    encontrado = True
                    # Salir del bucle una vez que se encuentre el producto.
                    break
        
        # 6. Informar si el producto no se encontró.
        if not encontrado:
            print(f"\nEl producto '{nombre_buscado}' no se encontró en el inventario.")

    except FileNotFoundError:
        print("Error: El archivo de inventario 'inventario.txt' no se encontró.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")