//ejercicio 3
#include <stdio.h>
#include <math.h>

int main()
{
int numero1 ;
int numero2 ;
int rst ;
 printf("Ingrese 2 numeros%c \n");

    scanf("%d ", &numero1 );
    scanf("%d ", &numero2 );

  printf("Nose porque corno me sigue pidiendo un 3 numero si tengo 3 scans \n");
    if (numero1 > numero2)
    {
        rst = numero1 * numero2;
        printf("\nComo el primer numero ingresado es mayor, se multiplican los dos numero\n");
        printf("\n El resultado de su multiplicacion es el siguiente : %d", rst);
    }
    else if (numero1 == numero2)

    {
        printf("Los numero son iguales ");
    }
    

    
    
    return 0;
}
