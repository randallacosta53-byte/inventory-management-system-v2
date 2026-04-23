from core.productos import registrar_producto, registrar_salida
from core.reportes import ver_inventario, productos_proximos_a_vencer, generar_reporte

def menu():
    while True:
        print("\n===== SISTEMA DE INVENTARIO FRUTILOGÍSTICA CR =====")
        print("1. Registrar nuevo producto")
        print("2. Registrar salida de producto")
        print("3. Ver inventario actual")
        print("4. Ver productos próximos a vencer")
        print("5. Generar reporte general")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            registrar_salida()
        elif opcion == "3":
            ver_inventario()
        elif opcion == "4":
            productos_proximos_a_vencer()
        elif opcion == "5":
            generar_reporte()
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()