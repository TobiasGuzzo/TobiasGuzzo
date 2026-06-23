//ejercio 9
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
int Ttrabajado;
int valor_de_hora;
int rst;

printf("El gil laburante quiere saber cuanto va a cobrar por horas trabajadas \n");
printf("Cuanto va a cobrar por hora el gil laburante?\n");
scanf("%d",&valor_de_hora);
printf("\nAhora cuanto va a trabajar el gil laburante? \n");
scanf("%d",&Ttrabajado);
printf("El gil laburante trabajo : %d",Ttrabajado, "horas");
rst = Ttrabajado * valor_de_hora;
printf("\nEn total el gil laburante cobro por sus horas de trabajo: %d", rst);
if (Ttrabajado >= 50)
{
    printf("\n Como el gil laburante el trabajo mas de 50 horas, al patron se le cayo 100$ y los tomo el gil laburante");
    rst = rst + 100; 
    printf("\n Entonces el gil laburante optiene en total: %d", rst);
}
if (Ttrabajado >= 150)
{
    printf("\nAl parecer el gil laburante trabajo mas de 150 horas y le parecio poco lo que cobro , se afano 100$");
    rst = rst + 100;
    printf("\nEntonces el gil laburante optiene en total: %d", rst); 
}





    return 0;
}