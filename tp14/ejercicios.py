import time
import random
import os
import numpy as np
#-------------------------------------------------------
def varlist(): #esto lo dejo aca por si es necesario usar , esto es parte de mi grupo del tp 5
    lista = []
    n = int(input("Cuantos numeros se desea agregar a la lista: "))

    for i in range(0,n):
        A = int(input("Ingrece un numero: "))
        lista.append(A)
    print("---------------------------")
    return(lista, n)
#-------------------------------------------------------
def ejercicio_1():
    """
     Desarrolle un script que solicite diez números al usuario y
     los almacene en un array.
     Posteriormente muestre los diez números uno debajo del otro.
    """
    array =  np.array([])
    for i in range(10):
        numero = float(input("ingrese 10 numeros:"))
        array = np.append(array,numero)
    for i in range(0,9):
        print(array[i])
    input("presione una tecla para continuar")
#-------------------------------------------------------
def ejercicio_2():
    """
    Desarrolle un script que primero solicite al usuario la cantidad de números que quiere ingresar
    luego los números uno a uno y los almacene en un array.
    Posteriormente sume todos los números e indique el resultado.
    """
    cantidad_de_numeros= int(input("\ncuantos numeros quiere escribir?: "))
    total = 0
    array = np.array([])
    print("ingrese", cantidad_de_numeros ,"numeros" )
    for i in range(cantidad_de_numeros):
        numeros = float(input())
        total = numeros + total
        array = np.append(array,numeros)
    print("el resultado es:", total)
    input("presione una tecla para continuar")
#-------------------------------------------------------
def ejercicio_3():
    """
     Desarrolle un script que solicite la cantidad de números que se van a ingresar
     luego los números y los almacene en un array.
     Posteriormente el script debe determinar el menor
     el mayor y el promedio y  mostrarlos por pantalla.
    """
    menor = float(10 ** 80)
    mayor = float(-10 ** 80)
    cantidad_de_numeros = int(input("\ncuantos numeros quiere escribir?: "))
    array = np.array([])
    total = 0
    print("ingrese",cantidad_de_numeros ,"numeros")
    for i in range(cantidad_de_numeros):
        numeros = float(input())
        array = np.append(array, numeros)
        total = numeros + total
    for i in range(cantidad_de_numeros):
        if( menor > array[i]):
            menor = array[i]
    for i in range(cantidad_de_numeros):
        if( mayor < array[ i ] ):
            mayor = array[ i ]
    promedio = total / cantidad_de_numeros
    print( "El menor es " , menor )
    print( "El mayor es " , mayor )
    print( "El promedio es " , promedio )
    input("presione una tecla para continuar")
#-------------------------------------------------------
def ejercicio_4():
    """
    Desarrolle un script que solicite la cantidad de números que se van a ingresar
    luego los números y los almacene en un array.
    Posteriormente el script debe solicitar de forma iterativa un número para
    determinar si se encuentra en el array e indicarlo al usuario.
     El programa termina cuando se ingresa un cero.
    """
    #-------------------------------------------------------
    cantidad_de_numeros = float(input("\ncuantos numeros desea escribir?: "))
    print("Ingrese " , cantidad_de_numeros , " numeros:")
    total = 0
    array = np.array([], dtype=int)
    for i in range(size_arr):
        numeros = int(input())
        array = np.append(array, numeros)
    print(array)
    opcion = 1
    while (opcion !=0):
        numero = float(input("ingrese un numero para saber si esta en la lista: "))
        for i in range(0,cantidad_de_numeros):
            if numero == array[i]:
                total = total + 1
        if total >= 1:
            print ("el numero esta en la lista")
        else:
            print ("el numero no esta en la lista")
        total = 0
        opcion = str(input("Ingrese 1 para volver a buscar un numero o ingrese 0 para terminar "))
        print("ingrese 1 si quiere volver")
        print("ingrese 0 si quiete terminar")
        input("presione una tecla para continuar")
