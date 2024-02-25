from sqlalchemy import Column, Integer, String, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

engine = create_engine('sqlite:///nombre_de_tu_base_de_datos.db')  
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()


def mostrar_registros(tabla):
    registros = session.query(tabla).all()
    for registro in registros:
        print(registro.__dict__)

def filtrar_por_id(tabla, id):
    registro = session.query(tabla).filter_by(id=id).first()
    if registro:
        print(registro.__dict__)
    else:
        print("No se encontró ningún registro con ese ID.")

def actualizar_registro(tabla, id, nombre=None, fecha=None):
    registro = session.query(tabla).filter_by(id=id).first()
    if registro:
        if nombre:
            registro.nombre = nombre
        if fecha:
            registro.fecha = fecha
        session.commit()
        print("Registro actualizado correctamente.")
    else:
        print("No se encontró ningún registro con ese ID.")

def eliminar_registro(tabla, id=None):
    if id:
        registro = session.query(tabla).filter_by(id=id).first()
        if registro:
            session.delete(registro)
            session.commit()
            print("Registro eliminado correctamente.")
        else:
            print("No se encontró ningún registro con ese ID.")
    else:
        session.query(tabla).delete()
        session.commit()
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
            mostrar_registros(tabla.capitalize())
        elif opcion == "2":
            tabla = input("Ingrese el nombre de la tabla (pelicula, usuario o renta): ")
            id = input("Ingrese el ID del registro a filtrar: ")
            filtrar_por_id(tabla.capitalize(), id)
        elif opcion == "3":
            tabla = input("Ingrese el nombre de la tabla (pelicula, usuario o renta): ")
            id = input("Ingrese el ID del registro a actualizar: ")
            nombre = input("Ingrese el nuevo nombre (deje en blanco si no desea actualizar): ")
            fecha = input("Ingrese la nueva fecha (deje en blanco si no desea actualizar): ")
            actualizar_registro(tabla.capitalize(), id, nombre, fecha)
        elif opcion == "4":
            tabla = input("Ingrese el nombre de la tabla (pelicula, usuario o renta): ")
            id = input("Ingrese el ID del registro a eliminar (deje en blanco para eliminar todos los registros): ")
            eliminar_registro(tabla.capitalize(), id)
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número del 1 al 5.")

if __name__ == "__main__":
    menu_principal()
