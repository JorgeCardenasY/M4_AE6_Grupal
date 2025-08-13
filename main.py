import os
import registrar #jorge 
import leer        #Emily
import visualizar  #emily
import modificar #jorge
import backup    #jorge
import consultar #Álvaro
import eliminar  #Álvaro

def menu_principal():
    while True:
        print("\nSISTEMA DE GESTIÓN DE INVENTARIO Moda Xpress")
        print("1. Registrar nuevo producto")
        print("2. Modificar producto")
        print("3. Visualizar producto")
        print("4. Consultar inventario completo")
        print("5. Crear respaldo")
        print("6. Consultar producto") 
        print("7. Eliminar producto") 
        print("8. Salir")
        
        opcion = input("Ingrese una opción: ")
        
        if opcion == '1':
            registrar.registrar_producto()
        elif opcion == '2':
            modificar.modificar_producto()
        elif opcion == '3':
            visualizar.visualizar_producto()
        elif opcion == '4':
            leer.leer_inventario_completo()
        elif opcion == '5':
            backup.backup()
        elif opcion == '6':
            consultar.consultar_producto() 
        elif opcion == '7':
            eliminar.eliminar_producto()   
        elif opcion == '8':
            print("Saliendo del sistema de gestión. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    menu_principal()