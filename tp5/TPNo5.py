import time
import random
import os

N = int(1)
def metodoburbuja(lista):
    for i in range(len(lista)-1, 0, -1):
        for j in range(i):
            if(lista[j]>lista[j+1]):
                aux = lista[j]
                lista[j] = lista[j+1]
                lista[j+1] = aux
    return(lista)

def metodoseleccion(lista):
    for i in range(len(lista)-1,0,-1):
        mayor=0
        for j in range(1,i+1):
            if lista[j]>lista[mayor]:
                mayor = j
        aux = lista[i]
        lista[i] = lista[mayor]
        lista[mayor] = aux
    return(lista)

def metodoinsercion(lista):
    for i in range(len(lista)):
        for j in range(i,0,-1):
            if(lista[j-1] > lista[j]):
                aux=lista[j]
                lista[j]=lista[j-1]
                lista[j-1]=aux
    return(lista)

def varlist():
    lista = []
    n = int(input("Cuantos numeros se desea agregar a la lista: "))

    for i in range(0,n):
        A = int(input("Ingrece un numero: "))
        lista.append(A)
    print("---------------------------")
    return(lista, n)

def limpiar():
    os.system("cls")

def fin():
    print("------------------------------------")
    input("Para volver al Menu presionar enter")
    limpiar()
    print("")
    limpiar()
def ej1():
    """
    7.1) Desarrolle un script que solicite diez números al usuario y los almacene en una Lista.
    Posteriormente muestre los diez números uno debajo del otro.
    """
    lista = []
    for i in range( 0 , 10 ):
        A = int( input( "Ingrece un numero: " ) )
        lista.append( A )
    print("---------------------------")
    for i in range( 0 , 10 ):
        print( lista[ i ] )
    fin()

def ej2():
    """
    7.2) Desarrolle un script que primero solicite al usuario la cantidad de números que quiere
    ingresar, luego los números uno a uno y los almacene en una Lista. Posteriormente sume
    todos los números e indique el resultado.
    """
    suma = int()
    lista , n = varlist()
    for i in range( 0 , n ):
        suma = suma + lista[ i ]
    print( " La suma de todos los numeros es " , suma )
    fin()

def ej3():
    """
    7.3) Desarrolle un script que solicite la cantidad de números que se van a ingresar, luego los
    números y los almacene en una Lista. Posteriormente el script debe determinar el menor, el
    mayor y el promedio y mostrarlos por pantalla.
    """
    lista , n = varlist()
    promedio = float()
    menor = float( 10 ** 80)
    mayor = float( -10 ** 80 )
    for i in range( 0 , n ):
        if( menor > lista[ i ] ):
            menor = lista[ i ]
    for i in range( 0 , n ):
        if( mayor < lista[ i ] ):
            mayor = lista[ i ]
    for i in range( 0 , n ):
        promedio = promedio + lista[ i ]
    promedio = promedio / n
    print( "El menor es " , menor )
    print( "El mayor es " , mayor )
    print( "El promedio es " , promedio )
    fin()

def ej4():
    """
    7.4) Desarrolle un script que solicite la cantidad de números que se van a ingresar, luego los
    números y los almacene en una Lista. Posteriormente el script debe solicitar de forma
    iterativa un número para determinar si se encuentra en la lista e indicarlo al usuario. El
    programa termina cuando se ingresa un cero.
    """
    lista , n = varlist()
    Var = int( 0 )
    n1 = float( 1 )
    while( n1 != 0 ):
        n1 = float( input( "Ingresar un numero para determinar si esta en la lista: ") )
        for i in range( 0 , n ):
            if( n1 == lista[ i ] ):
                Var = Var + 1
        if( Var == 1 ):
            print( "El numero " , n1, " esta en la lista" )
        else:
            print( "El numero " , n1 , " no se encuentra en la lista" )
        Var = 0
    fin()

def ej5():
    """
    7.5) Desarrolle un script similar al anterior pero que además de indicar si el número se
    encuentra en la lista también indique la posición en la que este se encuentra.

    """
    lista , n = varlist()
    Var = int( 0 )
    n1 = float( 1 )
    posicion = int()

    while( n1 != 0 ):
        n1 = float(input("Ingresar un numero para determinar si esta en la lista: "))
        for i in range( 0 , n ):
            if( n1 == lista[ i ] ):
                Var = Var + 1
                posicion = i
        if( Var == 1 ):
            print( "El numero " , n1 , " esta en la lista" )
        else:
            print( "El numero " , n1 , " no se encuentra en la lista" )
        print( "El numero se encuentra en la posición" , posicion )
        Var = 0
    fin()

