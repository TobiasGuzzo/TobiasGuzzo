#de tobias guzzo
import modulo_1 as m1
import modulo_2 as m2
import modulo_3 as m3
import modulo_4 as m4

def mostrar_menu():
    print("\nEcho por tobias guzzo de 4°1")
    print("\nselecciona el numero de actividad")
    print("-----------------------------------")
    print("1 = modulo_1")
    print("este modulo es de if y else ")
    print("-----------------------------------")
    print("2 = modulo_2")
    print("son ejercicios con for y while ")
    print("-----------------------------------")
    print("3 = modulo_3")
    print("ejercicios basados en fisica ")
    print("-----------------------------------")
    print("4 = modulo_4")
    print("ejercicios de finansas")
    print("-----------------------------------")
    print("0 = salir")

opcion = 88

while (opcion!=0):
    mostrar_menu()
    opcion = int(input("ingresar el numero del modulo: "))
    if (opcion==1):
        print("se a seleccionado el modulo 1")
        print("")
        print("------------------------------------------")
        print("ejercicio 1 indicador de edades")
        print("-----------------------------------------")
        print("ejercicio 2 indicador de menor o mayor")
        print("-----------------------------------------")
        print("ejercicio 3 partido de footbal entre dos equipos")
        print("-----------------------------------------")
        print("ejercicio 4 contador de menor a mayor ")
        print("-----------------------------------------")
        print("ejercicio 5 contador de par e inpar ")
        print("-----------------------------------------")
        print("ejercicio 6 localizador de punto cartesiano")
        print("-----------------------------------------")
        print("ejercicio 7 localizacion de un cuadrado")
        print("-----------------------------------------")
        print("ejercicio 8 localizacion de un punto dentro de un cuadrado ")
        print("-----------------------------------------")
        print("ejercicio 9 localizador de un punto dentro de un circulo ")
        print("-----------------------------------------")
        ejercicio = int(input("ingrese el numero del ejercicio que desea entrar: "))
        if(ejercicio==1):
            m1.ejercicio_1()
        elif(ejercicio==2):
            m1.ejercicio_2()
        elif(ejercicio==3):
            m1.ejercicio_3()
        elif(ejercicio==4):
            m1.ejercicio_4()
        elif(ejercicio==5):
            m1.ejercicio_5()
        elif(ejercicio==6):
            m1.ejercicio_6()
        elif(ejercicio==7):
            m1.ejercicio_7()
        elif(ejercicio==8):
            m1.ejercicio_8()
        elif(ejercicio==9):
            m1.ejercicio_9()
        else:
            print("\neste ejercicios es este modulo no esta disponible")
    if(opcion==2):
        print("se eligio el modulo_2")
        print("")
        print("------------------------------------------")
        print("ejercicio 1 agregado de un numero + la suma de sus anteriores")
        print("-----------------------------------------")
        print("ejercicio 2 sumador de numero impares")
        print("-----------------------------------------")
        print("ejercicio 3 muestra los numero que existen desde el 1 al 1000")
        print("-----------------------------------------")
        print("ejercicio 4 programa de numero divisibles y no ")
        print("-----------------------------------------")
        print("ejercicio 5 programa número entero mayor o igual a uno y menor o igual a 12 ")
        print("-----------------------------------------")
        print("ejercicio 6 indicador de numero si es o no primo ")
        print("-----------------------------------------")
        print("ejercicio 7 programa que muestra la cantidad de numeros que entran en una variable")
        print("-----------------------------------------")
        print("ejercicio 8 cantidad de gramos de trigo que muestra en un tablero ")
        print("-----------------------------------------")
        ejercicio = int(input("ingrese el numero del ejercicio: "))
        if(ejercicio==1):
            m2.ejercicio_1()
        elif(ejercicio==2):
            m2.ejercicio_2()
        elif(ejercicio==3):
            m2.ejercicio_3()
        elif(ejercicio==4):
            m2.ejercicio_4()
        elif(ejercicio==5):
            m2.ejercicio_5()
        elif(ejercicio==6):
            m2.ejercicio_6()
        elif(ejercicio==7):
            m2.ejercicio_7()
        elif(ejercicio==8):
            m2.ejercicio_8()
        else:
            print("\neste ejercicios es este modulo no esta disponible")
    if(opcion==3):
        print("se eligio el modulo_3")
        print("")
        print("------------------------------------------")
        print("ejercicio 1 lanzamiento de un objeto segun niuvel del mar y velocidad")
        print("-----------------------------------------")
        print("ejercicio 2 lazamiento de objeto segun hasta su altura maxima ")
        print("-----------------------------------------")
        print("ejercicio 3 lanzamiento de un objeto hasta que vuelva a su punto de salida ")
        print("-----------------------------------------")
        print("ejercicio 4 lanzamiento de un ogjeto segun su angulo y cuanto tarda en caer ")
        print("-----------------------------------------")
        ejercicio = int(input("ingrese el numero del ejercicio: "))
        if(ejercicio==1):
            m3.ejercicio_1()
        elif(ejercicio==2):
            m3.ejercicio_2()
        elif(ejercicio==3):
            m3.ejercicio_3()
        elif(ejercicio==4):
            m3.ejercicio_4()
        else:
            print("\neste ejercicios es este modulo no esta disponible")
    if(opcion==4):
        print("se eligio el modulo_3")
        print("")
        print("------------------------------------------")
        print("ejercicio 1 monto de una compra de un producto")
        print("-----------------------------------------")
        print("ejercicio 2 programa que calcular el monto total de una compra de distintos productos")
        print("-----------------------------------------")
        print("ejercicio 3 programa que calcule el dinero que se obtiene por un plazo fijo")
        print("-----------------------------------------")
        ejercicio = int(input("ingrese el numero del ejercicio: "))
        if(ejercicio==1):
            m4.ejercicio_1()
        elif(ejercicio==2):
            m4.ejercicio_2()
        elif(ejercicio==3):
            m4.ejercicio_3()
        else:
            print("\neste ejercicios es este modulo no esta disponible")
    else:
        print("\neste modulo no esta permitido, vuelva a intentarlo")
