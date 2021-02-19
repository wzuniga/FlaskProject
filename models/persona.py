
from sqlalchemy import Column, Integer, String, DateTime
from .base import Base


class Persona(Base):
    """
    Clase usada para manejo de datos persistentes

    ...

    Attributes
    ----------
    id : int
        Id en base de datos
    name : str
        Nombre de la persona
    father_lastname : str
        Apellido paterno de la persona
    mother_lastname : str
        Apellido materno de la persona
    age : int
        Edad de la persona
    fecha_creacion : DateTime
        Fecha de creacion, campo autocreado
    """

    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,)
    father_lastname = Column(String)
    mother_lastname = Column(String)
    age = Column(Integer)
    fecha_creacion = Column(DateTime)