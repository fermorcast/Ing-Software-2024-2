import pymysql
import datetime
import random
import string

def conectar_bd():
    try:
        connection = pymysql.connect(host='localhost',
                                     user='lab',   
                                     password='Developer123!',
                                     database='lab_ing_software')
        return connection
    except Exception as e:
        print("Error al conectar a la base de datos:", e)
        return None
    
def id_valido_usuario(conexion):

    with conexion.cursor() as cursor:
        cursor.execute("SELECT idUsuario FROM usuarios")
        id = [fila["idUsuario"] for fila in cursor.fetchall()]
        
        if id:
            return random.choice(id)
    
    return None

def id_valido_pelicula(conexion):

    with conexion.cursor() as cursor:
        cursor.execute("SELECT idPelicula FROM peliculas")
        id = [fila["idPelicula"] for fila in cursor.fetchall()]
        
        if id:
            return random.choice(id)
    
    return None

def generar_nombres(longitud):

    letras = string .ascii_lowercase
    return ''.join(random.choice(letras) for i in range(longitud))
nombre_aleatorio = generar_nombres(8)

def insertar_registros(connection):
 
    cursor = connection.cursor()
    try:
        cursor.execute(f"INSERT INTO Pelicula (nombre, genero, duracion, inventario) VALUES ({generar_nombres(10)}, {generar_nombres(34)}, {random.randint(0, 100)}, {random.randint(0,40)})")
        email = generar_nombres(10 + '@'+ generar_nombres(7) + '.com')
        cursor.execute(f"INSERT INTO Usuario (nombre, apPat, apMat, password, email, profilePicture, superUser) VALUES ({generar_nombres(10)}, {generar_nombres(10)}, {generar_nombres(10)}, {generar_nombres(10)}, {email()}, {os.urandom(70)}, {random.choice([True, False])})")
        cursor.execute(f"INSERT INTO Renta (idUsuario, idPelicula, fecha_renta, dias_de_renta, estatus) VALUES ({id_valido_usuario()}, {id_valido_pelicula()}, {datetime.today()}, {random.randit(0, 30)}, {random.choice([True,False])})")
        connection.commit()
        print("Registros insertados exitosamente.")
    except Exception as e:
        connection.rollback()
        print("Error al insertar registros:", e)
    finally:
        cursor.close()

def filtrar_por_apellido(connection, apellido):

    cursor = connection.cursor()
    try:
        cursor.execute("SELECT * FROM Usuario WHERE apPat  = %s OR apMat = %s" , (apellido , apellido))
        results = cursor.fetchall()
        for row in results:
            print(row)
    except Exception as e:
        print("Error al filtrar por apellido:", e)
    finally:
        cursor.close()

def cambiar_genero_pelicula(connection, nombre_pelicula, nuevo_genero):

    cursor = connection.cursor()
    try:
        cursor.execute("UPDATE Pelicula SET genero = %s WHERE nombre = %s", (nuevo_genero, nombre_pelicula))
        connection.commit()
        print("Género de la película actualizado correctamente.")
    except Exception as e:
        connection.rollback()
        print("Error al actualizar el género de la película:", e)
    finally:
        cursor.close()

def eliminar_rentas_antiguas(connection):

    cursor = connection.cursor()
    try:
        fecha_limite = datetime.datetime.now() - datetime.timedelta(days=3)
        cursor.execute("DELETE FROM Renta WHERE fecha < %s", (fecha_limite,))
        connection.commit()
        print("Rentas antiguas eliminadas correctamente.")
    except Exception as e:
        connection.rollback()
        print("Error al eliminar rentas antiguas:", e)
    finally:
        cursor.close()

if __name__ == "__main__":
    conexion = conectar_bd()
    if conexion:
        insertar_registros(conexion)
        filtrar_por_apellido(conexion, 'ApellidoUsuario')
        cambiar_genero_pelicula(conexion, 'NombrePelicula', 'NuevoGenero')
        eliminar_rentas_antiguas(conexion)
        conexion.close()
