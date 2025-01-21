// Realizar un programa que genere en pantalla una tabla de multiplicar,
// utilizandouna función que reciba como parámetro un entero que es el que indica a quetabla pertenece y
// despliegue en pantalla la tabla correspondiente
#include <stdio.h>

void imprimir_tabla(int numero) {
    int i;
    for(i = 1; i <= 10; i++) {
        printf("%d x %d = %d\n", numero, i, numero * i);
    }
}

int main() {
    int tabla;
    printf("Ingrese el número de la tabla que desea imprimir: ");
    scanf("%d", &tabla);
    imprimir_tabla(tabla);
    return 0;
}