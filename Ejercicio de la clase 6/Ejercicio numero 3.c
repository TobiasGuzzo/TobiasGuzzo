//ejercicio 3
#include <stdio.h>

int main() {
    int valor, positivos = 0, negativos = 0, ceros = 0;

    // Pedir los 10 valores
    for (int i = 0; i < 10; i++) {
        printf("Ingrese el valor %d: ", i+1);
        scanf("%d", &valor);

        // Verificar si el valor es positivo, negativo o cero
        if (valor > 0) {
            positivos++;
        } else if (valor < 0) {
            negativos++;
        } else {
            ceros++;
        }
    }

    // Imprimir los resultados
    printf("Cantidad de valores positivos: %d\n", positivos);
    printf("Cantidad de valores negativos: %d\n", negativos);
    printf("Cantidad de ceros: %d\n", ceros);

    return 0;
}
