# Imprime argumentos y el resultado dado (debugging)
def log(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Ejecutando {func.__name__}: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"[LOG] Resultado: {result}")
        return result
    return wrapper