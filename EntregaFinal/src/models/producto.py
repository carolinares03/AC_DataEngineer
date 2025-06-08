from sqlalchemy import Column, Integer, String, Float
from src.models.base import Base  # Base patrón Singleton

class Producto(Base):
    # Modelo que representa la tabla products en la base de datos
    __tablename__ = 'products'

    ProductID = Column(Integer, primary_key=True)  # ID único del producto
    ProductName = Column(String(100), nullable=False)  # Nombre del producto
    Price = Column(Float, nullable=False)  # Precio del producto
    CategoryID = Column(Integer)  # FK a la categoría
    Class = Column(String(45))  # Clase o categoría adicional
    ModifyDate = Column(String(20))  # Fecha de modificación (formato "hh:mm.ss")
    Resistant = Column(String(45))  # Resistencia del producto
    IsAllergic = Column(String(10))  # Indicador de alergia
    VitalityDays = Column(Integer)  # Duración en días del producto

    def aplicar_descuento(self, porcentaje):
        # Aplica un descuento porcentual al precio del producto
        if porcentaje < 0 or porcentaje > 100:
            raise ValueError("El porcentaje de descuento debe estar entre 0 y 100")
        self.Price *= (1 - porcentaje / 100)

    def actualizar_stock(self, cantidad, operacion='sumar'):
        # Método para actualizar stock (sumar o restar)
        pass  # Implementar si se añade atributo stock

    def es_alergico(self):
        # Retorna True si el producto puede causar alergias
        return self.IsAllergic.lower() in ['yes', 'true', 'sí', 'si']

    def __repr__(self):
        return f"<Producto(nombre={self.ProductName}, precio={self.Price}, vitality_days={self.VitalityDays})>"
