#include <stdio.h>
int main() {
    int vector[10];
    int posicion = 0;
    for (int i = 0; i < 10; i++) {
        printf("Ingrese un número: ");
        scanf("%d", &vector[i]);
    }
    for (int i = 0; i < 10; i++) {
        if (vector[i] == 5) {
            posicion = i;
            break;
        }
    }
    if (posicion != 0) {
        printf("El valor 5 se encuentra en la posición: %d\n", posicion);
    } else {
        printf("El valor 5 no se encontró en el vector.\n");
    }
    return 0;
}
