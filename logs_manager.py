from pathlib import Path

# Clase encargada de la gestión de archivos de logs
class LogsManager:
    def __init__(self, carpeta="entradas", extensions=(".csv", ".json")):
        self.base_path = Path.cwd() / carpeta  # Ruta actual + /entradas
        print("ruta: " + str(self.base_path))
        self.extensions = extensions
        self.files = self.get_available_logs()

    # Obtiene archivos de logs disponibles
    def get_available_logs(self):
        if not self.base_path.exists():
            print(f"La carpeta {self.base_path} no existe.")
            return []
        return [f for f in self.base_path.iterdir() if f.suffix in self.extensions and f.is_file()]

    # Devuelve el listado de logs disponibles para el usuario
    def list_logs(self):
        if not self.files:
            print("No se encontraron archivos de log.")
            return
        for i, file in enumerate(self.files):
            print(f"[{i}] {file.name}")

    # Valida y selecciona los logs elegidos por el usuario
    def select_logs(self, index):
        if index < 0 or index >= len(self.files):
            raise IndexError("Índice fuera de rango.")
        return self.files[index]
