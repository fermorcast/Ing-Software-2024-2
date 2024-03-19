

from alchemyClasses.Usuario import Usuario
from alchemyClasses import db

def agregar_usuario(informacion):
    nombre = informacion.form.get("nombre")
    ap_pat = informacion.form.get("ap_pat")
    ap_mat = informacion.form.get("ap_mat")
    password = informacion.form.get("password")
    email = informacion.form.get("email")
    super_user = informacion.form.get("super_user") == "on"

    nuevo_usuario = Usuario(nombre, ap_pat, ap_mat, password, email, None, super_user)
    db.session.add(nuevo_usuario)
    db.session.commit()

def eliminar_usuario(id_usuario):
    usuario = Usuario.query.get(id_usuario)
    db.session.delete(usuario)
    db.session.commit()

def modificar_usuario(id_usuario, informacion):
    usuario = Usuario.query.get(id_usuario)
    usuario.nombre = informacion.form.get("nombre")
    usuario.ap_pat = informacion.form.get("ap_pat")
    usuario.ap_mat = informacion.form.get("ap_mat")
    usuario.password = informacion.form.get("password")
    usuario.email = informacion.form.get("email")
    usuario.super_user = informacion.form.get("super_user") =="on"
    db.session.commit()

def obtener_todos_los_usuarios():
    try:
        informacion = Usuario.query.all()
        return informacion 
    except Exception as e:
        print("Error 1:" + str(e))
    return []


def obtener_usuario_por_id(id_usuario):
    return Usuario.query.get(id_usuario)
