
from sqlalchemy import Column, Integer, String, DateTime
from .base import Base


class Persona(Base):
    """Class Persona - test"""

    __tablename__ = "person"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String,)
    father_lastname = Column(String)
    mother_lastname = Column(String)
    age = Column(Integer)
    fecha_creacion = Column(DateTime)