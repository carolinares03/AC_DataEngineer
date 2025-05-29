from abc import ABC, abstractmethod

## Clase base abstracta para todos los reportes.
# Define la interfaz que deben implementar los reportes concretos.
class ReporteBase(ABC):
    @abstractmethod
    def generar_reporte(self, logs_validos):
        """
        Método para procesar los logs y generar el reporte.
        :parametro logs_validos: lista de diccionarios con logs validados.
        :return: estructura con los datos procesados del reporte.
        """
        pass
