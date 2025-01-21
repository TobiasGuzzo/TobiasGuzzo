//ejercio 6
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
int num1;
int num2;
int num3;
int pro;

printf("ingrese 3 numeros: %c \n");
scanf("%d ", &num1);
scanf("%d", &num2);
scanf("%d", &num3);
pro = num1 + num2 + num3;
pro = pro / 3;
printf("El promedio es: %d", pro);
 if (pro > num1)
 {
    printf("\nEl promedio es mayor que el primer numero ingresado que es: %d",num1 );
 }
  if (pro > num2)
  {
    printf("\nEl promedio es mayor que el segundo numero ingresado que es: %d",num2);
  }
  if (pro > num3)
  {
    printf("\nEl promedio es mayor que el tercero numero ingresado que es: %d",num3);
  } 
 

    return 0;
}

