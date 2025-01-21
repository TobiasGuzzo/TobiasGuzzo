#include <stdio.h>
#include <stdlib.h>

int main() {

    int vector[10]; 
    int i;

    
    for(i = 0; i < 10; i++) {
        printf("Ingrese el valor para la posición %d: ", i);
        scanf("%d", &vector[i]);
    }

    printf("El vector ingresado es:\n");
    for(i = 0; i < 10; i++) {
        printf("%d ", vector[i]);
    }

    return 0;
}