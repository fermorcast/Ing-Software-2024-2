from alchemyClasses.Pelicula import Pelicula
from alchemyClasses import db
from alchemyClasses.Renta import Renta

def agregar_pelicula(informacion):
    nombre = informacion.form.get("nombre")
    genero = informacion.form.get("genero")
    duracion = informacion.form.get("duracion")
    inventario = informacion.form.get("inventario")

    nueva_pelicula = Pelicula(nombre, genero, duracion, inventario)
    db.session.add(nueva_pelicula)
    db.session.commit()

def modificar_pelicula(id_pelicula, nueva_informacion):
    print("modificando")
    print(nueva_informacion)
    pelicula = Pelicula.query.get(id_pelicula)
    pelicula.nombre = nueva_informacion.get("nombre")
    pelicula.genero = nueva_informacion.get("genero")
    pelicula.duracion = nueva_informacion.get("duracion")
    pelicula.inventario = nueva_informacion.get("inventario")
    db.session.commit()

def eliminar_pelicula(id_pelicula):
    Renta.query.filter_by(idPelicula=id_pelicula).delete()

    pelicula = Pelicula.query.get(id_pelicula)
    db.session.delete(pelicula)
    db.session.commit()

def obtener_todas_las_peliculas():
    try:
        informacion = Pelicula.query.all()
        return informacion 
    except Exception as e:
        print("Error 1:" + str(e))
    return []

def obtener_pelicula_por_id(id_pelicula):
    return Pelicula.query.get(id_pelicula)
