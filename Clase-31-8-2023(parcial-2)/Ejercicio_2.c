/* Parte teorica del parcial */
/* Estructura de Dato, mencione y describa los tipos de búsquedas que conoce */

/* Los tipos de busqueda que conocemos hasta la fecha son 2 lineal y binaria:

La lineal es un metodo directo y simple que esta basado en la busqueda de elementos en una mistra estructura de datos

La Busqueda Binaria es un metodo para buscar elemento en una lista en si y haciendo comparaciones en el principal elemento
buscando igualdades y asi encontrando el elemento  */
/* ------------------------------------------------------------------ */
/* Parte practica  */

/* 4. En el siguiente ejemplo confeccionar la función func, para que el vector quede cargado con 
todos 1. */
#include <stdio.h>
int func(int );
int main(void) {
 int vect[2]={0,0};
 int a=2,resultado=0;
 
 resultado=func(a);
 for (int c=0;c<2;c++)
 {
 vect[c]=resultado;
 } 
 return 0;
}
int func(int x)
{
    x = 1;
  return x;
}
