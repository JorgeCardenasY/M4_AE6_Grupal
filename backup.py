import os
import datetime

def backup():
    x = datetime.datetime.now()
    x = x.strftime("%Y-%m-%d-%H%M%S")
    
    nombre_respaldo = f'inventario_bak_{x}.txt'
    os.system(f'copy inventario.txt inventario_bak_{x}.txt')
    print(f'\n   ===   RESPALDO  CREADO   ===\n-> Se ha creado el respaldo {nombre_respaldo}\n-> Tamaño del respaldo: {os.path.getsize(f"inventario_bak_{x}.txt")} bytes')
    return

