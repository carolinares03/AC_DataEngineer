from datetime import datetime
from registro_cache import RegistroCache
import csv
from collections import Counter
from reportes.reporte_factory import ReporteFactory
from utils.decoradores import Decoradores
import pandas as pd
import matplotlib.pyplot as plt

# Clase encargada de los logs del sistema
class Log:
    campos = ["timestamp", "estado", "sala", "temperatura", "humedad", "co2"]

    def __init__(self, fuente, tipo_fuente="csv"):
        self.fuente = fuente
        self.tipo_fuente = tipo_fuente
        self.logs_validos = []
        self.logs_invalidos = []
        self.razones_invalidos = []
        self.cache = RegistroCache()

    @Decoradores.log_ejecucion
    @Decoradores.medir_tiempo
    def leer_logs(self):
        # Selecciona el método de lectura en función del tipo de fuente
        if self.tipo_fuente == "csv":
            return self.leer_csv()
        else:
            raise NotImplementedError(f"Tipo de fuente no soportado: {self.tipo_fuente}")
    
    # Lee un archivo CSV y valida cada fila
    def leer_csv(self):
        with open(self.fuente, newline='', encoding='utf-8') as csvfile:
            lector = csv.DictReader(csvfile)
            for fila in lector:
                valido, motivo = self.validar_fila(fila)
                if valido:
                    self.logs_validos.append(fila)
                    self.cache.agregar(fila)
                else:
                    fila["error"] = motivo
                    self.logs_invalidos.append(fila)
                    self.razones_invalidos.append(motivo)

        self.guardar_errores()
    
    # Valida que todos los campos estén presentes y que el timestamp tenga formato válido
    def validar_fila(self, fila):
        for campo in self.campos:
            if campo not in fila or fila[campo].strip() == "":
                return False, f"Falta campo: {campo}"
        try:
            datetime.fromisoformat(fila["timestamp"])
        except ValueError:
            return False, "Timestamp inválido"
        return True, ""
    
    # Guarda los registros inválidos en un archivo CSV de errores
    def guardar_errores(self):
        if not self.logs_invalidos:
            return

        with open("errores_logs.csv", "a", newline="", encoding="utf-8") as archivo:
            campos = list(self.logs_invalidos[0].keys())
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            archivo.seek(0, 2)  # Moverse al final del archivo
            if archivo.tell() == 0:
                escritor.writeheader()
            for fila in self.logs_invalidos:
                escritor.writerow(fila)
    
    # Muestra estadísticas básicas y los errores más comunes
    def reporte(self):
        total = len(self.logs_validos) + len(self.logs_invalidos)
        print(f"Total de registros: {total}")
        print(f"Válidos: {len(self.logs_validos)}")
        print(f"Inválidos: {len(self.logs_invalidos)}")

        if self.logs_invalidos:
            contador = Counter(self.razones_invalidos)
            top_3 = contador.most_common(3)
            print("\n⚠️  Principales errores encontrados:")
            for error, cantidad in top_3:
                print(f"- {error}: {cantidad} ocurrencias")

        print(f"\n🧠 Registros válidos almacenados en caché: {len(self.cache.obtener_todos())}")

    @Decoradores.log_ejecucion
    def generar_reporte_personalizado(self, tipo_reporte: str):
        """
        Usa la factory para crear el reporte, lo ejecuta con los logs válidos,
        y permite exportar el resultado y visualizar gráficos si aplica.
        """
        try:
            reporte = ReporteFactory.crear_reporte(tipo_reporte)
            resultado = reporte.generar_reporte(self.logs_validos)

            print(f"\n📊 --- Reporte '{tipo_reporte}' ---\n")

            # Muestra el resultado si es un DataFrame
            if isinstance(resultado, pd.DataFrame):
                print(resultado.to_string(index=False))
            else:
                print(resultado)

            # Arma el archivo .csv o .xlsx en base a la elección del usuario
            exportar = input("\n¿Querés guardar el reporte? (csv/xlsx/ninguno): ").strip().lower()
            if exportar == "csv":
                nombre_archivo = f"reporte_{tipo_reporte}.csv"
                self.exportar_csv(resultado, nombre_archivo)
            elif exportar == "xlsx":
                nombre_archivo = f"reporte_{tipo_reporte}.xlsx"
                self.exportar_excel(resultado, nombre_archivo)

            # Genera gráfico si le es posible (columnas numéricas disponibles)
            if isinstance(resultado, pd.DataFrame) and not resultado.empty:
                self.graficar_reporte(resultado, tipo_reporte)

        except Exception as e:
            print(f"❌ Error al generar el reporte: {e}")

    
    # Exporta a CSV si el resultado es un DataFrame o lista de dicts
    def exportar_csv(self, resultado, nombre_archivo):
        if isinstance(resultado, pd.DataFrame):
            resultado.to_csv('salidas/'+nombre_archivo, index=False)
        elif isinstance(resultado, list):
            df = pd.DataFrame(resultado)
            df.to_csv('salidas/'+nombre_archivo, index=False)
        print(f"✅ Reporte exportado como {nombre_archivo}")

    # Exporta a Excel si el resultado es un DataFrame o lista de dicts
    def exportar_excel(self, resultado, nombre_archivo):
        if isinstance(resultado, pd.DataFrame):
            resultado.to_excel('salidas/'+nombre_archivo, index=False)
        elif isinstance(resultado, list):
            df = pd.DataFrame(resultado)
            df.to_excel('salidas/'+nombre_archivo, index=False)
        print(f"✅ Reporte exportado como {nombre_archivo}")

    # Genera un gráfico de barras si hay columnas numéricas disponibles
    def graficar_reporte(self, df: pd.DataFrame, tipo_reporte: str):
        try:
            columnas_numericas = df.select_dtypes(include="number").columns
            if "Sala" in df.columns:
                df.set_index("Sala", inplace=True)
            if not columnas_numericas.empty:
                df[columnas_numericas].plot(kind="bar", figsize=(10, 6), title=f"Reporte: {tipo_reporte}")
                plt.ylabel("Valores")
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.tight_layout()
                # Obtener fecha y hora actual en formato año-mes-día_hora-minuto-segundo
                timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

                # Construir nombre de archivo con fecha y hora
                nombre_grafico = f"salidas/grafico_{tipo_reporte}_{timestamp}.png"

                plt.savefig(nombre_grafico)
                plt.show()
                print(f"📈 Gráfico guardado como {nombre_grafico}")
                
        except Exception as e:
            print(f"⚠️ No se pudo generar gráfico: {e}")
