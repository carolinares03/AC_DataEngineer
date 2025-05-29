import pandas as pd
from reportes.reporte_base import ReporteBase

# Reporte que identifica logs con CO2 > 1000 o temperatura > 30 como alertas críticas.
class ReporteAlertasCriticas(ReporteBase):
    def generar_reporte(self, logs_validos: list) -> pd.DataFrame:
        if not logs_validos:
            return pd.DataFrame(columns=["sala", "co2", "temperatura"])

        df = pd.DataFrame(logs_validos)

        if "co2" not in df.columns or "temperatura" not in df.columns:
            raise ValueError("Faltan columnas necesarias en los datos")

        df["co2"] = pd.to_numeric(df["co2"], errors="coerce")
        df["temperatura"] = pd.to_numeric(df["temperatura"], errors="coerce")

        alertas = df[(df["co2"] > 1000) | (df["temperatura"] > 30)].copy()
        return alertas.reset_index(drop=True)
