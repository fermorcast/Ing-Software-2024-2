from sqlalchemy import Column, Integer, String

from alchemyClasses import db

class Pelicula(db.Model):

    __tablename__ = 'peliculas'
    idPelicula = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False)  
    genero = Column(String(45), default=None)  
    duracion = Column(Integer, default=None)
    inventario = Column(Integer, nullable=False, default=1)

    def __init__(self, nombre, genero, duracion, inventario):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f"ID: {self.idPelicula}, Nombre: {self.nombre}, Género: {self.genero}, Duración: {self.duracion}, Inventario: {self.inventario}"