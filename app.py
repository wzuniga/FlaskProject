from fastapi import FastAPI, Body, HTTPException
import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models.base import Base

from models.persona import Persona

engine = create_engine('sqlite:///database/store.db?check_same_thread=False')
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

app = FastAPI()

@app.get("/persons")
def get_persons():
    """Retorna todos lso elementos de la tabla persona.
    
        Return
        ------
        persons : dict
            Todos lso elementos en la tabla persona
    """

    persons = session.query(Persona).all()
    return persons

@app.post("/persons")
def add_person(person: dict = Body(...)):
    """Inserta un nuevo elemento en base a los datos enviados.
    
        Parameters
        ----------
        person : dict, required
            Valores de lso atributos dfe la clase Persona.

        Raises
        ------ 
        HTTPException 
            Si no contieen todos los datos requeridos para Persona.

        Return
        ------
        person : dict
            La variable enviada como confirmación
    """
    try:
        new_person = Persona(
            name = person["name"], 
            father_lastname = person["father_lastname"], 
            mother_lastname = person["mother_lastname"], 
            age = person["age"],
            fecha_creacion = datetime.datetime.now()
        )

        session.add(new_person)
        session.commit()
    except:
        session.rollback()
        raise HTTPException(status_code=404, detail="Mandatory data required")
    
    return person

@app.put("/persons/{person_id}")
def update_person(person_id: int, person: dict = Body(...)):
    """Actualiza un elemento en base al id enviado.
    
        Parameters
        ----------
        person_id: int, required
            Id de identificacion de Persona en la base de datos
        person : dict, required
            Valores de los atributos de la clase Persona que seran actualizados.

        Raises
        ------ 
        HTTPException 
            Si no existe el id en la tabla.

        Return
        ------
        person : dict
            La variable enviada como confirmación
    """

    try:
        current_person = session.query(Persona).get(person_id)
        current_person = session.query(Persona).filter_by(id=person_id).update(person)
        session.commit()
    except:
        session.rollback()
        raise HTTPException(status_code=404, detail="Item not found")
    return person


@app.delete("/persons/{person_id}")
def delete_person(person_id: int):
    """Elimina un elemento en base al id enviado.
    
        Parameters
        ----------
        person_id: int, required
            Id de identificacion de Persona en la base de datos

        Raises
        ------ 
        HTTPException 
            Si no existe el id en la tabla.

        Return
        ------
        person_id : dict
            La variable enviada como confirmación
    """

    try:
        person = session.query(Persona).filter(Persona.id == person_id).one()
        session.delete(person)
        session.commit()
    except:
        session.rollback()
        raise HTTPException(status_code=404, detail="Item not found")
    return person_id
