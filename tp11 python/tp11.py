#
# Trabajo Practico Numero 11
#
# Materia: Algoritmos y Estructura de Datos
#
# Alumno: Allan Montero
#
#
# TODO: MEJORAR ESTE MODULO
import archivos

def mostrar_menu():
    print("1) encriptar un archivo")
    print("2) desencriptar un archivo")
    print("3) salir del programa\n")


opcion=0

while opcion!=3:
    mostrar_menu()

    opcion = int(input("ingrese su opcion: "))

    if opcion== 1:
        nombre_archivo_original = input("Ingrese el nombre del archivo a encriptar: ")
        nombre_archivo_destino = input("Ingrese el nombre del archivo destino: ")
        clave = int(input("Ingrese la clave: "))
        archivos.encriptar_archivo(nombre_archivo_original, nombre_archivo_destino, clave)
    elif opcion == 2:
        nombre_archivo_original = input("Ingrese el nombre del archivo a desencriptar: ")
        nombre_archivo_destino = input("Ingrese el nombre del archivo destino: ")
        clave = int(input("Ingrese la clave: "))
        archivos.desencriptar_archivo(nombre_archivo_original, nombre_archivo_destino, clave)
    elif opcion !=3:
        print(f"La opcion {opcion} no es valida")


print("Fin del programa. Gracias por utilizar los servicios de nuestra empresa.")
