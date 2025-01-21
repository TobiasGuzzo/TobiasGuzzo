//Ejercicio 2
#include <stdio.h>
#include <math.h>

struct alumno {
    char nombre[20];
    float nota;
};

int main() {
    struct alumno alumnos[20];
    int i;
    
    // Pedir los nombres y notas de los alumnos
    for (i = 0; i < 20; i++) {
        printf("Ingrese el nombre del alumno %d: ", i+1);
        scanf("%s", alumnos[i].nombre);
        printf("Ingrese la nota del alumno %d: ", i+1);
        scanf("%f", &alumnos[i].nota);
    }
    
    // Mostrar los nombres y notas de los alumnos
    printf("\nNombres y notas de los alumnos:\n");
    for (i = 0; i < 20; i++) {
        printf("%s: %.2f\n", alumnos[i].nombre, alumnos[i].nota);
    }
    
    return 0;
}