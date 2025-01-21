#de tobias guzzo
import math
g = 9.80665
def ejercicio_1():
    """
 Considerando que la aceleración de la gravedad en la tierra es aproximadamente
9,80665 m/s² haga un programa que pregunte al usuario desde qué altura (en kilómetros) se lanza
al vacío con velocidad inicial cero y permita calcular cuánto tiempo (en segundos) tarda en llegar al
nivel del mar y con qué velocidad.
    """
    print("\nEjercicio 3.1")

    a = float(input("Ingrese la altura en la que se lanza un objeto (En kilometros): "))

    a = a * 1000


    t = math.sqrt(a / (0.5 * g))
    vf = g * t

    print("\nTarda" , t , "Segundos en caer al nivel del mar desde una altura de" , (a / 1000) , "km \nCon una velocidad de" , vf , "m/s")

def ejercicio_2():
    """
     Hacer un programa que permita ingresar la velocidad con que se lanza un objeto hacia arriba
y determine cuánto tiempo tarda el objeto en alcanzar la altura máxima antes de empezar a caer.
(La altura máxima se alcanza cuando la velocidad llega a cero)
    """
    print("\nEjercicio 3.2")
    objeto = float(input("Ingrese la velocidad con la que se lanza el objeto hacia arriba(metros sobre Segundos): "))
    am = objeto / g

    print("\nTarda" , am , "Segundos en llegar a su altura maxima")

def ejercicio_3():
    """
    Hacer un programa que permita ingresar la velocidad con que se lanza un objeto hacia arriba
e indique cuanto tiempo tarda el objeto en regresar al mismo nivel.
    """
    print("\nEjercicio 3.3")
    vi = float(input("Ingrese la velocidad con la que se lanza un objeto hacia arriba(velosidad sobre Segundos): "))
    t1 = vi / g
    x = vi * t1 + 0.5 * g * t1 ** 2
    t2 = math.sqrt(x / (0.5 * g))
    t = t1 + t2
    print("\nTarda" , t , "Segundos en subir y bajar al mismo nivel")

def ejercicio_4():
    """
    Hacer un programa que solicite la velocidad con la que se lanza un objeto y el ángulo respecto
del suelo. Luego calcule cuanto tiempo tarda en caer y la distancia que recorre horizontalmente.
    """
    print("\nEjercicio 3.4")
    v = float(input("Ingrese la velocidad con la que se lanza un objeto hacia arriba: "))
    G = float(input("Ingrese el angulo de lanzamiento (en grados '°'): "))

    G = G * (math.pi / 180)

    vx = v * math.cos(G)
    vy = v * math.sin(G)

    vx = vx * (180 / math.pi)
    vy = vy * (180 / math.pi)
    t1 = vy / g
    medidor_de_tiempo = vy * t1 + 0.5 * g * t1 ** 2
    t2 = math.sqrt(medidor_de_tiempo / (0.5 * g))
    tiempo_total = t1 + t2
    desplazamiento = vx * tiempo_total
    print("\nTarda" , vy , "segundos en caer y se dezplaza hasta" , desplazamiento , "M")
