#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

    int Empleados = 50;
    int MESES = 12;
    char empleados[Empleados][50];
    int horas_trabajadas[Empleados];
    float valor_hora[Empleados];
    char meses[Empleados][50];
    int sueldo_anual[Empleados];
    int total_sueldos_por_mes[MESES];
    int cantidad_meses_mayor_100k = 0; 

    for (int i = 0; i < MESES; i++) {
        total_sueldos_por_mes[i] = 0;
    }
    for (int i = 0; i < Empleados; i++) {
        printf("Ingrese el nombre del empleado: ");
        scanf("%s", &empleados[i]);
        printf("Ingrese la cantidad de horas trabajadas por el empleado: ");
        scanf("%d", &horas_trabajadas[i]);
        printf("Ingrese el valor de la hora de trabajo del empleado: ");
        scanf("%f", &valor_hora[i]);
        printf("Ingrese el mes(Especificar en palabras): ");
        scanf("%s", &meses[i]);
        sueldo_anual[i] = horas_trabajadas[i] * valor_hora[i] * MESES;
      
        if (strcmp(meses[i], "Enero") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Febrero") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Marzo") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Abril") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Mayo") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Junio") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Julio") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Agosto") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Septiembre") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Octubre") == 0) { 
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Noviembre") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        } else if (strcmp(meses[i], "Diciembre") == 0) {
            total_sueldos_por_mes[i] += sueldo_anual[i]; 
        }
        if (total_sueldos_por_mes[i] > 100000) {
            cantidad_meses_mayor_100k++;
        }
    }
    printf("\nSueldo anual de cada empleado:\n");
    for (int i = 0; i < Empleados; i++) {
        printf("Nombre: %s, Sueldo anual: $%.2f\n", empleados[i], (float)sueldo_anual[i]); 
    }
    printf("\nTotal de sueldos pagados cada mes:\n");
    for (int i = 0; i < MESES; i++) { 
        printf("Mes: %d, Total de sueldos: $%.2f\n", i + 1, (float)total_sueldos_por_mes[i]);
    }
    printf("\nCantidad de meses en los que el total de sueldos superó los $100000: %d\n", cantidad_meses_mayor_100k);

    return 0;
}
