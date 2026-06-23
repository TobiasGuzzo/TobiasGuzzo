//Realizar un programa que permita generar una tabla de multiplicar, donde
//ingresamos por teclado el resultado de cada valor de la tabla y nos va indicando
//ese resultado es correcto o no. (Utilizar dos funciones)
#include <stdio.h>

void ftabla(int);
void ftabla1(int,int,int);
int main(void) {
int num=0;

printf("Ingrese el valor de la TABLA");
scanf("%d",&num);
ftabla(num);
 return 0;
}
void ftabla(int num)
{
int a,res;
printf("La Tabla del %d\n ",num);
for (a=0;a<=10;a++)
{
printf("%d x %d =",a,num);
scanf("%d",&res);
ftabla1(a,num,res);
}
}
void ftabla1(int a,int num,int res)
{
if (res==a*num)
{printf("\tCorrecto\n");}
else
{printf("\tMal\n");}
}
