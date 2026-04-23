import csv
import datetime
import os

ARCHIVO = "inventario.csv"

def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []

    with open(ARCHIVO, mode='r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        return list(lector)

def ver_inventario():
    datos = cargar_datos()
    if not datos:
        print("Inventario vacío.")
        return

    print("\nINVENTARIO ACTUAL")
    print("-" * 60)
    for producto in datos:
        print(f'ID: {producto["ID"]} | Nombre: {producto["Nombre"]} | '
              f'Ingreso: {producto["FechaIngreso"]} | Vence: {producto["FechaVencimiento"]} | '
              f'Cantidad: {producto["Cantidad"]}')
    print("-" * 60)

def productos_proximos_a_vencer():
    datos = cargar_datos()
    if not datos:
        print("Inventario vacío.")
        return

    hoy = datetime.date.today()
    print("\nPRODUCTOS PRÓXIMOS A VENCER (5 días o menos)")
    print("-" * 60)
    encontrados = False
    for producto in datos:
        try:
            fecha_venc = datetime.datetime.strptime(producto["FechaVencimiento"], "%Y-%m-%d").date()
            dias_restantes = (fecha_venc - hoy).days
            if 0 <= dias_restantes <= 5:
                encontrados = True
                print(f'ID: {producto["ID"]} | Nombre: {producto["Nombre"]} | '
                      f'Vence en {dias_restantes} días | Cantidad: {producto["Cantidad"]}')
        except Exception as e:
            continue
    if not encontrados:
        print("No hay productos próximos a vencer.")
    print("-" * 60)

def generar_reporte():
    datos = cargar_datos()
    if not datos:
        print("No hay datos para generar el reporte.")
        return

    total_productos = len(datos)
    total_unidades = sum(int(p["Cantidad"]) for p in datos)

    print("\nREPORTE GENERAL")
    print("-" * 60)
    print(f"Total de registros de productos: {total_productos}")
    print(f"Total de unidades en inventario: {total_unidades}")

    vencidos = 0
    hoy = datetime.date.today()
    for producto in datos:
        try:
            fecha_venc = datetime.datetime.strptime(producto["FechaVencimiento"], "%Y-%m-%d").date()
            if fecha_venc < hoy:
                vencidos += 1
        except:
            continue

    print(f"Productos vencidos: {vencidos}")
    print("-" * 60)