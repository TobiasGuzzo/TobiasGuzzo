#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{
    int suma= 0;
    float promedio_total =0 ;
    int numero = 0;
    int cantidad = 0; //contador 

    printf("ingrese un numero\n"); 
    scanf("%d", &numero);  
    while (numero != 0 )
    {
        printf("ingese otro numero\n"); 
        suma = numero + suma;
        cantidad++;
        scanf("%d", &numero); 
    
    }
    printf("\n %d", suma);
    printf("\n %d", cantidad);
    promedio_total = suma / cantidad ;
    printf("\n El promedio de la cuenta seria %f", promedio_total);

        return 0;
}
