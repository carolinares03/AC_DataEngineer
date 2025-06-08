--------- Sistema de Gestión de Productos, Empleados y Clientes ---------
Este proyecto implementa un sistema de gestión utilizando Python y SQLAlchemy para modelar entidades como productos, empleados, clientes y categorías. También permite generar reportes visuales con Matplotlib y conectarse a una base de datos MySQL mediante SQLAlchemy y variables de entorno.

El código está organizado en una estructura modular para facilitar el mantenimiento y la expansión futura. Cada clase representa una entidad de negocio con atributos específicos y métodos propios, incluyendo validaciones personalizadas. Además, se incluye un menú interactivo en consola para acceder fácilmente a todas las funcionalidades del sistema.


--------- Estructura del Proyecto ---------
El proyecto está estructurado en carpetas separadas para conexión a la base de datos (db), modelos (models), generación de reportes, una fábrica de clases (factories) y un archivo principal main.py para ejecutar la aplicación desde la terminal.

src/
├── db/
│   └── conector.py          # Clase singleton para manejar la conexión a la base de datos
├── models/
│   ├── base.py              # Clase base para los modelos ORM
│   ├── producto.py          # Modelo Product
│   ├── empleado.py          # Modelo Employee
│   ├── cliente.py           # Modelo Cliente
│   ├── categoria.py         # Modelo Categoria
│   └── reportes.py          # Módulo para generación de reportes con Matplotlib
│   ├── base.py              # Clase base para los modelos ORM
│   ├── producto.py          # Modelo Product 
├── factory/
    └── model_factory.py     # Clase para instanciar modelos dinámicamente
utils/
    └── logging.py           # Clase decorator
└──  main.py                 # Menú interactivo
.env                         # Variables de entorno
requirements.txt             # Dependencias del proyecto

--------- Requisitos ---------
- Python 3.8 o superior
- MySQL como sistema de base de datos
- Archivo .env con las variables necesarias para la conexión a la base de datos (no se sube el personal por cuestiones de seguridad)


--------- Instalación ---------
Clonar el repositorio:
git clone https://github.com/tuusuario/ENTREGABLEFINAL.git
cd ENTREGABLEFINAL

Crear un entorno virtual e instalar las dependencias:
- python -m venv venv
- source venv/bin/activate   # En Windows: venv\Scripts\activate
- pip install -r requirements.txt
- Crear un archivo .env en la raíz del proyecto y completar las credenciales de la base de datos.

--------- Ejecución ---------
Ejecutar el archivo principal:
- python src/main.py

Esto abrirá un menú interactivo por consola desde el cual se pueden realizar las siguientes acciones-

- Listar productos, empleados o clientes
- Agregar nuevos registros
- Modificar datos existentes (como nombre, dirección, precio, etc.)
- Generar reportes visuales de distintos aspectos del sistema


--------- Código ---------

Reportes
El archivo reportes.py permite generar gráficos utilizando Matplotlib con los siguientes análisis:
- Productos por categoría
- Ventas por empleado
- Mejores clientes
- Productos más vendidos
Los gráficos se abren automáticamente en ventanas emergentes interactivas al ejecutarse cada reporte.


Modelos y ORM
Cada modelo está desarrollado usando SQLAlchemy y representa una tabla en la base de datos. Algunos modelos disponibles:
- Producto: nombre, precio, clase, resistencia, alergias, categoría
- Empleado: nombre, edad, fecha de ingreso
- Cliente: nombre completo, dirección
- Categoría: nombre de la categoría

Cada clase incluye validaciones automáticas y funciones útiles, como:
- aplicar descuento en productos
- nombre completo en empleados o clientes
- cálculo de antigüedad o verificación de edad legal en empleados


Fábrica de Modelos
La clase ModelFactory permite instanciar modelos dinámicamente a partir de su tipo. Por ejemplo:

from src.factories.model_factory import ModelFactory
producto = ModelFactory.crear('product', ProductName="Agua", Price=10.5)

Esto facilita la creación de objetos sin necesidad de importar manualmente cada clase.


--------- Dependencias ---------
Las principales bibliotecas utilizadas son:
- SQLAlchemy
- pymysql
- python-dotenv
- matplotlib
- pandas

Todas están listadas en el archivo requirements.txt y se instalan con:
- pip install -r requirements.txt