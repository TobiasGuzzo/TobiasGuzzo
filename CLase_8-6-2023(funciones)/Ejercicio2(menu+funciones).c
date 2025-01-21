#include <stdio.h>
#include <math.h>
int bandera = 1;
int resultado_suma ;
int resultado_multi ;
int main()
{          
    int n, opcion;
    do
    {
        printf( "\n   1. Cargar datos  %c.", 110  );
        printf( "\n   2. Multiplicar los numeros  %c.", 110 );
        printf( "\n   3. sumar los numeros.%c", 110 );
        printf( "\n   0. Salir." );
        printf( "\n\n   Introduzca opcion (1-3): %c", 202 );

        scanf( "%d", &opcion );

        
        switch ( opcion )
        {
            case 1: printf("cargar 2 numeros: \n");
                
                printf("\ningrese los 2 numeros que quiera cargar\n");	
                cargar(&num1,&num2);
                printf("\nEl resultado es:\n");
                printf("%d,%d",num1,num2);	
                    break;

            case 2:  printf("\n multiplicar\n");
                    
                    multiplicar(num1,num2);

                    printf("Los numeros cargados anteiror mente se multiplicaran");	
                    printf("%d,%d",num1,num2);	
                    printf("\nEl resultado de la multiplicacion de los dos numeros cargados son %d:",resultado_multi);
              
                    break;

            case 3:  printf("\n sumar\n");
                    sumar(&num1,&num2);
                    printf("Los numeros cargados anteiror mente se multiplicaran");	
                    printf("%d,%d",num1,num2);	
                    printf("\nEl resultado de la multiplicacion de los dos numeros cargados son %d:",resultado_suma);
              
                    break;
        }  
    } while ( opcion != 0 );

        return 0;
}

void cargar( int *a, int *b)
    {
        scanf("%d",*a );
        scanf("%d",*b );
    
    return 0;
        
    }
 multiplicar(int a,int b)
    {
        if (bandera == 1)
        {
            
         resultado_multi = a * b;    

        }
        
        return resultado_multi;
    }
    suma(int a,int b)
    {
        if (bandera == 1)
        {
            
         resultado_suma = a + b;    

        }
     return resultado_suma;   

    }