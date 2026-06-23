#include <stdio.h>
#include <string.h>

void catemp(int[], int, int*, int*, int*, int*);
int may2000(int[], int);
int may1000(int[], int[], int);
void suelmax(char[][20], int[], int);
void suelmin(char[][20], int[], int);
void porcentaje(int, int, int, int, int);

int main(void)
{
    int c = 0, x = 0, categoria[10], sueldo[10], b = 0, auxc = 0, cat1 = 0, cat2 = 0, cat3 = 0, cat4 = 0;
    char nombre[10][20];

    printf("Ingrese cantidad de empleados: ");
    scanf("%d", &x);
    printf("\n");

    for (c = 0; c < x; c++)
    {
        printf("Ingrese nombre del empleado: ");
        scanf("%s", nombre[c]);
        printf("\n");
    }
    for (c = 0; c < x; c++)
    {
        printf("Ingrese categoría del empleado: ");
        scanf("%d", &categoria[c]);
        printf("\n");
    }
    for (c = 0; c < x; c++)
    {
        printf("Ingrese sueldo del empleado: $");
        scanf("%d", &sueldo[c]);
        printf("\n");
    }
    catemp(categoria, x, &cat1, &cat2, &cat3, &cat4); // Punto A y F
    printf("\n");
    b = may2000(sueldo, x); // Punto B
    printf("La cantidad de sueldos que superan los $2000 son: %d\n", b);
    auxc = may1000(categoria, sueldo, x); // Punto C
    printf("La cantidad de empleados de cat1 con sueldo superior a los $1000 son: %d\n", auxc);
    suelmax(nombre, sueldo, x); // Punto D
    suelmin(nombre, sueldo, x); // Punto E
    porcentaje(cat1, cat2, cat3, cat4, x); // Punto G
    return 0;
}

// Punto A y F:
void catemp(int categoria[], int x, int *cat1, int *cat2, int *cat3, int *cat4)
{
    int c = 0;
    for (c = 0; c < x; c++)
    {
        if (categoria[c] == 1)
        {
            (*cat1)++;
        }
        else if (categoria[c] == 2)
        {
            (*cat2)++;
        }
        else if (categoria[c] == 3)
        {
            (*cat3)++;
        }
        else
        {
            (*cat4)++;
        }
    }
    if (*cat1 > *cat2 && *cat1 > *cat3 && *cat1 > *cat4)
    {
        printf("La categoría 1 es la que más empleados tiene\n");
    }
    else if (*cat2 > *cat3 && *cat2 > *cat4)
    {
        printf("La categoría 2 es la que más empleados tiene\n");
    }
    else if (*cat3 > *cat4)
    {
        printf("La categoría 3 es la que mayor empleados tiene\n");
    }
    else
    {
        printf("La categoría 4 es la que mayor empleados tiene\n");
    }
    printf("La cantidad de empleados por categoría son:\n");
    printf("Categoría 1: %d empleados\n", *cat1);
    printf("Categoría 2: %d empleados\n", *cat2);
    printf("Categoría 3: %d empleados\n", *cat3);
    printf("Categoría 4: %d empleados\n", *cat4);
    printf("\n");
}

// Punto B:
int may2000(int sueldo[], int x)
{
    int c = 0, contsueldos = 0;
    for (c = 0; c < x; c++)
    {
        if (sueldo[c] > 2000)
        {
            contsueldos++;
        }
    }
    return contsueldos;
}

// Punto C:
int may1000(int categoria[], int sueldo[], int x)
{
    int c = 0, contcat1 = 0;
    for (c = 0; c < x; c++)
    {
        if (categoria[c] == 1 && sueldo[c] > 1000)
        {
            contcat1++;
        }
    }
    return contcat1;
}

// Punto D:
void suelmax(char nombres[][20], int sueldos[], int x)
{
    int c = 0, max = 0;
    char suelmax[20];
    max = sueldos[0];
    strcpy(suelmax, nombres[0]);
    for (c = 1; c < x; c++)
    {
        if (sueldos[c] > max)
        {
            max = sueldos[c];
            strcpy(suelmax, nombres[c]);
        }
    }
    printf("%s posee el mayor sueldo: $%d\n", suelmax, max);
}

// Punto E:
void suelmin(char nombres[][20], int sueldos[], int x)
{
    int c = 0, min = 0;
    char suelmin[20];
    min = sueldos[0];
    strcpy(suelmin, nombres[0]);
    for (c = 1; c < x; c++)
    {
        if (sueldos[c] < min)
        {
            min = sueldos[c];
            strcpy(suelmin, nombres[c]);
        }
    }
    printf("%s posee el menor sueldo: $%d\n", suelmin, min);
}

// Punto G
void porcentaje(int cat1, int cat2, int cat3, int cat4, int x)
{
    int por1 = 0, por2 = 0, por3 = 0, por4 = 0;
    por1 = (cat1 * 100) / x;
    por2 = (cat2 * 100) / x;
    por3 = (cat3 * 100) / x;
    por4 = (cat4 * 100) / x;
    printf("El porcentaje de empleados por categoría corresponde a:\n");
    printf("Categoría 1: %d%%\n", por1);
    printf("Categoría 2: %d%%\n", por2);
    printf("Categoría 3: %d%%\n", por3);
    printf("Categoría 4: %d%%\n", por4);
}