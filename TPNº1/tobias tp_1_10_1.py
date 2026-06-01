def imprimir_cuadrados():
    print("Se calcularán cuadrados de números")

    n1 = int(input("Ingrese un número entero: "))
    n2 = int(input("Ingrese otro número entero: "))

    for i in range(n1, n2):
        print(i * i)

    print("Es todo por ahora")

imprimir_cuadrados()