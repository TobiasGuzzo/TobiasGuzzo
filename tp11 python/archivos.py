import cripto as c
import os.path

#TODO: implementar
def encriptar_archivo(nombre_archivo_original, nombre_archivo_destino, clave):
    if (os.path.isfile(nombre_archivo_original)):
        print("el archivo existe")
    archivo_inicial = open(nombre_archivo_original,"r")
    destino_archivo = open(nombre_archivo_destino,"w")
    linea = archivo_inicial.readline()
    while linea != '':
        linea.rstrip('\n')
        linea_encriptada = c.encriptar(linea,clave)
        destino_archivo.write(linea_encriptada + "\n")
        linea = archivo_inicial.readline()
    archivo_inicial.close()
    destino_archivo.close()
#TODO: implementar
def desencriptar_archivo(nombre_archivo_original, nombre_archivo_destino, clave):
    if (os.path.isfile(nombre_archivo_original)):
        print("el archivo existe")
    archivo_inicial = open(nombre_archivo_original,"r")
    destino_archivo = open(nombre_archivo_destino,"w")
    linea = archivo_inicial.readline()
    while linea != "":
        linea.rstrip('\n')
        linea_encriptada = c.desencriptar(linea,clave)
        destino_archivo.write(linea_encriptada + "\n")
        linea = archivo_inicial.readline()
    archivo_inicial.close()
    destino_archivo.close()
