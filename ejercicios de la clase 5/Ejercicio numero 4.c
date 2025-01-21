//Ejercicio 4
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
int num1;
int num2;
int rts;
printf("ingrese 2 numeros: %c \n");
scanf("%d ", &num1);
scanf("%d", &num2);
printf("");
if (num1  >  num2)
{
    rts = num1 - num2; 
 printf(" Se resto el numero mayor menos el menor, el resultado es: %d", rts);
}
else
{
    rts = num2 - num1;
    printf(" Se resto el numero mayor menos el menor, el resultado es: %d", rts);
}

    return 0;
}

