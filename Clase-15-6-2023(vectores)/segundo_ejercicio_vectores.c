#include <stdio.h>

int main() {
    int vector1[3] = {2, 4, 6};
    int vector2[3] = {3, 5, 7};
    int vector3[3];

    
    for(int i = 0; i < 3; i++) {
        vector3[i] = vector1[i] + vector2[i];
    }

  
    printf("El resultado de la suma es: ");
    for(int i = 0; i < 3; i++) {
        printf("%d ", vector3[i]);
    }
    printf("\n");

    return 0;
}
