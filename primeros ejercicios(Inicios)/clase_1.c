#include <stdio.h>
#include <math.h>

int main()
{       

       //esto es para el primero ejercicio
        int num1;
        int num2;
        int resultado;
          // Esto es para el segundo ejercicio
        int num_1;
        int num_2;
        int num_3;
        int resultado_1;
        int resultado_2;
      //Esto es para el tercer ejercicio
        int horas;
        int sueldo; 
        int resultado_suldo;

        // Esto es para el 4 ejercicio
        int lado_1;
        int lado_2;
        int lado_3;
        int perimetro;

      //esto es para el 5 ejercicio
        int numero_c;
        int numero_c2;
        int resultado_mayor;
      
      //Esto es para el 6 ejercicio
      int temperatura; 
      int resultado_temperatura;
      //Esto es para el ejercicio 7
      int temperaturas [4];


        //intento de menu
   
    int n, opcion;
    do
    {
        printf( "\n   1. Ejercicio calcular la suma de 2 numeros  %c.", 110  );
        printf( "\n   2. Calcular la suma de 3 numeros de forma en 2 %c.", 110 );
        printf( "\n   3. Calcula cuanto cobra el gil laburante.%c", 110 );
        printf( "\n   4. Calcula el perimetro de un triangulo.%c", 110 );
        printf( "\n   5. Formato de if con condicionales .%c", 110 );
        printf( "\n   6. ejercicio de temperatura .%c", 110 );
        printf( "\n   7. ejercicios con 4 temperaturas .%c", 110 );
        printf( "\n   8.  .%c", 110 );
        printf( "\n   0. Salir." );
        printf( "\n\n   Introduzca opcion (1-8): %c", 202 );

        scanf( "%d", &opcion );

        /* Inicio del anidamiento */

        switch ( opcion )
        {
            case 1: printf("ingrese 2 numeros: \n");
                    scanf("%d ", &num1);
                    scanf("%d", &num2);
                    printf("--------------------\n");
                    printf("los valores del numero 1 es: %d",num1);
                    printf("\n-----------------------");
                    printf( "\nel resultado de numero 2 es: %d", num2);
                    printf("\n-----------------------");
                    resultado = num1 + num2 ;
                    printf("\nEl resultado de la suma de los 2 numeros %d", resultado);
                    printf("\n-----------------------");
                    break;

            case 2:  printf("\n segundo ejercicio\n");
                        printf("\n ingresa 3 numeros\n");
                        scanf("%d", &num_1);
                        scanf("%d", &num_2);
                        scanf("%d", &num_3);
                        printf("--------------------\n");
                        printf("\nlos valores del numero 1 es: %d",num_1);
                        printf("\nlos valores del numero 2 es: %d",num_2);
                        printf("\nlos valores del numero 3 es: %d",num_3);
                        resultado_1 = num_1 + num_2 ;
                        printf("\nel resultado de la suma de los 2 primeoros numero es %d: " ,resultado_1);
                        resultado_2 = resultado_1 + num_3;
                        printf("\nEl resultado de todo los numeros sumando es: %d: " ,resultado_2);
                    break;

            case 3:  printf("\n tercer ejercicio ejercicio\n");
                    printf("\n Sos un gil laburante que cobra una miseria \n");
                    printf("\n Cuanto va a cobrar el gil laburante?\n");
                    scanf("%d", &sueldo);
                    printf("\n Cuanto va a trabajar el gil laburante?\n");         
                    scanf("%d",&horas);        
                    printf("\nEl gil laburante trabajo: %d",horas);
                    resultado_suldo = horas * sueldo ;
                    printf("\n En total el gil laburante cobro %d", resultado_suldo);
                    break;
            case 4:  printf("\n Cuarto ejercicio\n");
                        printf("\n ingresa 3 lados de un triangulo para despues scar su perimetro\n");
                        printf("\n ingresa el primer lado\n");
                        scanf("%d", &lado_1);
                        printf("\n ingresa el segundo lado \n");
                        scanf("%d", &lado_2);
                        printf("\n ingresa el tercer lado \n");
                        scanf("%d", &lado_3);
                        perimetro = lado_1 + lado_2 + lado_3;
                        printf("\n El perimetro del triangulo es: %d", perimetro);
                    break;
            case 5:  printf("\n quinto ejercicio\n");
                      printf("Ingresar 2 numero y se determinara cuando es mayor o menor\n");
                      printf("ingresar el primero numero\n ");
                      
                      scanf("%d",&numero_c);

                      printf("ingresar el segundo numero\n ");
                      scanf("%d",&numero_c2);
                        if (numero_c < numero_c2)
                        {
                          printf("En este caso los numero se sumaron\n");                          
                          resultado_mayor = numero_c + numero_c2;
                          printf("la suma es %d", resultado_mayor);
                        }
                        else
                        {
                          printf("En este caso los numero se multiplicaron\n");
                           resultado_mayor = numero_c * numero_c2;
                          printf("La multiplicacion es: %d", resultado_mayor);
                  
                        }
                        
                    
                    break;
          case 6:   printf("sexto ejercicio");
                    printf("\nejercicio de temperatura");
                    printf("Ingrese una temperatura \n\n");
                    scanf("%d", &temperatura);
                    
                    if (temperatura == 0)
                    {
                      printf("La temperatura ingresada es igual a 0 \n");
                    }
                    if (temperatura > 0)
                    {
                      printf("La temperatura ingresada es positiva \n");
                    }
                    if (temperatura < 0)
                    {
                      printf("La tamperatura ingresada es negativa \n");
                    }

                    break;

          case 7 : printf("Mas ejercicios de temperatura ");          
                    printf("\nIngrese 4 numeros para generar \n ");    
                    for (int i = 0; i < 4; i++)
                    {
                    scanf("%d", &temperaturas[i]);  
                    if (temperaturas[i] < 0)
                        {
                        printf("Esta temperatura es menor a 0: %d", temperaturas[i],"\n \n");
                        }
                    else if (temperaturas[i] > 0)
                    {
                      printf("\nEsta temperatura no es menor a 0\n ");
                    }
                    
                    }  
                 
      
                    break;

          case 8 :  printf("Este es el ejercicio numero 8");
                      printf("");



         }


    } while ( opcion != 0 );

        return 0;

        

 
}

