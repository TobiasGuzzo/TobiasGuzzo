//ejercio 5
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
int lado1;
int lado2;
int lado3;
int rst;

printf("ingrese 3 lados: %c \n");
scanf("%d ", &lado1);
scanf("%d", &lado2);
scanf("%d", &lado3);
if (lado1 == lado2 && lado2 == lado3)
{
    printf("El triangulo es un equilatero");
}
else if (lado1 == lado2 || lado1 == lado3 || lado2 == lado3  )
{
     printf("El triangulo es isoceles");
}
else
{
    printf("El triangulo es escaleno");
}

    return 0;
}




