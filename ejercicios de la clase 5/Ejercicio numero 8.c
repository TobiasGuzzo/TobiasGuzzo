//ejercio 8
#include <stdio.h>
#include <math.h>

int main(int argc, char const *argv[])
{
//edades
int edad1;
int edad2;
//alturas
float altura1;
float altura2;



printf("ingrese la edad y altura de 2 personas: %c \n");
printf("\nPara la primera persona ingrese primero su edad y altura  %c \n");
scanf("%d ", &edad1);
scanf(" %f", &altura1);
printf("Para la siguiente persona, ingrese la edad y altura\n");
scanf("%d", &edad2);
scanf("%F", &altura2);
printf("\n la primera persona tiene una edad de: %d",edad1);
printf("\n y tiene una altura de: %f",altura1);
printf("\n La segunda persona tiene una edad de: %d",edad2);
printf("\n y tiene una altura de: %f",altura2);
if ( edad1 > edad2)
{
    printf("\nla primera persona tiene edad mayor con una altura de: %f", altura1);
}
else
{
    printf("\nla segunda persona tiene edad mayor con una altura de: %f", altura2); 
}


    return 0;
}