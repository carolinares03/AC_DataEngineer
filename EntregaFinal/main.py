# Importamos las clases necesarias
from src.models.reportes import Reportes
from src.db.conector import ConectorBDD
from factory.modelo_factory import ModelFactory

# Función para mostrar el menú principal
def mostrar_menu():
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Ver reportes")
    print("2. Crear nuevo registro")
    print("3. Salir")

# Submenú de reportes
def menu_reportes():
    while True:
        print("\n--- REPORTES DISPONIBLES ---")
        print("1. Productos por categoría")
        print("2. Ventas por empleado")
        print("3. Mejores clientes")
        print("4. Productos más vendidos")
        print("5. Volver al menú principal")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            Reportes.productos_por_categoria()
        elif opcion == "2":
            Reportes.ventas_por_empleado()
        elif opcion == "3":
            Reportes.mejores_clientes()
        elif opcion == "4":
            Reportes.productos_mas_vendidos()
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

# Submenú para crear registros de modelos
def menu_creacion_modelos():
    while True:
        print("\n--- CREAR NUEVO REGISTRO ---")
        print("1. Crear producto")
        print("2. Crear empleado")
        print("3. Volver al menú principal")

        opcion = input("Elegí una opción: ")

        if opcion == "1":
            crear_modelo('product')
        elif opcion == "2":
            crear_modelo('employee')
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

# Función que permite crear instancias de productos o empleados
def crear_modelo(tipo):
    try:
        if tipo == 'product':
            print("\n--- Carga de nuevo Producto ---")
            data = {
                'ProductName': input("Nombre: "),
                'Price': float(input("Precio: ")),
                'CategoryID': int(input("ID de Categoría: ")),
                'Class': input("Clase: "),
                'ModifyDate': input("Fecha de modificación (hh:mm.ss): "),
                'Resistant': input("¿Es resistente? "),
                'IsAllergic': input("¿Puede causar alergia? "),
                'VitalityDays': int(input("Días de vida útil: "))
            }

        elif tipo == 'employee':
            print("\n--- Carga de nuevo Empleado ---")
            from datetime import datetime
            data = {
                'FirstName': input("Nombre: "),
                'MiddleInitial': input("Inicial del segundo nombre: "),
                'LastName': input("Apellido: "),
                'BirthDate': datetime.strptime(input("Fecha de nacimiento (YYYY-MM-DD): "), '%Y-%m-%d'),
                'Gender': input("Género (M/F): "),
                'CityID': int(input("ID de Ciudad: ")),
                'HireDate': datetime.strptime(input("Fecha de contratación (YYYY-MM-DD): "), '%Y-%m-%d')
            }

        # Creamos el objeto con ModelFactory
        nuevo_objeto = ModelFactory.crear(tipo, **data)

        # Obtenemos una sesión de la BDD y guardamos el objeto
        db = ConectorBDD()
        session = db.get_session()
        session.add(nuevo_objeto)
        session.commit()
        print(f"{tipo.capitalize()} creado exitosamente: {nuevo_objeto}")

    except Exception as e:
        print(f"Ocurrió un error al crear el {tipo}: {e}")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccioná una opción: ")

        if opcion == "1":
            menu_reportes()
        elif opcion == "2":
            menu_creacion_modelos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intentá de nuevo.")

# Ejecutamos la función principal
if __name__ == "__main__":
    main()
