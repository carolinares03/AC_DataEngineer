from collections import deque
from datetime import datetime, timedelta

## Clase encargada de la gestión y registro de cachés del sistema, incluyendo una ventana de minutos max
class RegistroCache:
    def __init__(self, ventana_minutos=5):
        self.ventana = timedelta(minutes=ventana_minutos)
        self.cache = deque()

    # Agrega un registro al cache si su timestamp es válido
    def agregar(self, registro):
        timestamp = datetime.fromisoformat(registro["timestamp"])
        self.cache.append((timestamp, registro))
        self.limpiar(timestamp)

    # Elimina registros fuera de la ventana temporal desde el extremo más viejo
    def limpiar(self, referencia):
        while self.cache and self.cache[0][0] < referencia - self.ventana:
            self.cache.popleft()

    def consultar_por_sala(self, sala):
        return [r for _, r in self.cache if r["sala"] == sala]

    # Devuelve los registros que coincidan exactamente con el timestamp dado
    def consultar_por_timestamp(self, ts):
        return [r for t, r in self.cache if t == datetime.fromisoformat(ts)]
    
    # Obtiene todos los cachés
    def obtener_todos(self):
        return [r for _, r in self.cache]
