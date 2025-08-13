def modificar_producto():
    try:
        with open('inventario.txt', 'r') as archivo:
            lineas = archivo.readlines()

        print("\nLista de productos:")
        for i, linea in enumerate(lineas, 1):
            print(f"Producto {i}: {linea.strip()}")
        
        num_producto = int(input("\nNúmero del producto a modificar: "))
        if num_producto < 1 or num_producto > len(lineas):
            print("Error: Número de producto inválido")
            return
            
        nuevo_dato =[]
        while  len(nuevo_dato) == 0 :
            nuevo_dato = input("Ingrese los nuevos datos del producto: \n")
            
        lineas[num_producto - 1] = nuevo_dato

        with open('inventario.txt', 'w') as archivo:
            archivo.writelines(lineas)
        
        print(f"\nProducto {num_producto} modificado. Lista actualizada:")
        with open('inventario.txt', 'r') as archivo:
            for i, linea in enumerate(archivo, 1):
                print(f"Producto {i}: {linea.strip()}")

    except FileNotFoundError:
        print("Error: El archivo 'inventario.txt' no existe")
    except ValueError:
        print("Error: Debe ingresar un número entero")
    except IndexError:
        print("Error: Número de producto fuera de rango")
    except Exception as e:
        print(f"Error inesperado: {e}")

