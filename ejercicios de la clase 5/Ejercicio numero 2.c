//ejercicio 2
#include <stdio.h>


int main()
{
int numero ;
 printf("Ingrese un numero (si el programa no arranca ingresar otro numero, va a tomar el primero que ingresaste) \n");
    scanf("%d ", &numero );
printf("\n no se porque el programa pide que pongas 2 cuando solo hay un scan y encima toma el primero que pusiste\n");
    if (numero == 0)
    {
        printf("El numero es igual a cero");
    }
    else if (numero > 0)
    {
         printf("El numero es positivo");
    }
    else
    {
         printf("El numero es negativo");
    }
   
    
    
    
    return 0;
}
