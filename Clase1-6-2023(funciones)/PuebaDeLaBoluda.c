#include <stdio.h>
int funcmia(int);
main()
{
int varglobal=10;	
int judio;
judio=funcmia(varglobal);
printf("%d",judio);	
}
int funcmia(int master)
{
	master= master+50;
	return master;
}