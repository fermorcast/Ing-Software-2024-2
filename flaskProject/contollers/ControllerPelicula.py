from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import  Pelicula
from models.ModelPelicula import*



pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/') #localhost:5000/pelicula/
def ver_peliculas():
    peliculas = obtener_todas_las_peliculas() 
    return render_template('Pelicula/pelicula.html', peliculas=peliculas)


#responde a localhost:5000/pelicula/id/1
@pelicula_blueprint.route('/id/<int:id_pelicula>') #<tipo:nombre_variable>
def ver_pelicula_id(id_pelicula):
    peliculas = obtener_pelicula_por_id(id_pelicula) 
    return render_template('Pelicula/pelicula.html', peliculas=peliculas)

    #return f"Se hace el query con el id {id_pelicula} y el nombre {nombre}"

@pelicula_blueprint.route('/eliminar/<int:id_pelicula>') 
def eliminar_peliculas(id_pelicula):
    eliminar_pelicula(id_pelicula)
    return redirect(url_for('pelicula.ver_peliculas'))

@pelicula_blueprint.route('/modificar/<int:id_pelicula>', methods=['GET', 'POST'])
def modificar_peliculas(id_pelicula):
    print("modificando")
    if request.method == "GET":
        pelicula = obtener_pelicula_por_id(id_pelicula)
        return render_template('Pelicula/formulario.html', informacion = pelicula)
    else:
        modificar_pelicula(id_pelicula, request.get_json())
        return redirect(url_for('pelicula.ver_peliculas'))

@pelicula_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_peliculas():
    if request.method == "GET":
        return render_template('Pelicula/formulario.html', informacion = None)
    else:
        agregar_pelicula(request)
        return redirect(url_for('pelicula.ver_peliculas'))
  