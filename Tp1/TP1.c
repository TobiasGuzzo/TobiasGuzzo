#include <stdio.h>

int main() {
    int matri[5][5],f, c, elem;

    for (f = 0; f <= 4; f++) {
        for (c = 0; c <= 3; c++) {
            printf("Ingrese el elemento f%d , c%d ", f, c);
            scanf("%d", &matri[f][c]);
        }
    }

    mostrorigen(matri);
    mostrcamb(matri, 2);

    for (f = 0; f <= 4; f++) {
        for (c = 0; c <= 4; c++) {
            printf("%d ", matri[f][c]);
        }
        printf("\n");
    }

    return 0;
}

void mostrorigen(int matri[][5]) {
    int f, c;

    for (f = 0; f <= 4; f++) {
        for (c = 0; c <= 3; c++) {
            printf("%d ", matri[f][c]);
        }
        printf("\n");
    }
}

void mostrcamb(int matri[][5], int elem) {
    int a = 0;
    for (int f = 0; f < 5; f++) {
        a = 0;
        for (int columna = 0; columna <= 3; columna++) {
            if (matri[f][columna] == elem) {
                a++;
            }
        }
        if (a > 1) {
            matri[f][4] = 1;
        } else {
            matri[f][4] = 0;
        }
    }
}

