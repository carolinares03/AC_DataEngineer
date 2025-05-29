# decoradores.py
import time
import functools

# Contiene decoradores para logging y benchmarking.
class Decoradores:
    @staticmethod
    def log_ejecucion(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[LOG] Ejecutando {func.__name__}...")
            resultado = func(*args, **kwargs)
            print(f"[LOG] Finalizó {func.__name__}.")
            return resultado
        return wrapper

    @staticmethod
    def medir_tiempo(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            inicio = time.time()
            resultado = func(*args, **kwargs)
            fin = time.time()
            print(f"[BENCHMARK] {func.__name__} tardó {fin - inicio:.4f} segundos.")
            return resultado
        return wrapper
