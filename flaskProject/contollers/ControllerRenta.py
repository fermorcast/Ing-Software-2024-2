from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import  Renta
from models.ModelRenta import*


renta_blueprint = Blueprint('renta', __name__, url_prefix='/renta')

@renta_blueprint.route('/') #localhost:5000/renta/
def ver_rentas():
    rentas = obtener_todas_las_rentas()
    return render_template('Renta/renta.html', rentas=rentas)

#responde a localhost:5000/renta/id/1
@renta_blueprint.route('/id/<int:id_renta>') #<tipo:nombre_variable>
def ver_renta_id(id_renta):
    rentas = obtener_renta_por_id(id_renta) 
    return render_template('Renta/renta.html', rentas=rentas)


@renta_blueprint.route('/rentas/modificar/<int:idRenta>', methods=['GET', 'POST'])
def modificar_rentas(idRenta):
    modificar_estado_entrega(idRenta)
    return redirect(url_for("renta.ver_rentas"))


@renta_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_rentas():
    if request.method == "GET":
        print("no debo agregar")
        return render_template('Renta/formulario.html', informacion = None)
    else:
        print("estoy agre")
        agregar_renta(request)
        return redirect(url_for('renta.ver_rentas'))
  