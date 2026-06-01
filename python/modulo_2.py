#de tobias guzzo
import math
import sys
def ejercicio_1():
    """
     Hacer un programa que solicite un número N y luego muestre el valor de la suma de los
números que van del 1 al N. (1 + 2 + 3 + 4 + 5 … N)
    """
    print("\nEjercicio 2.1")
    a = int(input("\nIngrese un numero: "))
    d = 0
    for i in range(N+1):
        d = d + i
    print ("\nLa suma de los numeros del 1 al", a , "son" , d)

def ejercicio_2():
    """
    Hacer un programa similar al anterior pero que sume los números impares 1, 3, 5, 7, 9 … N.
    """
    print("\nEjercicio 2.2")
    a = int(input("\nIngrese un numero: "))
    s = 0
    for i in list(range(1, a+1 ,2)):
        s = s + i
    print ("\nLa suma de los numeros del 1 al", a , "son" , s)

def ejercicio_3():
    """
    Hacer un programa que muestre los números pares que existen entre 1 y 1000. (Usar el
operador módulo %)
    """
    print("\nEjercicio 2.3")
    print("\n Los pares que existen entre 1 y 1000 son:")
    for i in range(1,1001):
        if i % 2 == 0:
            print(i)

def ejercicio_4():
    """
     Hacer un programa que solicite un número al usuario que denominaremos divisor y luego de
forma iterativa solicite un número al usuario e indique si dicho número es divisible por el que se
ingreso inicialmente. El programa termina cuando el usuario ingresa cero.

    """
    print("\nEjercicio 2.4")

    divisor = int(input("\nIndique el divisor: "))
    dividendo = int(input("Indique el numero a dividir: "))
    if divisor == 0:
        print()
        quit()
    if dividendo % divisor == 0:
        print("\nEl numero es divisible por" , divisor)
    else:
        print("\nEl numero no es divisible por" , divisor)

def ejercicio_5():
    """
     Hacer un programa que solicite un número entero mayor o igual a uno y menor o igual a 12 y
luego muestre la tabla de multiplicar de dicho número. (La tabla de multiplicar va del 1 al 10)
    """
    print("\nEjercicio 2.5")
    n = int(input("\nIndique un numero <= 1 y >= 12: "))
    if n >= 1 and n <= 12:
        print ("La tabla de multiplicar de " , n , "es la siguiente")
        for i in range(11):
            print (n , "*" , i , "=" , n * i)

    else:
        print("\nEl numero es incorrecto")

def ejercicio_6():
    """
    Hacer un programa que solicite un número N al usuario y luego indique si el número es o no
es primo (Un número es primo si solo es divisible por sí mismo y por uno. Debe recorrer todos los
números desde 2 a N-1 y comprobar si la división deja resto. Utilice el operador % módulo para
chequear el resto de las divisiones).
    """
    print("\nEjercicio 2.6")
    n = int(input("\nIndique un numero: "))
    print("")
    primo = True
    for i in range(2, n):
        if (n % i == 0):
            primo = False
    if (primo):
        print ("\nEl numero" , n , "es un numero primo")
    else:
        print ("\nEl numero" , n , "es un numero compuesto")
    print("")

def ejercicio_7():
    """
     Hacer un programa que imprima todos los números primos que caben en una variable
integer. (Debe hacer un ciclo de 1 al máximo valor que cabe en la variable integer y chequear para
cada número si es primo y en tal caso mostrarlo por pantalla)
    """
    print("\nEjercicio 2.7")
    print("\nTodos los numeros primos de Integer:")
    for N in range( 1 , sys.maxsize ) :
        di = True
        n = 2
        while (n < N and di == True) :
            if((N % n) == 0):
                di = False
                n += 1
        if(di):
            print(N)

def ejercicio_8():
    """
    Hacer un programa que permita resolver el problema del tablero de ajedrez y los granos de
trigo para tableros cuadrados de distinto tamaño. El problema consiste en determinar cuántos
granos de trigo habría que poner en el tablero si se pone un grano en el primer casillero, dos en el
segundo, luego cuatro, ocho y así sucesivamente doblando la cantidad en cada paso. El tablero de
ajedrez tiene 8 x 8. El programa debe preguntar la cantidad de casilleros que hay en cada lado del
tablero y luego mostrar el resultado.
    """
    print("\nEjercicio 2.8")
    casilleros = int(input("\nIngrese la cantidad de casilleros que hay en uno de los lados del tablero: "))
    casilleros2 = int (input("\ningrese la cantidad de casilleros del otro lado"))
    s = casilleros2 * casilleros
    d = 2
    suma = 1
    for i in range(1,s+1):
        d += d
    suma += d
    print(suma)
