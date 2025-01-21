#
# Trabajo Practico Numero 10
#
# Materia: Algoritmos y Estructura de Datos
#
# Alumno: Tobias guzzo
import cripto
#TODO: Desarrollar un menu que iterativamente le permita al usuario elegir
# 1) encriptar un mensaje
# 2) desencriptar un mensaje
# 3) salir del programa
variable = 0
def mostrar_menu():
    print("que quiere realizar?")
    print("1 encriptar un mensaje")
    print("2 desencriptar mensaje")
    print("3 salir")

while (variable != 4):
    mostrar_menu()
    opcion = int(input("ingrese su opcion:"))

    if opcion == 1:
        print("\nincriptacion de un texto")
        mensaje = input("ingrese un texto a encriptar:")
        clave = int(input("ingrese la clave:"))
        encriptado = cripto.encriptar(mensaje,clave)
        print("El mensaje enciptado es:",encriptado)

    elif opcion == 2:
        print("\ndesincriptacion de un texto")
        texto = input("ingrese para desencriptar:")
        clave = int(input("ingrese la clave:"))
        desencriptar = cripto.desencriptar(texto, clave)
        print("el txto encriptado es:" , desencriptar)
    elif opcion == 3:
        print("vuelva pronto")
        variable = 4
