from reportes.reporte_estado_sala import ReporteEstadoSala
from reportes.reporte_alertas_criticas import ReporteAlertasCriticas
from reportes.reporte_temperatura_promedio import ReporteTemperaturaPromedio

## Clase Factory que devuelve una instancia del reporte solicitado
## Permite escalabilidad de sumar nuevos tipos de reporte sin cambiar main/log
class ReporteFactory:
    @staticmethod
    def crear_reporte(tipo: str):
        tipos = {
            "estado_sala": ReporteEstadoSala,
            "alertas_criticas": ReporteAlertasCriticas,
            "reporte_temperatura_promedio": ReporteTemperaturaPromedio
        }
        clase_reporte = tipos.get(tipo.lower())
        if not clase_reporte:
            raise ValueError(f"Tipo de reporte desconocido: {tipo}")
        return clase_reporte()
