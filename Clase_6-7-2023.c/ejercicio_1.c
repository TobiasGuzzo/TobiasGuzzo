#include <stdio.h>
int main() {
    int numeros[10]; 
    int posicion = 0; 
    printf("Ingrese 10 números distintos:\n");
    printf("La idea es revisar si uno de los numeros ingresador es un 5\n");
    for (int i = 0; i < 10; i++) {
        scanf("%d", &numeros[i]);
    }
    for (int i = 0; i < 10; i++) {
        if (numeros[i] == 5) {
            posicion = i; 
            break; 
        }
    }
    if (posicion != 0) {
        printf("El valor 5 se encuentra en la posición %d.\n", posicion);
    } else {
        printf("El valor 5 no se encuentra en el vector.\n");
    }
    return 0;
}
