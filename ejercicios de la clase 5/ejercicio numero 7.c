//ejercio 7
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
int num1;
int num2;
int num3;
int num4;
int rst1;
int rst2;

printf("ingrese 4 numeros: %c \n");
scanf("%d ", &num1);
scanf("%d", &num2);
scanf("%d", &num3);
scanf("%d", &num4);

rst1 = num1 + num2;

rst2 = num3 + num4;

printf("\nlas suma de los primeros 2 numeros son: %d", rst1, "\n");
printf("\nlas suma de los ultimos 2 numeros son: %d", rst2,"\n");
if (rst1 > rst2 )
{
    printf("\nEl primer resultado es mayor que el segundo");
}
else
{
    printf("\nEl segundo resultado es mayor que el primero");   
}




    return 0;
}