//Realizar un programa que permita generar una tabla de multiplicar donde
//ingresamos por teclado el resultado de cada valor de la tabla y al finalizar,
//muestre por pantalla los resultados correctos. (Utilizar dos funciones)


/* Programa TABLA cn funciones 1 */
#include <stdio.h>
void ftabla(int);
int ftabla1(int,int);
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
printf("\t Por maquina es %d\n\n",ftabla1(a,num));
}
}
int ftabla1(int a,int num)
{
return(a*num);
}