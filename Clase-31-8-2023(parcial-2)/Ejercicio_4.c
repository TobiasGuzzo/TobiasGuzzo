/* En el siguiente programa se ingresan cinco números por teclado (enteros positivos y 
negativos) y por medio de dos funciones se desea obtener el mayor de los números
ingresados, teniendo en cuenta:
a. Función extrae debe recibir como parámetro un entero y devolver un entero. 
(Esta función solo debe devolver números positivos entre 1 y 10 caso contrario 
devuelve 0)
b. Función maximo debe recibir solamente dos parámetros positivos. (Esta función 
busca el mayor )
Se deberá crear las funciones en base al ejercicio propuesto a continuación */

#include <stdio.h>

int main(void) {
 int num1,c,max;
max=0;
for (c=1;c<=5;c++)
    printf("Ingrese el numero 1%d:", c);
    scanf("%d", &num1);
    maximo(extrae(num1), &max);
{
printf("Ingrese el numero %d ",c);
scanf("%d",&num1);

maximo(extrae(num1),&max);
}
printf("El mayor es %d",max);
 return 0;
}
 int extrae(int num)
{
    /* Esto es lo agregado para el valor de la funcion extraer   */
      if (num > 0 && num <= 10) {
        return num;
    } else {
        return 0;
    }
}
void maximo(int posicion, int *max)
{
    /* Esto es lo agregado para el valor de la funcion maximo */
      if (posicion > *max) {
        *max = posicion;
    }
}
