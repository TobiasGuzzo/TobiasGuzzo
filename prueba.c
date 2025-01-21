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

        //primer ejercicio
        printf("ingrese 2 numeros: \n");
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
        //segundo ejercicio
         printf("\n segundo ejercicio\n");
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
        printf("\n tercer ejercicio ejercicio\n");
        printf("\n Sos un gil laburante que cobra una miseria \n");
        printf("\n Cuanto va a cobrar el gil laburante?\n");
        scanf("%d", &sueldo);
        printf("\n Cuanto va a trabajar el gil laburante?\n");         
        scanf("%d",&horas);        
        printf("\nEl gil laburante trabajo: %d",horas);
        resultado_suldo = horas * sueldo ;
        printf("\n En total el gil laburante cobro %d", resultado_suldo);
         printf("\n-----------------------");
        //ejercicio numero 4 
         printf("\n Cuarto ejercicio\n");
         printf("\n ingresa 3 lados de un triangulo para despues scar su perimetro\n");
                        printf("\n ingresa el primer lado\n");
                        scanf("%d", &lado_1);
                        printf("\n ingresa el segundo lado lado\n");
                        scanf("%d", &lado_2);
                        printf("\n ingresa el tercer lado lado\n");
                        scanf("%d", &lado_3);
                        perimetro = lado_1 + lado_2 + lado_3;
                        printf("\n El perimetro del triangulo es: %d", perimetro);


        
        
        
        return 0;

        

 
}

