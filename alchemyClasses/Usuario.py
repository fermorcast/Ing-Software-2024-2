from sqlalchemy import Column, Integer, String, Boolean, String, LargeBinary

from alchemyClasses import db

class Usuario(db.Model):

    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False) 
    ap_pat = Column(String(200), nullable=False)  
    ap_mat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500), unique=True, nullable=None)
    profile_picture = Column(LargeBinary)
    super_user = Column(Boolean, default=None)

    def __init__(self, nombre, ap_pat, ap_mat, password, email, profile_picture, super_user):
        self.nombre = nombre
        self.ap_pat = ap_pat
        self.ap_mat = ap_mat
        self.password = password
        self.email = email
        self.profile_picture = profile_picture
        self.super_user = super_user

    def __str__(self):
        return f"ID Usuario: {self.id_usuario}, Nombre: {self.nombre}, Apellido Paterno: {self.ap_pat}, Apellido Materno: {self.ap_mat}, Email: {self.email}, Super Usuario: {self.super_user}"
