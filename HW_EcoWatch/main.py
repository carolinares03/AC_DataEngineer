from logs_manager import LogsManager
from logs import Log

def mostrar_menu_reportes():
    print("\n¿Qué tipo de reporte querés generar?")
    print("1. Estado de sala")
    print("2. Alertas críticas")
    print("3. Temperatura promedio")
    print("4. Ninguno")

    opciones = {
        "1": "estado_sala",
        "2": "alertas_criticas",
        "3": "reporte_temperatura_promedio",
        "4": "ninguno",
        "": "ninguno"
    }

    while True:
        eleccion = input("Seleccioná una opción (1/2/3/4): ").strip()
        if eleccion in opciones:
            return opciones[eleccion]
        else:
            print("Opción inválida, intentá de nuevo.")


if __name__ == "__main__":
    manager = LogsManager()

    while True:
        print("\n=== Archivos disponibles ===")
        manager.list_logs()
        print("\nElegí los archivos que querés cargar:")
        print("- Ingresá números separados por coma (ej: 1,3,4)")
        print("- Ingresá 'todos' o '*' para seleccionar todos")
        print("- Ingresá 'x' para salir\n")

        entrada = input("Tu elección: ").strip().lower()

        if entrada in ("x", "salir"):
            print("Saliendo del programa.")
            break

        if entrada in ("todos", "*"):
            archivos_seleccionados = manager.files
        else:
            try:
                indices = [int(i.strip()) - 1 for i in entrada.split(",")]
                archivos_seleccionados = [manager.files[i] for i in indices]
            except (ValueError, IndexError):
                print("Entrada inválida, intentá de nuevo.")
                continue

        for archivo in archivos_seleccionados:
            print(f"\n📄 Procesando archivo: {archivo}")
            log = Log(archivo)
            log.leer_logs()
            log.reporte()

            tipo_reporte = mostrar_menu_reportes()
            if tipo_reporte != "ninguno":
                log.generar_reporte_personalizado(tipo_reporte)
