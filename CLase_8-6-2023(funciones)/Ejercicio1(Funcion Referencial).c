#include <stdio.h>
main()
{
int num1 = 8;	
int num2 = 5;

printf("%d,%d",num1,num2);	
printf("\n-------\n");	
funcion(&num1,&num2);

printf("%d,%d",num1,num2);	
}
void funcion(int *b,int *a)
{
	int r = 0;
    r = *b;
    *b = *a;	
    *a = r;
}