def ej6():
    """
    7.6) Desarrolle un script que permita cargar una cantidad de números indicada por el usuario y
    luego los ordene usando el método de burbuja. Luego muestre los números ordenados.

    """
    lista, n = varlist()
    lista = metodoburbuja(lista)
    print( "Numeros de la lista ordenados con el metodo burbuja: ", lista)
    fin()

def ej7():
    """
    7.7) Desarrolle un script que permita cargar una cantidad de números indicada por el usuario y
    luego los ordene usando el método de selección. Luego muestre los números ordenados.
    """
    lista, n = varlist()
    lista = metodoseleccion(lista)

    print("Numeros de la lista ordenados con el metodo selección: ", lista)
    fin()

def ej8():
    """
    7.8) Desarrolle un script que permita cargar una cantidad de números indicada por el usuario y
    luego los ordene usando el método de inserción. Luego muestre los números ordenados.
    """
    lista, n = varlist()
    lista = metodoinsercion(lista)
    print("Numeros de la lista ordenados con el metodo inserción: ", lista)
    fin()

def ej9():
    """
    7.9) Haga un programa que permita comprobar cuál de los algoritmos de ordenamiento
nombrados anteriormente es más eficiente. Para esto es necesario medir el tiempo de
ejecución de los algoritmos y compararlos. Es necesario medir muchas veces el tiempo que
tarda un algoritmo en ejecutarse y obtener el promedio.
Por lo tanto lo que el programa debe hacer es repetir miles de veces para cada tipo de
ordenamiento un algoritmo que en primer lugar asigne valores al azar a una lista números
enteros, en segundo lugar ordene la lista midiendo el tiempo y acumule dicho valor. Antes y
después de ordenar la lista debe consultar el tiempo al sistema y calcular la diferencia, esa
diferencia de tiempo es el tiempo que demora el algoritmo de ordenamiento en ejecutarse. El
programa debe sumar los tiempos y luego obtener el promedio.
    """
    TA = float()
    TMB = float()
    TMS = float()
    TMI = float()
    TTMB = float()
    TTMS = float()
    TTMI = float()

    lista = [0]
    for i in range(0, 999):
        for i in range(0,999):
            lista.append(random.randint(1,10000))

        TA = time.time()
        metodoburbuja(lista)
        TMB = time.time() - TA
        TTMB = TTMB + TMB
        lista = [0]

        for i in range(0,999):
            lista.append(random.randint(1,10000))
        TA = time.time()
        metodoseleccion(lista)
        TMS = time.time() - TA
        TTMS = TTMS + TMS
        lista = [0]
        for i in range(0,999):
            lista.append(random.randint(1,10000))

        TA = time.time()
        metodoinsercion(lista)
        TMI = time.time() - TA
        TTMI = TTMI + TMI

    TTMB = TTMB / 1000
    TTMS = TTMS / 1000
    TTMI = TTMI / 1000

    if(TTMB < TTMS and TTMB < TTMI):
        print("El Metodo burbuja es el mas eficiente en este caso")
    elif(TTMS < TTMI):
        print("El Metodo seleccion es el mas eficiente en este caso")
    else:
        print("El Metodo inserción es el mas eficiente en este caso")

    print("timpo que tardo el Metodo burbuja: ", TTMB)
    print("timpo que tardo el Metodo selección: ", TTMS)
    print("timpo que tardo el Metodo inserción: ", TTMI)

def menu():
    limpiar()
    print("-------------------")
    print("-      Listas     -")
    print("-------------------")
    print("- 0 - Salir       -")
    for i in range(1, 10):
        print("-", i, "- Ejecicio ", i, "-")
    print("-------------------")
    print("")

while(N != 0):

    menu()

    N = int(input("Ingrese el numero: "))
    num_ej = int(N)
    if(N == 0):
        limpiar()
        print("---------------")
        print("- Cerrando... -")
        print("---------------")
        time.sleep(1)
        limpiar()
    elif(N >= 10 or N < 0):
        limpiar()
        print("------------------------")
        print("- Modulo no encontrado -")
        print("------------------------")
        time.sleep(1)
        limpiar()
    else:
        limpiar()
        print("-------------------")
        print("   Ejercicio ", num_ej)
        print("-------------------")
        print("")
        if(N == 1):
            ej1()
        elif(N == 2):
            ej2()
        elif(N == 3):
            ej3()
        elif(N == 4):
            ej4()
        elif(N == 5):
            ej5()
        elif(N == 6):
            ej6()
        elif(N == 7):
            ej7()
        elif(N == 8):
            ej8()
        elif(N == 9):
            ej9()
        fin()
        limpiar()
