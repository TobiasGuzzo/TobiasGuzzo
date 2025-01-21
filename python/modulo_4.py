#de tobias guzzo
import math
rta = int()
def ejercicio_1():
    """
 Hacer un programa que indique el monto de una compra de un producto. Debe solicitar al
usuario el precio del producto, la cantidad que lleva y luego indicar el precio total de la venta.

    """
    print("\nEjercicio 4.1")
    a = int(input("\nIngrese el precio del producto: "))
    b = int(input("\nCuantas unidades llevara? "))
    c = a * b
    print( "Debe abonar: " , c , "." )

def ejercicio_2():
    """
 Hacer un programa que calcule el monto total de una compra de distintos productos. El
programa solicita de forma iterativa (repetitiva) al usuario la cantidad de un producto y el costo
individual de ese producto, luego pregunta si desea continuar, en caso afirmativo vuelve a
preguntar lo anterior en caso negativo muestra el resultado final.

    """
    print("\nEjercicio 4.2")
    pro1 = int(input("Indique el costo del producto: $"))
    canti = int(input("Indique la cantidad que desea llevar: "))
    t1 = pro1 * canti
    total = 0

    print("¿Desea continuar agregando? S/N")
    rta = input()

    while(rta == "S"):

        pro2 = int(input("Indique el costo del nuevo producto: $"))
        canti2 = int(input("Indique la cantidad que desea llevar: "))
        t1 = pro2 * canti2
        print("¿Desea continuar agregando? S/N")
        total = total + total2
        rta = input()


    if rta == "N":
        print("\nEl monto toal es de $" , t1 + total)
    else:
        print("\nEl dato ingresado es incorrecto")


def ejercicio_3():
    """
) Hacer un programa que calcule el dinero que se obtiene por un plazo fijo. El usuario ingresa
el monto inicial, la cantidad de meses y el porcentaje mensual que gana el dueño del plazo fijo.
(Debe considerar que cada mes se suma al monto del plazo fijo los intereses ganados)
    """
    print("\nEjercicio 4.3")
    monto_inicial = float(input("\nIngrese el monto inicial del plazo fijo: $"))
    meses_de_plazo = int(input("\nIngrese la cantidad de meses del plazo fijo: "))
    porcentaje_mensual = float(input("\nIngrese el porcentaje mensual del plazo fijo: %"))
    monto_acumulado = monto_inicial
    for  mes in range(meses_de_plazo ):
        interes_generado = ( porcentaje_mensual * monto_acumulado ) / 100
        monto_acumulado = monto_acumulado + interes_generado
    print( "\nAlfianl usted tendra: $" , monto_acumulado , "." )
