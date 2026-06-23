//Ejercicio 1 
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
    
    int acumulador = 0;
    int numeros;
    int promedio;
    
    printf("Ingrese 25 numeros\n ");
    for (size_t i = 0; i < 25; i++)
    {
        scanf("%d", &numeros); 
        acumulador += numeros ;      
    }
    promedio = acumulador /25;
    printf("el promedio en total de los 25 numero es: %d",acumulador);

    return 0;
}
