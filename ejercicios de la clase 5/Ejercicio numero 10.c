//ejercio 10
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
int categoria;
int sueldo;
int antiguedad;
int final;
printf("Ingresar El sueldo de este trabajador\n");
scanf("%d",&sueldo);
printf("Ingresar la categoria de este trabajador(1,2,3)\n");
scanf("%d",&categoria);
printf("Ingrese la antiguedad en numero del laburante\n");
scanf("%d",&antiguedad);
if (categoria == 1 )
{
    printf("Como el pobre trabajador es de categoria 1 se le sumara 50$ por años de actividad al sueldo\n");
    final = antiguedad * 50 ;
    sueldo = sueldo + final;
     printf("El pobre laburante en total cobro: %d", sueldo);
}
else
{
    printf("el pobre trabajador solo cobra: %d", sueldo);
}


    return 0;
}
