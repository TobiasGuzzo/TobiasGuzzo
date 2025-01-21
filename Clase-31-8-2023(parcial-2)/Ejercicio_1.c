/* Parte teorica del parcial */
/* 1. Definicion de función? */

/* Una funcion es un bloque aparte del main que puede ser llamado de otra seccion del programa
y a su vez, tambien pueden tener parametros y retornar valores. 
Hay 2 tipos de funciones(Valor ,referencia)
En el caso que sea una funcion por valor simepre va a retornar un valor.
En el caso de referencia modifica directamente los datos 
*/
/* ------------------------------------------------------------------ */
/* Parte practica  */

/*2.Teniendo en cuenta el siguiente ejemplo donde el parámetro de la función func(a) es pasadopor valor,a.
a)Indicar cual es el resultado de la variable a.
b) En caso de ser pasado por referencia cual sería el resultado
de la variable a.Justifique */

#include <stdio.h>
int func(int);
int main(void) {
  
int a=8,resultado=0;
resultado=func(a);
printf("El resultado de a es %d",a);

return 0;
}
int func(int x)
{
 x=x+1;
 return x;
}
/* --------------------------------------------------------------------------------------- */
/* Respuesta: */

/* a) La varible "a" seguira siendo 8 porque cuando se manda a la funcion mediante "resultado=func(a);"
  la funcion recibe el parametro "x" y no "a", asi que nunca entra "a" en la funsion haciendo que su valor que es 8 se mantenga  */

/* --------------------------------------------------------------------------------------- */

/* Esto seria el codigo por referencia  */
#include <stdio.h>

void func(int *);

int main(void) {
    int a = 8;
    int resultado;
    func(&a);
    printf("El resultado de a es %d",a);
    return 0;
}

void func(int *x) {
    (*x)++; 
}
/* En el caso de que se pase por valor el valor de "a" seria 9 ya que al pasarlo por referencia "a" entra en la funcion haciendo que se le sume 1 y el vaor
total de "a" sea 9 */


