#tobias guzzo
#-----------------------------------------
import os
import usuarios_db as u
#-----------------------------------------
usuarios_db.iniciar_usuarios_db("usuarios.csv")
def menu():
    print("TOBIAS GUZZO")
    print("4*1")
    print ("-----------------------------------------------")
    print ("0 - salir")
    print ("-----------------------------------------------")
    print ("1 - agregar usuario")
    print ("-----------------------------------------------")
    print ("2 - borrar usuario")
    print ("-----------------------------------------------")
    print ("3 - mostrar nombre a partir del id")
    print ("-----------------------------------------------")
    print ("4 - mostrar email a partir del id")
    print ("-----------------------------------------------")
    print ("5 - mostrar puntos a partir del id")
    print ("-----------------------------------------------")
    print ("6 - listar usuarios")
    print ("-----------------------------------------------")
    print ("7 - listar usuarios ordenados por puntaje")
    print ("-----------------------------------------------")
    print ("8 - mostrar el podio")
    print ("-----------------------------------------------")
    print("9 - agragar puntos a usuarios")
    print ("\n")
    print ("Ingrese una opcion: ")
#-------------------------------------------------------------------------
opcion = -1
while opcion!=0:
    menu()
    opcion = int(input())
#------------------------------------------------------------------------
    if opcion==1:
        id = int(input("ingrese id:"))
        nombre = input("ingrese nombre:")
        email = input ("ingrse email:")
        u.agregar_usuario(id, nombre, email)
        print("se a registrado el nuevo usuario")
        print("\n")
#------------------------------------------------------------------------
    elif opcion ==2:
        id = int(input("ingrese id:"))
        if u.borrar_usuario(id):
            u.borrar_usuario(id)
            print("el usuario a sido eliminado ")
        else:
            print("este usuario no esxite")
            print("porfavor vea si ingreso bien el id")
            print("presione enter para continuar")
        print("\n")
#------------------------------------------------------------------------
    elif opcion == 3:
        id = int(input("ingrese id: "))
        if u.existe_usuario(id):
            nombre = u.obtener_nombre(id)
            print("el nombre del usuario",id,"es",nombre)
            print("precione enter para seguir")
        else:
            print("el archivo no existe")
            print("precione enter para seguir")
        print("\n")
#-----------------------------------------------------------------------
    elif opcion == 4:
        id = int(input("ingrese id: "))
        if u.existe_usuario(id):
            email = u.obtener_email(id)
            print("el email",id,"es",nombre)
            print("precione enter para seguir")
        else:
            print("no existe un usuarion con ese id")
            print("precione enter para seguir")
        print("\n")
#------------------------------------------------------------------------
    elif opcion == 5:
        id = int(input("Ingrese id: "))
        if u.existe_usuario(id):
            puntos = u.obtener_puntos(id)
            print("el usuario",id,"tiene",nombre)
            print("precione enter para seguir")
        else:
            print("no existe un usuarion con ese id")
            print("precione enter para seguir")
        print("\n")
#------------------------------------------------------------------------
    elif opcion==6:
        lista = u.lista_de_usuarios()
        print("Nombre \tpuntos")
        for e in lista:
            print("{} \t{}".format(e[0],e[1]))
        print("\n")
#------------------------------------------------------------------------
    elif opcion==7:
        por_puntos = u.lista_usuarios_por_Puntajes()
        for i in range(len(por_puntos)):
            usuario = por_puntos[ i ][ 0 ]
            puntaje = por_puntos[ i ][ 1 ]
            print(usuario , puntaje)
        print("\n")
#-----------------------------------------------------------------------
    elif opcion==8:
        por_puntos = u.lista_usuarios_por_Puntajes()
        x = len( por_puntos )
        if x >= 3:
            for i in range( 3 ):
                usuario = por_puntos[ i ][ 0 ]
                puntaje = por_puntos[ i ][ 1 ]
                print(usuario , puntaje)
        elif x == 2:
            for i in range( 2 ):
                usuario = por_puntos[ i ][ 0 ]
                puntaje = por_puntos[ i ][ 1 ]
                print(usuario , puntaje)
        elif x == 1:
                usuario = por_puntos[ i ][ 0 ]
                puntaje = por_puntos[ i ][ 1 ]
                print(usuario , puntaje)
        print("\n")
#-------------------------------------------------------------------------
    elif opcion==9:
        id = int( input( "Ingrese el ID del usuario: " ) )
        puntos_a_sumar = int( input( "Ingrese la cantidad de puntos a sumar: " ) )
        usuarios_db.agregar_puntos( id , puntos_a_sumar )
        print( "Se han agregado " , puntos_a_sumar , " puntos al usuario ID: " , id )
        print("\n")
#-------------------------------------------------------------------------
