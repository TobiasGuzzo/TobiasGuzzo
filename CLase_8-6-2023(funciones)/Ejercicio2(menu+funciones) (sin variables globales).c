#include <stdio.h>
#include <stdlib.h>
   
 void  SyM (int x, int y, int bandera, int salir)
 {
 		if (bandera==1)
 		{
 			if (salir==2)
 			{
 			int multi=0;
			multi= x * y;
			printf ("%d.\n", multi);	
 			}
 			else
 			{
 				int suma=0;	
				suma= x + y;
				printf ("%d\n", suma);	
 			}
 		}
 		else
 		{
 			printf ("necesitas cargar los datos primeros");
 		}
 }

int main(int argc, char *argv[]) 
{
	int num1=0, num2=0, salir=0, bandera=0;
	do
	{
		printf (".\n");
		printf("Menu\n");
		printf("\n1--Carga de Datos");
		printf("\n2--Multiplicar ");
		printf("\n3--Sumar ");
		printf("\n4--Salir");
		printf("\nIngrese la Opcion...");
		scanf("%d",&salir);
		switch (salir)
		{
			case 1: cargar (&num1, &num2, &bandera);
			break;
			case 2: SyM (num1, num2, bandera, salir);
			break;
			case 3: SyM  (num1, num2, bandera, salir);
			break;
			default: printf ("saliste");
			break;
		}
		
		
	}
	while (salir!=4);

	return 0;
	
}

void cargar (int *x, int *y, int *bandera)
{
	*bandera = 1;
	scanf ("%d", &*x);
	scanf ("%d", &*y);
	
}

void sumar (int x, int y, int bandera)
	{

	if (bandera==1)
		{
		int suma=0;	
		suma= x + y;
		printf ("%d\n", suma);
			
		
		}
	else
	{
		printf ("necesitas cargar los datos primeros");
		
	}
	}

	void multiplicacion (int a, int b, int bandera)
	{
	
		if (bandera==1)
		{
		int multi=0;
		multi= a * b;
		printf ("%d.\n", multi);
		
		}
	else 
		{
		printf ("pasar primero por la instruccion numero 1");
		}
   }


