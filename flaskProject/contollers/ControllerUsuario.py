from flask import Blueprint, request, render_template, flash, url_for, redirect
from random import randint
from alchemyClasses import  Usuario
from models.ModelUsuario import*

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')


@usuario_blueprint.route('/') #localhost:5000/usuario/
def ver_usuarios():
    usuarios = obtener_todos_los_usuarios()
    return render_template('Usuario/usuario.html', usuarios=usuarios)

#responde a localhost:5000/usuario/id/1
@usuario_blueprint.route('/id/<int:id_usuario>') #<tipo:nombre_variable>
def ver_usuario_id(id_usuario):
    usuarios = obtener_usuario_por_id(id_usuario) 
    return render_template('Usuario/usuario.html', usuarios=usuarios)

@usuario_blueprint.route('/eliminar/<int:id_usuario> ') 
def eliminar_usuarios(id_usuario):
    eliminar_usuario(id_usuario)
    return redirect(url_for('usuario.ver_usuarios'))

@usuario_blueprint.route('/modificar/<int:id_usuario>', methods=['GET', 'POST'])
def modificar_usuarios(id_usuario):
    if request.method == "GET":
        usuario = obtener_usuario_por_id(id_usuario)
        return render_template('Usuario/formulario.html', informacion = usuario)
    else:
        modificar_usuario(id_usuario, request.get_json())
        return redirect(url_for('usuario.ver_usuarios'))

@usuario_blueprint.route('/agregar', methods=['GET', 'POST'])
def agregar_usuarios():
    if request.method == "GET":
        return render_template('Usuario/formulario.html', informacion = None)
    else:
        agregar_usuario(request)
        return redirect(url_for('usuario.ver_usuarios'))
  