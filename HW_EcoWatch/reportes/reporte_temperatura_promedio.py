import pandas as pd
from reportes.reporte_base import ReporteBase

# Reporte que calcula la temperatura promedio por sala.
class ReporteTemperaturaPromedio(ReporteBase):
    def generar_reporte(self, datos: list) -> pd.DataFrame:
        if not datos:
            return pd.DataFrame(columns=["Sala", "Temperatura Promedio (°C)"])

        df = pd.DataFrame(datos)
        
        ## Preprocesamiento de datos
        # Validar columnas requeridas
        if "sala" not in df.columns or "temperatura" not in df.columns:
            raise ValueError("Faltan columnas necesarias en los datos")

        # Convertir a numérico y eliminar filas con errores
        df["temperatura"] = pd.to_numeric(df["temperatura"], errors="coerce")
        df = df.dropna(subset=["temperatura"])

        # Dataframe resultante con el promedio de temperatura por sala
        resultado = df.groupby("sala")["temperatura"].mean().reset_index()
        resultado.columns = ["Sala", "Temperatura Promedio (°C)"]
        return resultado
