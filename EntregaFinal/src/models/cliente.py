from sqlalchemy import Column, Integer, String
from src.models.base import Base   # Base patrón Singleton

class Cliente(Base):
    # Modelo que representa la tabla customers en la base de datos
    __tablename__ = 'customers'

    CustomerID = Column(Integer, primary_key=True)  # ID único del cliente
    FirstName = Column(String(45))  # Nombre del cliente
    MiddleInitial = Column(String(1))  # Inicial del segundo nombre
    LastName = Column(String(45))  # Apellido del cliente
    CityID = Column(Integer)  # FK a la ciudad
    Address = Column(String(90))  # Dirección del cliente

    def nombre_completo(self):
        # Devuelve el nombre completo del cliente, considerando inicial opcional
        return f"{self.FirstName} {self.MiddleInitial or ''} {self.LastName}".strip()

    def actualizar_direccion(self, nueva_direccion):
        # Actualiza la dirección del cliente
        self.Address = nueva_direccion

    def __repr__(self):
        return f"<Cliente(nombre={self.nombre_completo()}, dirección={self.Address})>"
