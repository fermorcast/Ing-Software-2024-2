from sqlalchemy import Column, Integer, String, Boolean, String, LargeBinary

from alchemyClasses import db

class Usuario(db.Model):

    __tablename__ = 'usuarios'
    idUsuario = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    nombre = Column(String(200), nullable=False) 
    apPat = Column(String(200), nullable=False)  
    apMat = Column(String(200))
    password = Column(String(64), nullable=False)
    email = Column(String(500), unique=True, nullable=None)
    profilePicture = Column(LargeBinary)
    superUser = Column(Boolean, default=None)

    def __init__(self, nombre, ap_pat, ap_mat, password, email, profile_picture, super_user):
        self.nombre = nombre
        self.apPat = ap_pat
        self.apMat = ap_mat
        self.password = password
        self.email = email
        self.profilePicture = profile_picture
        self.superUser = super_user

    def __str__(self):
        return f"ID Usuario: {self.idUsuario}, Nombre: {self.nombre}, Apellido Paterno: {self.apPat}, Apellido Materno: {self.apMat}, Email: {self.email}, Super Usuario: {self.superUser}"