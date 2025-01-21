#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{

    int suma= 0;
    int factura = 0;
    int importe = 0;
    int cantidad = 0; //contador 

    printf("Que numero de factura es\n"); 
    scanf("%d", &factura);  
    while (factura != 0  )
    {
        printf("ingrese el importe de la factura\n"); 
        scanf("%d", &importe); 
        
        printf("ingresar devuelta otro numero de factura\n");
        scanf("%d", &factura);
        if (importe == 1000)
        {
            suma++;        
        }
        }
        printf("La cantidad de importes que superan los 1000 son %d", suma);
        return 0;
}
