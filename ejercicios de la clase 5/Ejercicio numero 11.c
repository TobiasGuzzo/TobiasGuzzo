//ejercio 11
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
int categoria;
int sueldo;
int horas_trabajadas;

printf("Ingresar Las horas que va trabajar el gil laburante\n");
scanf("%d",&horas_trabajadas);
printf("Ingresar la categoria del gil laburante(1,2,3) \n");
scanf("%d",&categoria);
if (categoria == 1)
{
    sueldo = horas_trabajadas * 50 ; 
    printf("El laburante es categoria 1 entonces cobra 50 pesos por hora\n"); 
    printf("En total el laburante categoria 1 cobra: %d \n",sueldo); 
}
else if (categoria == 2)
{
    sueldo = horas_trabajadas * 70 ;  
    printf("El laburante es categoria 2 entonces cobra 70 pesos por hora\n"); 
    printf("En total el laburante categoria 2 cobra: %d \n",sueldo); 
}
else if (categoria == 3)
{
    sueldo = horas_trabajadas * 80 ; 
     printf("El laburante es categoria 3 entonces cobra 80 pesos por hora\n"); 
    printf("En total el laburante categoria 3 cobra: %d \n",sueldo); 
}





    return 0;
}
