import csv
import os

ARCHIVO = "inventario.csv"
COLUMNAS = ["ID", "Nombre", "FechaIngreso", "FechaVencimiento", "Cantidad"]

def cargar_datos():
    datos = []
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, mode='r', newline='', encoding='utf-8') as archivo:
            lector = csv.DictReader(archivo)
            for fila in lector:
                datos.append(fila)
    return datos

def guardar_datos(datos):
    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)
        escritor.writeheader()
        for fila in datos:
            escritor.writerow(fila)

def generar_nuevo_id(datos):
    if not datos:
        return 1
    ids = [int(fila["ID"]) for fila in datos]
    return max(ids) + 1