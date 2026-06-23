#include <stdio.h>
#include <stdlib.h>
int Alumnos = 20;
int main()
{
    int opcion;
    int primerCuatrimestre[Alumnos];
    int segundoCuatrimestre[Alumnos];
    char nombres[Alumnos][30];
    float promedios[Alumnos];
    do
    {
        printf("Menu:\n");
        printf("1 Cargar notas y nombres\n");
        printf("2 Calcular promedios\n");
        printf("3 Listar alumnos aprobados\n");
        printf("4 Salir del programa\n");
        printf("Ingrese una opción: ");
        scanf("%d", &opcion);
        switch (opcion)
        {
            case 1:
                cargarNotas(primerCuatrimestre, segundoCuatrimestre, nombres);
                break;
            case 2:
                calcularPromedios(primerCuatrimestre, segundoCuatrimestre, promedios);
                printf("Se han calculado los promedios\n\n");
                break;
            case 3:
                listarAprobados(promedios, nombres);
                break;
            case 4:
                printf("Saliendo del programa\n");
                break;
            default:
                printf("Numero inexistente.\n\n");
                break;
        }
    }
    while (opcion != 4);
    return 0;
}
void cargarNotas(int primerCuatrimestre[], int segundoCuatrimestre[], char nombres[])
{
    int i;
    printf("Carga de notas y nombres de alumnos:\n");

    for (i = 0; i < Alumnos; i++)
    {
        printf("Ingrese el nombre del alumno %d:", i + 1);
        scanf("%s", &nombres[i]);
        printf("Ingrese la nota del alumno %s para el primer cuatrimestre (entre 1 y 10): ", nombres[i]);
        scanf("%d", &primerCuatrimestre[i]);
        printf("Ingrese la nota del alumno %s para el segundo cuatrimestre (entre 1 y 10): ", nombres[i]);
        scanf("%d", &segundoCuatrimestre[i]);
    }
}
void calcularPromedios(int primerCuatrimestre[], int segundoCuatrimestre[], float promedios[])
{
    int i;
    for (i = 0; i < Alumnos; i++)
    {
        promedios[i] = (primerCuatrimestre[i] + segundoCuatrimestre[i]) / 2;
    }
}
void listarAprobados(float promedios[], char nombres[])
{
    int i;
    printf("Alumnos que están en condiciones de dar final:\n");
    for (i = 0; i < Alumnos; i++)
    {
        if (promedios[i] >= 4)
        {
            printf("%s\n", nombres[i]);
        }
    }
}
