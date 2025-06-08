from sqlalchemy import Column, Integer, String
from src.models.base import Base  # Base patrón Singleton

class Categoria(Base):
    # Modelo que representa la tabla categories en la base de datos
    __tablename__ = 'categories'

    CategoryID = Column(Integer, primary_key=True)  # ID único de la categoría
    CategoryName = Column(String(45))  # Nombre de la categoría

    def cambiar_nombre(self, nuevo_nombre):
        # Permite actualizar el nombre de la categoría
        self.CategoryName = nuevo_nombre

    def __repr__(self):
        return f"<Categoria(nombre={self.CategoryName})>"
