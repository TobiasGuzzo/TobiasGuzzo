import math
print("Hipotenusa de un Triangulo cuadrado")
print("Para saber la hipotenusa2 se necesitan:")
C = int(input("Cateto adyacente:"))
C1 = int(input("Cateto opuesto:"))

h = math.sqrt((C*C)+(C1*C1))

print("La hipotenusa es: ", h)