from alchemyClasses.Renta import Renta
from alchemyClasses import db

def agregar_renta(informacion):
    print("informacion")
    print(informacion.form)
    id_usuario = informacion.form.get("idUsuario")
    id_pelicula = informacion.form.get("idPelicula")
    fecha_renta = informacion.form.get("fecha_renta")
    dias_de_renta = informacion.form.get("dias_de_renta")
    estatus = informacion.form.get("estatus") == "rentada"

    nueva_renta = Renta(id_usuario, id_pelicula, fecha_renta, dias_de_renta, estatus)
    db.session.add(nueva_renta)
    db.session.commit()

def modificar_estado_entrega(id_renta):
    renta = Renta.query.get(id_renta)
    renta.estatus = not renta.estatus 
    db.session.commit()


def obtener_todas_las_rentas():
    try:
        informacion = Renta.query.all()
        return informacion 
    except Exception as e:
        print("Error 1:" + str(e))
    return []


def obtener_renta_por_id(id_renta):
    return Renta.query.get(id_renta)


# def obtener_todas_las_rentas():
#     rentas = Renta.query.all()

#     for renta in rentas:
#         # Calcular la fecha de vencimiento sumando los días de renta a la fecha de renta
#         fecha_vencimiento = renta.fecha_renta + timedelta(days=renta.dias_de_renta)
#         # Si la fecha de vencimiento es anterior a la fecha actual, marcar la renta como vencida
#         renta.vencida = fecha_vencimiento < datetime.now()

#     return rentas
