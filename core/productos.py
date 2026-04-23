import datetime
from .base_datos import cargar_datos, guardar_datos, generar_nuevo_id

def registrar_producto():
    datos = cargar_datos()

    nombre = input("Nombre del producto: ").strip()
    fecha_ingreso = input("Fecha de ingreso (YYYY-MM-DD): ").strip()
    fecha_vencimiento = input("Fecha de vencimiento (YYYY-MM-DD): ").strip()
    cantidad = input("Cantidad: ").strip()

    # Validaciones básicas
    try:
        datetime.datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        datetime.datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        cantidad = int(cantidad)
        if cantidad < 1:
            raise ValueError
    except ValueError:
        print("Error: formato de fecha o cantidad inválido.")
        return

    nuevo_id = generar_nuevo_id(datos)
    nuevo_producto = {
        "ID": str(nuevo_id),
        "Nombre": nombre,
        "FechaIngreso": fecha_ingreso,
        "FechaVencimiento": fecha_vencimiento,
        "Cantidad": str(cantidad)
    }

    datos.append(nuevo_producto)
    guardar_datos(datos)
    print("Producto registrado exitosamente.")

def registrar_salida():
    datos = cargar_datos()
    if not datos:
        print("Inventario vacío.")
        return

    id_producto = input("Ingrese el ID del producto a dar salida: ").strip()
    cantidad_salida = input("Cantidad a retirar: ").strip()

    try:
        cantidad_salida = int(cantidad_salida)
        if cantidad_salida < 1:
            raise ValueError
    except ValueError:
        print("Error: cantidad inválida.")
        return

    for producto in datos:
        if producto["ID"] == id_producto:
            cantidad_actual = int(producto["Cantidad"])
            if cantidad_salida > cantidad_actual:
                print("⚠️ No hay suficiente stock disponible.")
                return
            producto["Cantidad"] = str(cantidad_actual - cantidad_salida)
            guardar_datos(datos)
            print("✅ Salida registrada.")
            return

    print("Producto no encontrado.")