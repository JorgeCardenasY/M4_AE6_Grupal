import os

def registrar_producto():
    with open('inventario.txt', 'a') as file:
        producto = input('Por favor, ingresa el nombre y Color del producto:\n')
        precio = input('Por favor, ingresa el precio del producto (formato "123 USD"):\n')
        cantidad = input('Por favor, ingresa la cantidad del producto (formato "123 unidades"):\n')
        talla = input('Por favor, ingresa la talla del producto:\n')

        file.write(f'{producto}, {precio}, {cantidad}, {talla}\n')
        file.seek(0)

        with open('inventario.txt', 'r') as file:
            ultima_linea = file.readlines()[-1]
            print(f'El producto {ultima_linea} ha sido ingresado al sistema\n')

