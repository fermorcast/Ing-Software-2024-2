from flask import Flask
from sqlalchemy import and_, or_
from datetime import datetime
from alchemyClasses import db
from alchemyClasses.Pelicula import Pelicula
from alchemyClasses.Renta import Renta
from alchemyClasses.Usuario import Usuario
from cryptoUtils.CryptoUtils import cipher
from hashlib import sha256

from model.model_alumno import borra_alumno

#mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft
#<dialecto>+<driver>://<usuario>:<passwd>@localhost:3306/<db>
#mysql+pymysql://lab:Developer123!@localhost:3306/lab_ing_soft
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ferfong:Developer123!@localhost:3306/ing_soft'
app.config.from_mapping(
    SECRET_KEY='dev'
)
db.init_app(app)

def ver_tabla(tabla):
    if tabla == Pelicula:
        for pelicula in Pelicula.query.all(): # Select * from alumno
            print(pelicula)

    if tabla == Renta:
        for renta in Renta.query.all(): # Select * from alumno
            print(renta)

    if tabla == Usuario:    
        for usuario in Usuario.query.all: # Select * from alumno
            print(usuario)   

def filtrar_registro(tabla, id):

    if tabla == Pelicula:
        for pelicula in Pelicula.query.filter(and_(Pelicula.id == id)): #Un booleano a evaluar.
                print(f"Pelicula es:  {pelicula.__str__()}")

    if tabla == Renta:  
        for renta in Renta.query.filter(and_(Renta.id_rentar == id)): #Un booleano a evaluar.
                print(f"Renta es:  {renta.__str__()} ")

    if tabla == Usuario:     
        for usuario in Usuario.query.filter(and_(Usuario.id_usuario == id)): #Un booleano a evaluar.
                print(f"Usuario es:  {usuario.__str__()}")

    
def actualizar(tabla, nombre, id):

    if tabla == Pelicula:
        pelicula = Pelicula.query.filter(Pelicula.id == id).first()
        pelicula.nombre = nombre
        db.session.commit()
        
    if tabla == Usuario:
        usuario = Usuario.query.filter(Usuario.id_usuario == id).first()
        usuario.nombre = nombre
        db.session.commit()

    if tabla == Renta:   
        renta = Renta.query.filter(Renta.id_rentar == id).first()
        renta.fecha_renta = datetime.today()
        db.session.commit()
        

def eliminar_registro(tabla, id=None):
    if tabla == Pelicula:
        if id:
            registro = db.session.query(Pelicula).filter_by(id=id).first()
            if registro:
                rentas = db.session.query(Renta).filter.by(Renta.id_pelicula == id).all()
                for renta in rentas: 
                    db.session.delete(renta) 
                db.session.delete(registro)
                db.session.commit()
                print("Registro eliminado correctamente.")
            else:
                print("No se encontró ningún registro con ese ID.")
        else:
            db.session.query(Pelicula).delete()
            db.session.query(Renta).delete()
            db.session.commit()
            print("Todos los registros han sido eliminados.")

    if tabla == Usuario:
        if id:
            registro = db.session.query(Usuario).filter_by(id=id).first()
            if registro:
                rentas = db.session.query(Renta).filter.by(Renta.id_usuario== id).all()
                for renta in rentas: 
                    db.session.delete(renta) 
                db.session.delete(registro)
                db.session.commit()
                print("Registro eliminado correctamente.")
            else:
                print("No se encontró ningún registro con ese ID.")
        else:
            db.session.query(Renta).delete()
            db.session.query(Usuario).delete()
            db.session.commit()
            print("Todos los registros han sido eliminados.")

    if tabla == Renta:   
        if id:
            registro = db.session.query(Renta).filter_by(id=id).first()
            if registro:
                db.session.delete(registro)
                db.session.commit()
                print("Registro eliminado correctamente.")
            else:
                print("No se encontró ningún registro con ese ID.")
        else:
            db.session.query(Renta).delete()
            db.session.commit()
            print("Todos los registros han sido eliminados.")

def menu_principal():
    while True:
        print("\nMenú:")
        print("1. Ver registros de una tabla")
        print("2. Filtrar registros por ID")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Salir")

        opcion = input("Ingrese el número de opción: ")

        if opcion == "1":
            tabla = input("Ingrese el nombre de la tabla (pelicula, usuario o renta): ")
            ver_tabla(tabla.capitalize())

        elif opcion == "2":
            tabla = input("Ingrese el nombre de la tabla (pelicula, usuario o renta): ")
            id = input("Ingrese el ID del registro a filtrar: ")
            filtrar_registro(tabla.capitalize(), id)

        elif opcion == "3":
            tabla = input("Ingrese el nombre de la tabla (pelicula, usuario o renta): ")
            id = input("Ingrese el ID del registro a actualizar: ")
            nombre = input("Ingrese el nuevo nombre (deje en blanco si no desea actualizar): ")
            fecha = input("Ingrese la nueva fecha (deje en blanco si no desea actualizar): ")
            actualizar(tabla.capitalize(), nombre, id)

        elif opcion == "4":
            tabla = input("Ingrese el nombre de la tabla (pelicula, usuario o renta): ")
            id = input("Ingrese el ID del registro a eliminar (deje en blanco para eliminar todos los registros): ")
            eliminar_registro(tabla.capitalize(), id)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")
            
if __name__ == '__main__':
    with app.app_context():
        menu_principal()

        #Create
        """valeria = Alumno('Valeria', 'Ramirez', 319311918, apMat=None, password=sha256(cipher("Developer123#")).hexdigest())
        db.session.add(valeria)
        db.session.commit()"""
        #Update
        #Primero tenemos que buscar el objeto que queremos.
        #Ya que lo tengo, entonces cambio el atributo.
        #Y entonces hago el commit.
        #fer = Alumno.query.filter(Alumno.nombre == 'Fernando').first()
        #print(type(fer))
        #fer.nombre = "Fer"
        #fer.ap_mat = "Baeza"
        #db.session.commit()
        #Delete
        #borra_alumno(313320679)
        #print("Borrado con éxito!")