#-------------------------------------------------------
def ejercicio_5():
    """
    Desarrolle un script similar al anterior pero que además de indicar
     si el número se encuentra en el array también indique la posición
     en la que este se encuentra.
    """
    array =np.array([])
    #total es el contador
    total = 0
    cantidad_de_numeros = float(input("cuantos numeros desea ingresar?:"))
    print("ingrese", cantidad_de_numeros, "numeros")
    for i in range(cantidad_de_numeros):
        numeros = float(input())
        array = np.append(array,numeros)
    print(array)
    opcion = 1
    while(opcion != 0):
        origen = float(input("debe ingresar un numero para saber si esta en la lista"))
        pos = 0
        total = 0
        for i in range(inicio):
            if origen == array[i]:
                total = total + 1
                pos = i
                break
        if total >= 1:
            print("esta en la lista en:", pos + 1)
        else:
            print("no esta en la lista")
        opcion = str("ingrese 1 para volvor a intentar o ingrese 0 para salir ")
        print("-1 para volver a intentar")
        print("-0 para salir")
        input("presione una tecla para continuar")
    #-------------------------------------------------------
def ejercicio_6():
    """
     Desarrolle un script que permita cargar en un array una cantidad de números
     indicada por el usuario y luego los ordene usando el método de burbuja.
      Luego muestre los números ordenados.
    """
    cantidad_de_numeros = int(input("\ncuantos numeros desea ingresar?:"))
    array = np.array([])
    for i in range(cantidad_de_numeros):
        array =np.append(array,random.radint(-2147483647,2147483647))#esto es lo que aguanta el int
        metodoburbuja(array)
        print(array)
        input("presione una tecla para continuar")
#-----------------------------------------------------------------------------
def ordenarPorSeleccion(array):
    for i in range(len(array)-1):
        minimo = i
        for j in range(i+1, len(array)):
            if array[j] < array[minimo]:
                minimo = j
        temp = array[minimo]
        array[minimo]=array[i]
        array[i]= temp
    return array

#-------------------------------------------------------
def ejercicio_7():
    """
    Desarrolle un script que permita cargar en un array una cantidad de números
    indicada por el usuario y luego los ordene usando el método de selección.
     Luego muestre los números ordenados.
    """
    inicio = int(input("\ncuantos numeros desea ingresar "))
    array = np.array([])
    for i in range(inicio):
        array = np.append(array, random.randint(-2147483647 , 2147483647))
    ordenarPorSeleccion(array)
    print(array)
    input("presione una tecla para continuar")
#---------------------------------------------------------
def metodo_de_burbuja(arr):
    for i in range(len(arr)-1, 0, -1):
        for j in range(i):
            if(arr[j]>arr[j+1]):
                aux = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = aux
    return(arr)
#-------------------------------------------------------
def generadorrandomarray(i):
    np.random.seed(i)
    return np.random.randint(10000,size = 1000)
#-------------------------------------------------------
def ejercicio_8():
    """
     Haga un programa que permita comprobar cuál de los algoritmos de ordenamiento nombrados anteriormente es más eficiente.
     Para esto es necesario medir el tiempo de ejecución de los algoritmos y compararlos.
     Es necesario medir muchas veces el tiempo que tarda un algoritmo en ejecutarse y obtener el promedio.
    """


    tiempodeinicioconburbuja = 0
    tiempofinalconburbuja = 0
    timpoinicialconseleccion = 0
    tiempofinalconseleccion = 0

    total_burbuja = 0
    total_seleccion = 0
    print("aguarde mientras se ejecuta el codigo")
    for i in range(1000):
        array = generadorrandomarray(i)
        tiempodeinicioconburbuja = time.time()
        metodo_de_burbuja(array)
        tiempofinalconburbuja = time.time()
        #print(array) # por si quiero ver el array
        burbuja = tiempofinalconburbuja - tiempodeinicioconburbuja
        total_burbuja += burbuja
    #--------------------------------------------------------------
        array = generadorrandomarray(i)
        timpoinicialconseleccion = time.time()
        ordenarPorSeleccion(array)
        tiempofinalconseleccion = time.time()
        #print(array) # por si quiero ver el array
        seleccion = tiempofinalconseleccion - timpoinicialconseleccion
        total_seleccion += seleccion
    #--------------------------------------------------------------
    total_seleccion = total_seleccion / 1000
    total_burbuja = total_burbuja / 1000

    print("el metodo burbuja tardo" , total_burbuja , "en promedio")
    print("el metodo de seleccion tardo" , total_seleccion, "en promedio")
    input("presione una tecla para continuar")
