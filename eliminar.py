def eliminar_producto():
    try:
        with open("inventario.txt", "r", encoding="utf-8") as archivo:
            lineas = [linea.strip() for linea in archivo.readlines()]

        print("\nLista de productos:")
        for i, linea in enumerate(lineas, start=1):
            print(f"{i}. {linea}")
        
        num_producto = int(input("\nIngrese el número del producto a eliminar: "))
        if num_producto < 1 or num_producto > len(lineas):
            print("Número de producto inválido.")
            return

        # Eliminar la línea correspondiente al producto seleccionado
        new_lines = [linea for index, linea in enumerate(lineas) if index + 1 != num_producto]
        with open("inventario.txt", "w", encoding="utf-8") as archivo:
            for linea in new_lines:
                archivo.write(f"{linea}\n")

        print(f"\nProducto {num_producto} eliminado con éxito.")
    except FileNotFoundError:
        print("El archivo 'inventario.txt' no existe.")
    except ValueError:
        print("Debe ingresar un número entero.")
    except Exception as e:
        print(f"Error inesperado: {e}")