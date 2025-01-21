#de tobias guzzo
import math
def ejercicio_1():
    """
    Hacer un programa que solicite la edad al usuario y luego indique si es mayor de edad
(consideramos mayor de edad quien tiene al menos 18 años).
    """
    print("\nEjercicio 1.1")
    n = int(input("\nIngrese Su edad: "))
    if (n >= 18):
        print("\nUsted es mayor de edad")
    else:
        print("\nUsted es menor de edad")

def ejercicio_2():
    """
    Hacer un programa que solicite dos números al usuario y luego indique cual es el menor y
cual el mayor o si son iguales.
    """
    print("\nEjercicio 1.2")
    n1 = int(input("\nIngrese un numero: "))
    n2 = int(input("\nIngrese otro numero: "))
    print()
    if n1 > n2:
        print(n1 , "Es mayor que" , n2)
    elif n2 > n1:
        print(n2 , "Es mayor que" , n1)
    else:
        print(n1 , "Es igual que" , n2)

def ejercicio_3():
    """
    Hacer un programa que solicite al usuario los goles que convirtió el equipo A y los goles que
convirtió el equipo B y luego indique el ganador o si hubo empate.
    """
    print("\nEjercicio 1.3")
    n1 = int(input("\nel numero de goles del equipo 1: "))
    n2 = int(input("el numero de goles del equipo 2: "))
    if n1 > n2:
        print("\ngana el quipo 1")
    elif n2 > n1:
        print("\ngana el quipo 2")
    else:
        print("\nes un empate")

def ejercicio_4():
    """
     Hacer un programa que solicite tres números al usuario y luego los muestre de menor a
mayor.

    """
    print("\nEjercicio 1.4")

    a = int(input("\nIngrese un numero: "))
    b = int(input("\nIngrese otro numero: "))
    c = int(input("\nIngrese otro numero mas: "))
    print()

    if(a > b and a > c):
        if(b > c):
            print(c, b, a)
        else:
            print(b, c, a)
    elif(b > a and b > c):
        if(a > c):
            print(c, a, b)
        else:
            print(a, c, b)
    elif(c > a and c > b):
        if(a > b):
            print(b, a, c)
        else:
            print(a, b, c)


    print("asi son de menor a mayor:")
    print(n1 , ";" , n2 , ";" , n3)

def ejercicio_5():
    """
    Hacer un programa que solicite un número al usuario y luego indique si el número es par o
impar. (Usar el operador % modulo para determinar si la división por 2 deja resto)

    """
    print("\nEjercicio 1.5")

    n = int(input("\nIngrese un numero: "))

    print()

    if (n % 2):
        print("El numero " , n , "es impar")
    else:
        print("El numero " , n , " es par")

def ejercicio_6():
    """
     Hacer un programa que solicite el valor de un punto en el plano cartesiano (el valor de x y el
valor de y) y luego indique en que cuadrante se encuentra el punto.
    """
    print("\nEjercicio 1.6")

    cx = float(input("\nIngrese el eje X: "))
    cy = float(input("Ingrese el eje Y: "))
    print()

    if cx > 0 and cy > 0:
        print("(" , cx , ";" , cy , ") se encuentra en el eje X positivo y el eje Y positivo")
    elif cx < 0 and cy > 0:
        print("(" , cx , ";" , cy , ") se encuentra en el eje X negativo y el eje Y positivo")
    elif cx > 0 and cy < 0:
        print("(" , cx , ";" , cy , ") se encuentra en el eje X positivo y el eje Y negativo")
    elif cx < 0 and cy < 0:
        print("(" , cx , ";" , cy , ") se encuentra en el eje X negativo y el eje Y negativo")
    elif cx == 0 and cy == 0:
        print("(" , cx , ";" , cy , ") se encuentra en el centro de coordenadas")

def ejercicio_7():
    """
    Suponemos que existe un cuadrado en el plano cartesiano cuyos lados tienen dos unidades
de distancia, cuyo vértice inferior izquierdo coincide con el centro de coordenadas del plano y el
lado inferior coincide con el eje x. Hacer un programa que solicite al usuario las coordenadas de un
punto e indicar si el punto está dentro o fuera del cuadrado. (Determine qué rango de valores
deben tener la abscisa y la ordenada del punto para estar dentro del cuadrado)
    """
    print("\nEjercicio 1.7")
    cuadrado = 5
    cordenada_x = float(input("\nIngrese una coordenada en el eje X: "))
    cordenada_y = float(input("Ingrese una coordenada en el eje Y: "))
    print()
    r = False
    if (cordenada_x >= 0 and cuadrado <= 2):
        if (cordenada_y >= 0 and cuadrado <= 2):
            r = True
    if (r == True):
        print("El punto de interseccion está dentro del cuadrado")
    else:
        print("El punto de interseccion está fuera del cuadrado")

def ejercicio_8():
    """
    Hacer un programa que solicite la longitud del lado y la posición del vértice inferior izquierdo
de un cuadrado que se encuentra en el plano cartesiano con el lado inferior paralelo al eje x.
Luego solicitar al usuario las coordenadas de un punto e indicar si dicho punto se encuentra
dentro o fuera del cuadrado.
    """
    print("\nEjercicio 1.8")
    l = int(input("ingresar longitud del lado"))

    print("poner coordenadas del vértice inferior izquierdo en el eje x:")
    x1 = float(input())
    print("poner coordenadas del vértice inferior izquierdo en el eje y:")
    y1 = float(input())
    print("Coordenadas de un punto en el eje Y:")
    y = float(input())
    print("Coordenadas de un punto en el eje X:")
    x = float(input())

    x2 = x1 + l
    y2 = y1 + l

    if(x > x1 and x < x2 and y > y1 and y < y2):
        print("Las coordenadas estan dentro del cuadrado")
    else:
        print("Las coordenadas estan fuera del cuadrado")


def ejercicio_9():
    """
    Hacer un programa que solicite la longitud del lado y la posición del vértice inferior izquierdo
de un cuadrado que se encuentra en el plano cartesiano con el lado inferior paralelo al eje x.
Luego solicitar al usuario las coordenadas de un punto e indicar si dicho punto se encuentra
dentro o fuera del cuadrado.
    """
    print("\nEjercicio 1.9")

    radio = float(input("ingrese el radio de un circulo: "))
    cirx = float(input("ingrese el eje X de su punto central: "))
    ciry = float(input("ingrese eje Y de su punto sentral: "))
    x = float(input("\nIngrese el eje X: "))
    y = float(input("Ingrese el eje Y: "))
    g = math.sqrt(( cirx - x ) ** 2 + ( ciry - y ) ** 2)
    if g <= radio:
        print( "El punto esta dentro del circulo." )
    else:
        print( "El punto esta fuera del circulo." )
