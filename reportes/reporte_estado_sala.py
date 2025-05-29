import pandas as pd
from reportes.reporte_base import ReporteBase

# Reporte que calcula temperatura y humedad promedio por sala.
class ReporteEstadoSala(ReporteBase):
    def generar_reporte(self, logs_validos: list) -> pd.DataFrame:
        if not logs_validos:
            return pd.DataFrame(columns=["Sala", "Temperatura Promedio", "Humedad Promedio"])

        df = pd.DataFrame(logs_validos)

        ## Preprocesamiento de datos
        # Validar columnas requeridas
        if "sala" not in df.columns or "temperatura" not in df.columns or "humedad" not in df.columns:
            raise ValueError("Faltan columnas necesarias en los datos")

        # Convertir a numérico y eliminar filas con errores / nan
        df["temperatura"] = pd.to_numeric(df["temperatura"], errors="coerce")
        df["humedad"] = pd.to_numeric(df["humedad"], errors="coerce")
        df = df.dropna(subset=["temperatura", "humedad"])

        # Entregable como dataframe
        resultado = (
            df.groupby("sala")[["temperatura", "humedad"]]
            .mean()
            .reset_index()
            .rename(columns={
                "sala": "Sala",
                "temperatura": "Temperatura Promedio",
                "humedad": "Humedad Promedio"
            })
        )

        return resultado
