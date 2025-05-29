# Sistema de Procesamiento LogsWatch
Este proyecto procesa archivos de logs ambientales en formato CSV, validando su contenido, almacenando registros válidos, reportando errores y generando reportes personalizados con opciones de exportación y gráficos.

## Instalación y configuración

1. Crear y activar un entorno virtual (recomendado):  
--> Desde consola (cmd)
    python -m venv venv
    venv\Scripts\activate   

2. Instalar las dependencias:
    pip install -r requirements.txt

## Componentes principales
main.py
Interfaz principal para interacción con el usuario. Permite listar archivos en /entradas, seleccionar y procesar archivos, mostrar estadísticas básicas y generar reportes exportables.

LogsManager
Gestiona la lista y selección de archivos válidos (.csv, .json) disponibles para procesar.

Log
Lee y valida registros CSV, almacena logs válidos en caché, registra errores en archivo, muestra resumen general, genera reportes personalizados, exporta resultados y grafica datos.
Atributos principales:
- fuente: ruta del archivo a procesar.
- tipo_fuente: formato del archivo (por defecto "csv").
- logs_validos: lista de registros válidos.
- logs_invalidos: lista de registros inválidos con motivo.
- cache: instancia de RegistroCache para almacenamiento temporal.

Decoradores
Funciones reutilizables para loguear ejecución y medir tiempo de funciones clave, usadas para debugging y análisis de rendimiento.

RegistroCache
Maneja un sistema de caché temporal en memoria con ventana de tiempo configurable para registros válidos recientes.

ReporteFactory
Implementa patrón fábrica para generar distintos tipos de reportes a partir de los datos validados.

## Flujo de ejecución
1. Se inicia main.py. 
2. Se muestran archivos disponibles en /entradas. 
3. Usuario selecciona uno o más archivos. 
4. Se leen y validan registros de cada archivo. 
5. Se reportan errores encontrados. 
6. Se muestra resumen general con totales y principales errores. 
7. Usuario puede generar reportes personalizados. 
8. Reportes pueden ser exportados a .csv o .xlsx. 
9. Se generan gráficos y se guardan en /salidas si corresponde.

## Requisitos
Python 3.8 o superior
