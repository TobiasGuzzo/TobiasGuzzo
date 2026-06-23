#include <stdio.h>
#include<conio.h>
#include<stdlib.h>
void carga(int[]);
void suma(int[],int,int);
void informe(int[]);

int main()
{
int vec[13]={0};
system("cls");
carga(vec);
system("cls");
informe(vec);
}
void carga(int x[13])
{
int mes, lluvia;
do
{
printf("ingrese el mes");
scanf("%d",&mes);
}while(mes<0||mes>12);
while(mes!=0)
{
printf("ingrese cantidad de lluvia caida");
scanf("%d",&lluvia);
suma(x,mes,lluvia);
do
{
printf("ingrese el mes");
scanf("%d",&mes);
}while(mes<0||mes>12);
}
}
void suma(int x[13],int y, int z)
{
x[y]= x[y]+ z;
}

void informe(int x[13])
{
int i;
for (i=1;i<=12;i++)
{
printf("en el mes %d llovio %d mm\n",i,x[i]);
}
}
