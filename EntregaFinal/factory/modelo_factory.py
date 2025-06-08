from src.models.producto import Product
from src.models.empleado import Employee

class ModelFactory:
    @staticmethod
    def crear(modelo, **kwargs):
        clases = {
            'product': Product,
            'employee': Employee
        }
        cls = clases.get(modelo)
        if not cls:
            raise ValueError(f'Modelo {modelo} desconocido.')
        return cls(**kwargs)
