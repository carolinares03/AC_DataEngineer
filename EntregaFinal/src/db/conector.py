# Importamos las librerías necesarias
from sqlalchemy import create_engine, text         # Para crear la conexión con la base de datos
from sqlalchemy.orm import sessionmaker            # Para manejar sesiones (interacción con la DB)
from dotenv import load_dotenv                     # Para cargar las variables de entorno desde un archivo .env
import os                                          # Para acceder a las variables de entorno
import pandas as pd                                # Para manejo de tablas como dataframes
import pymysql

# Cargamos las variables de entorno definidas en el archivo .env
load_dotenv()

class ConectorBDD:
    # Atributo de clase que guardará la instancia única (Singleton)
    _instance = None

    def __new__(cls):
        # Si aún no se creó la instancia, la creamos
        if cls._instance is None:
            # Armamos la URL de conexión con los datos del .env
            db_url = (
                f"mysql+pymysql://{os.getenv('DB_USER')}:"
                f"{os.getenv('DB_PASSWORD')}@"
                f"{os.getenv('DB_HOST')}:"
                f"{os.getenv('DB_PORT')}/"
                f"{os.getenv('DB_NAME')}"
            )
            print(db_url)
            # Creamos el motor de conexión con SQLAlchemy
            engine = create_engine(db_url)

            # Creamos la instancia y le asignamos el engine y el sessionmaker
            cls._instance = super().__new__(cls)
            cls._instance.engine = engine
            cls._instance.Session = sessionmaker(bind=engine)

        # Devolvemos la instancia única (si ya existía, devuelve la misma)
        return cls._instance

    # Devuelve el engine (conexión directa)
    def get_engine(self):
        return self.engine

    # Devuelve una nueva sesión para ejecutar operaciones con ORM
    def get_session(self):
        return self.Session()
    
    # Ejecuta la consulta parametrizada (query) y devuelve un df con el resultado
    def ejecutar_sql(self, query):
        with self.engine.connect() as conn:
            return pd.read_sql(text(query), conn)
