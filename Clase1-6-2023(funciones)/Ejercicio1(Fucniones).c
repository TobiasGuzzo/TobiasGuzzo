#include <stdio.h>
int main() {
    int num1;
    int num2;
    int resultado;
    printf("Ingrese 2 numeros \n");
     scanf("%d", &num1);  
     scanf("%d", &num2); 

    if (num1 == num2)
    {
        printf("Como los numeros son iguales se suman \n");
        printf("El resultado es \n %d",sumar(num1,num2));
    }
    else
    {
        printf("El Como los numeros no son iguales se multiplican \n");
        printf("El resultado es \n %d",Mumtiplicacion(num1,num2));
    }
    return 0;
}

// Definición de la función sumar
int sumar(int a, int b) {
    int suma = a + b;
    return suma;
}
int Mumtiplicacion(int a, int b) {
    int multi = a * b;
    return multi;
}
