#include <stdio.h>
int main() {
    int vector[10];
    int posicion[10]; 
    int contador = 0; 
    for (int i = 0; i < 10; i++) {
        printf("Ingrese un número entero: ");
        scanf("%d", &vector[i]);
        if (vector[i] == 5) {
            posicion[contador] = i;
            contador++;
        }
    }
    int posicion_minima = 10; 
    for (int i = 0; i < contador; i++) {
        if (posicion[i] < posicion_minima) {
            posicion_minima = posicion[i];
        }
    }
    if (contador > 0) {
        printf("La posición más pequeña de los números 5 es: %d\n", posicion_minima);
    } else {
        printf("No se encontraron números 5 en el vector.\n");
    }
    return 0;
}

