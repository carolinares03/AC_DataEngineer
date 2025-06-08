from sqlalchemy import Column, Integer, String, DateTime
from src.models.base import Base  # Base patrón Singleton
from datetime import datetime

class Employee(Base):
    # Modelo que representa la tabla employees en la base de datos
    __tablename__ = 'employees'

    EmployeeID = Column(Integer, primary_key=True)  # ID único del empleado
    FirstName = Column(String(45))  # Nombre del empleado
    MiddleInitial = Column(String(1))  # Inicial del segundo nombre
    LastName = Column(String(45))  # Apellido del empleado
    BirthDate = Column(DateTime)  # Fecha de nacimiento
    Gender = Column(String(1))  # Género (M/F)
    CityID = Column(Integer)  # FK a la ciudad
    HireDate = Column(DateTime)  # Fecha de contratación

    def nombre_completo(self):
        # Devuelve el nombre completo del empleado, considerando inicial opcional
        return f"{self.FirstName} {self.MiddleInitial or ''} {self.LastName}".strip()

    def antiguedad(self):
        # Calcula años trabajados desde HireDate hasta hoy
        if not self.HireDate:
            return None
        hoy = datetime.now()
        delta = hoy - self.HireDate
        return delta.days // 365

    def es_mayor_de_edad(self):
        # Determina si el empleado tiene 18 años o más
        if not self.BirthDate:
            return None
        hoy = datetime.now()
        edad = (hoy - self.BirthDate).days // 365
        return edad >= 18

    def __repr__(self):
        return f"<Employee(nombre={self.nombre_completo()}, antiguedad={self.antiguedad()} años)>"
