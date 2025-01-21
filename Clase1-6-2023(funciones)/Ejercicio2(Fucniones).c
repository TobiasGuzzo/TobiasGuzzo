//Ingresar dos números en caso de que sean iguales mostrar la suma de lo contrario la multiplicación

#include <stdio.h>

int main() {
    int num1 = 5;
    int num2 = 10;
    int resultado;

    // Llamada a la función sumar
    resultado = sumar(num1, num2);

    printf("El resultado de la suma es: %d\n", resultado);

    return 0;
}

// Definición de la función sumar
int sumar(int a, int b) {
    int suma = a + b;
    return suma;
}
