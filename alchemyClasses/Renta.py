from sqlalchemy import Column, Integer, DateTime, Boolean,ForeingKey

from alchemyClasses import db

class Renta(db.Model):

    __tablename__ = 'renta'
    id_rentar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    id_usuario = Column(Integer, ForeingKey('usuario.id_usuario'), nullable=False,)  
    id_pelicula = Column(Integer, ForeingKey('pelicula.ide_pelicula', nullable=False)) 
    fecha_renta = Column(DateTime, nullable=False)  
    dias_de_renta = Column(Integer, default=5)
    estatus =  Column(Boolean, default=False)

    def __init__ (self, id_usuario, id_pelicula, fecha_renta, dias_de_renta, estatus):
        self.id_usuario = id_usuario
        self.id_pelicula = id_pelicula
        self.fecha_renta = fecha_renta
        self.estatus = estatus

    def __str__(self):
        return f"ID Renta: {self.id_rentar}, ID Usuario: {self.id_usuario}, ID Película: {self.id_pelicula}, Fecha Renta: {self.fecha_renta}, Días de Renta: {self.dias_de_renta}, Estatus: {self.estatus}"
