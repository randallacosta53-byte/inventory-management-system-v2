import tkinter as tk
from tkinter import messagebox, ttk
import csv
import os
import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO = os.path.join(BASE_DIR, "inventario.csv")
COLUMNAS = ["ID", "Nombre", "FechaIngreso", "FechaVencimiento", "Cantidad"]

def cargar_datos():
    if not os.path.exists(ARCHIVO):
        return []
    with open(ARCHIVO, mode='r', newline='', encoding='utf-8') as archivo:
        return list(csv.DictReader(archivo))

def guardar_datos(datos):
    with open(ARCHIVO, mode='w', newline='', encoding='utf-8') as archivo:
        writer = csv.DictWriter(archivo, fieldnames=COLUMNAS)
        writer.writeheader()
        for fila in datos:
            writer.writerow(fila)

def generar_nuevo_id(datos):
    if not datos:
        return 1
    ids = [int(f["ID"]) for f in datos]
    return max(ids) + 1


def registrar_producto():
    nombre = entry_nombre.get()
    fecha_ingreso = entry_fecha_ingreso.get()
    fecha_vencimiento = entry_fecha_vencimiento.get()
    cantidad = entry_cantidad.get()

    try:
        datetime.datetime.strptime(fecha_ingreso, "%Y-%m-%d")
        datetime.datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        cantidad = int(cantidad)
        if cantidad < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Verifique las fechas (YYYY-MM-DD) y cantidad (>0)")
        return

    datos = cargar_datos()
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
    messagebox.showinfo("Éxito", "Producto registrado.")
    limpiar_campos()
    actualizar_tabla()

def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_fecha_ingreso.delete(0, tk.END)
    entry_fecha_vencimiento.delete(0, tk.END)
    entry_cantidad.delete(0, tk.END)
    entry_salida_id.delete(0, tk.END)
    entry_salida_cant.delete(0, tk.END)

def registrar_salida():
    datos = cargar_datos()
    id_buscado = entry_salida_id.get()
    cantidad_salida = entry_salida_cant.get()

    try:
        cantidad_salida = int(cantidad_salida)
        if cantidad_salida < 1:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Cantidad de salida inválida.")
        return

    for producto in datos:
        if producto["ID"] == id_buscado:
            cantidad_actual = int(producto["Cantidad"])
            if cantidad_salida > cantidad_actual:
                messagebox.showerror("Error", "Cantidad insuficiente en inventario.")
                return
            producto["Cantidad"] = str(cantidad_actual - cantidad_salida)
            guardar_datos(datos)
            messagebox.showinfo("Éxito", "Salida registrada.")
            limpiar_campos()
            actualizar_tabla()
            return

    messagebox.showerror("Error", "ID no encontrado.")


def mostrar_vencimientos():
    datos = cargar_datos()
    hoy = datetime.date.today()
    proximos = []

    for producto in datos:
        try:
            fecha_venc = datetime.datetime.strptime(producto["FechaVencimiento"], "%Y-%m-%d").date()
            dias = (fecha_venc - hoy).days
            if 0 <= dias <= 5:
                proximos.append((producto["ID"], producto["Nombre"], fecha_venc, producto["Cantidad"], dias))
        except:
            continue

    if not proximos:
        messagebox.showinfo("Sin vencimientos", "No hay productos por vencer en los próximos 5 días.")
    else:
        msg = ""
        for p in proximos:
            msg += f"ID: {p[0]} | {p[1]} | Vence en {p[4]} días | Cantidad: {p[3]}\n"
        messagebox.showinfo("Próximos a vencer", msg)


def actualizar_tabla():
    for fila in tabla.get_children():
        tabla.delete(fila)
    datos = cargar_datos()
    for producto in datos:
        tabla.insert("", tk.END, values=(
            producto["ID"], producto["Nombre"],
            producto["FechaIngreso"], producto["FechaVencimiento"],
            producto["Cantidad"]
        ))


ventana = tk.Tk()
ventana.title("Inventario - FrutiLogística CR")
ventana.geometry("850x600")


frame_form = tk.LabelFrame(ventana, text="Registrar Producto")
frame_form.pack(fill="x", padx=10, pady=5)

tk.Label(frame_form, text="Nombre:").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = tk.Entry(frame_form)
entry_nombre.grid(row=0, column=1, padx=5)

tk.Label(frame_form, text="Fecha Ingreso (YYYY-MM-DD):").grid(row=1, column=0, padx=5, pady=5)
entry_fecha_ingreso = tk.Entry(frame_form)
entry_fecha_ingreso.grid(row=1, column=1, padx=5)

tk.Label(frame_form, text="Fecha Vencimiento (YYYY-MM-DD):").grid(row=2, column=0, padx=5, pady=5)
entry_fecha_vencimiento = tk.Entry(frame_form)
entry_fecha_vencimiento.grid(row=2, column=1, padx=5)

tk.Label(frame_form, text="Cantidad:").grid(row=3, column=0, padx=5, pady=5)
entry_cantidad = tk.Entry(frame_form)
entry_cantidad.grid(row=3, column=1, padx=5)

btn_guardar = tk.Button(frame_form, text="Registrar Producto", command=registrar_producto)
btn_guardar.grid(row=4, column=0, columnspan=2, pady=10)

frame_salida = tk.LabelFrame(ventana, text="Registrar Salida de Producto")
frame_salida.pack(fill="x", padx=10, pady=5)

tk.Label(frame_salida, text="ID del producto:").grid(row=0, column=0, padx=5, pady=5)
entry_salida_id = tk.Entry(frame_salida)
entry_salida_id.grid(row=0, column=1, padx=5)

tk.Label(frame_salida, text="Cantidad a retirar:").grid(row=1, column=0, padx=5, pady=5)
entry_salida_cant = tk.Entry(frame_salida)
entry_salida_cant.grid(row=1, column=1, padx=5)

btn_salida = tk.Button(frame_salida, text="Registrar Salida", command=registrar_salida)
btn_salida.grid(row=2, column=0, columnspan=2, pady=10)


btn_vencimientos = tk.Button(ventana, text="Ver Productos Próximos a Vencer", command=mostrar_vencimientos)
btn_vencimientos.pack(pady=5)


frame_tabla = tk.LabelFrame(ventana, text="Inventario Actual")
frame_tabla.pack(fill="both", expand=True, padx=10, pady=5)


columnas = ("ID", "Nombre", "Ingreso", "Vencimiento", "Cantidad")
tabla = ttk.Treeview(frame_tabla, columns=columnas, show="headings")
for col in columnas:
    tabla.heading(col, text=col)
    tabla.column(col, anchor="center")

tabla.pack(fill="both", expand=True)
tabla.column("ID", width=60, anchor="center")
tabla.column("Nombre", width=150, anchor="w")
tabla.column("Cantidad", width=100, anchor="center")
tabla.column("Ingreso", width=100, anchor="center")
tabla.column("Vencimiento", width=100, anchor="center")

actualizar_tabla()
ventana.mainloop()