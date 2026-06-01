###########################################################################
#
## @file usuarios_db.py
#
###########################################################################
import os.path
__DBNAME__ = None
###########################################################################
#
#    Este modulo ofrece interfaces en forma de funciones para acceder
#    a los datos de la tabla usuairios que se guardan en un archivo .csv
#
###########################################################################
#tobias guzzo
#------------------------------------------------------------------------------
def iniciar_usuarios_db(path):
    """Funcion para iniciar la base de datos abriendo un archivo si no existe

    :param path: str con la direccion completa del archivo que se va a utizar
    :return None
    """
    global __DBNAME__
    if __DBNAME__ is None:
        __DBNAME__ = path
        if not os.path.isfile(__DBNAME__):
            archivo = open(__DBNAME__, "w")
            archivo.write("id,nombre,email,puntos\n")
            archivo.close()
    else:
        raise RuntimeError("La base de datos ya fue definida.")
#------------------------------------------------------------------------------
def agregar_usuario(id, nombre, email):
    """Funcion para agregar un usuario a la base de datos
    :param id: int
    :param nombre: str
    :param email: str
    :return: None
    """
    archivo = open(__DBNAME__, "a")
    archivo.write("{},{},{},{}\n".format(id, nombre, email, 0))
    archivo.close()
#------------------------------------------------------------------------------
def lista_de_usuarios():
    """Funcion para eliminar un usuario a la base de datos
    :return: lista de tuplas con los datos de los usuarios
    [(nombre, puntos),(nombre, puntos),(nombre, puntos)]
    """
    lista = []
    archivo = open(__DBNAME__, "r")
    linea = archivo.readline()
    linea = archivo.readline()
    while linea != "":
        contenido = linea.strip("\n")
        contenido = tuple(contenido.split(","))
        tupla_usuario = (contenido[1], contenido[3])
        lista.append(tupla_usuario)
        linea = archivo.readline()
    archivo.close()
    return lista
#------------------------------------------------------------------------------
def lista_usuarios_por_Puntajes():
    """Genera una lista de usuarios ordenados por puntajes.
    :return: lista de tuplas con los datos de los usuarios ordenados por puntaje
    [(nombre, puntos),(nombre, puntos),(nombre, puntos)]
    """
    archivo = open( __DBNAME__, "r")
    archivo_inicial = []
    archivo.readline()
    linea = archivo.readline()
    #en este while tuve ayuda
    while linea != "":
        linea_inicial = ""
        linea_secundaria = linea.split(",")
        linea_inicial += str(linea_secundaria[ 1 ])
        linea_inicial += ","
        linea_inicial += str(linea_secundaria[ 3 ].rstrip())
        linea_final = linea_inicial.split(" , ")
        archivo_inicial.append(linea_final)
        linea = archivo.readline()
    archivo.close()
    for i in range(len(archivo_inicial)-1):
        for j in range(len(archivo_inicial)-i-1):
            if int(archivo_inicial[ j ][ 1 ] ) < int( archivo_inicial[j + 1 ][ 1 ]):
                linea_secundaria = archivo_inicial[ j ]
                archivo_inicial[ j ] = archivo_inicial[ j + 1 ]
                archivo_inicial[ j + 1 ] = linea_secundaria
    return archivo_inicial
#------------------------------------------------------------------------------
def borrar_usuario(id):
    """Funcion para eliminar un usuario a la base de datos
    :param id: id del usuario
    :return: None
    """
    archivo_inicial = almacenamiento()
    archivo = open (__DBNAME__, "w")
    archivo.write("id,nombre,mail,puntos\n")
    for x in range (1,len(archivo_inicial)):
        if id != int(archivo_inicial[x][0]):
            archivo.write(archivo_inicial[x][0])
            for j in range (1,4):
                archivo.write(",")
                archivo.write(archivo_inicial[x][j])
    archivo.close()
#------------------------------------------------------------------------------
def existe_usuario(id):
    """Funcion determinar si un usuario está en la base de datos
    Si el usuario existe devuelve True
    Si elusuario no existe devuelve False
    :param id: int id del usuario
    :return: boolean
    """
    usuario = False
    lista = []
    archivo = open (__DBNAME__, "r")
    archivo.readline()
    linea = archivo.readline()
    while linea != "":
        linea = linea.strip("\n")
        linea= tuple(linea.split(","))
        if id == contenido[ 0 ]:
            encontrado = True
    archivo.close()
    return usuario
#------------------------------------------------------------------------------
def agregar_puntos(id , untos_a_sumar):
    """Funcion para sumarle puntos a un usuario
    :param id: int id del usuario
    :return:
    """
    archivo_inicial = almacenamiento()
    archivo = open( __DBNAME__, "w" )
    archivo.write( "id,nombre,mail,puntos" )
    for i in range ( 1 , len(archivo_inicial)):
        archivo.write ( archivo_inicial[i][0])
        for j in range (1,4):
            if id == int(archivo_inicial[i][0]) and j == 3:
                nuevos_puntos = str( int( archivo_inicial[ i ][ j ] ) + puntos_a_sumar)
                archivo.write( "," )
                archivo.write( nuevos_puntos )
                archivo.write( "\n" )
            else:
                archivo.write( "," )
                archivo.write( archivo_inicial[ i ][ j ] )
    archivo.close()
#------------------------------------------------------------------------------
def obtener_puntos(id):
    """Funcion para obtener los puntos de un usuario en la base
    :param id: int id del usuario
    :return: int puntos del usuario
    """
    repito = ""
    archivo_inicial = almacenamiento()
    for i in range( 1 , len( archivo_inicial ) ):
        if id == int( archivo_inicial[ i ][ 0 ] ):
            puntos = archivo_inicial[ i ][ 3 ]
    return repito
#------------------------------------------------------------------------------
def obtener_email(id):
    """Funcion para obtener el email de un usuario en la base
    :param id: int id del usuario
    :return: str email del usuario
    """
    repito = ""
    archivo_inicial = almacenamiento()
    for i in range( 1 , len( archivo_inicial ) ):
        if id == int( archivo_inicial[ i ][ 0 ] ):
            email = archivo_inicial[ i ][ 2 ]
    return repito
#------------------------------------------------------------------------------
def obtener_nombre(id):
    """Funcion para obtener el nombre de un usuario en la base
    :param id: int id del usuario
    :return: str nombre del usuario
    """
    repito = ""
    archivo_inicial = GuardarEnLista()
    for i in range( 1 , len( archivo_inicial ) ):
        if id == int( archivo_inicial[ i ][ 0 ] ):
            nombre = archivo_inicial[ i ][ 1 ]
    return repito
#------------------------------------------------------------------------------
def almacenamiento():
    archivo = open( __DBNAME__, "r" )
    archivo_original = []
    linea = archivo.readline()
    while linea != "":
        linea_split = linea.split( "," )
        archivo_original.append( linea_split )
        linea = archivo.readline()
    archivo.close()
    return archivo_original
#------------------------------------------------------------------------------
