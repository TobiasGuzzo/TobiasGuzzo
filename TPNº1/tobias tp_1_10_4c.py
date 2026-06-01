import math
print("Area de un rectangulo ")
print("Para saber el area se necesitan:")
x = int(input("Cordenada x1: "))
x1 = int(input("Cordenada x2: "))
y = int(input("Cordenada y1: "))
y1 = int(input("Cordenada y2: "))

a = math.sqrt(( x1 - x )^2+( y1 - y )^2)

print("El Area total del rectangulo es: ", a)