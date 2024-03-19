from sqlalchemy import Column, Integer, DateTime, Boolean,ForeignKey

from alchemyClasses import db

class Renta(db.Model):

    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False,)  
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False) 
    fecha_renta = Column(DateTime, nullable=False)  
    dias_de_renta = Column(Integer, default=5)
    estatus =  Column(Boolean, default=False)

    def __init__ (self, id_usuario, id_pelicula, fecha_renta, dias_de_renta, estatus):
        self.idUsuario = id_usuario
        self.idPelicula = id_pelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus

    def __str__(self):
        return f"ID Renta: {self.idRentar}, ID Usuario: {self.idUsuario}, ID Película: {self.idPelicula}, Fecha Renta: {self.fecha_renta}, Días de Renta: {self.dia_de_renta}, Estatus: {self.estatus}"