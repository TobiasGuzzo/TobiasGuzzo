#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{
  int pru [2]; 
  int var = -999999999999999999999999999 ;
  int var1 = 0  ;
  int i = 0;
    printf("ingrese 2 temperaturas\n");
     for (int i = 0; i < 2; i++)
                    {
        scanf("%d", &pru[i]);  
                  
           if (var < pru[i]  )// la muy puta no le gusta los numeros negativos 
    {
           var = pru[i];   
    
        
    }
     if (var1 > pru[i])
    {
       var1 = pru[i];
    }
     if (pru[i] < 0 && var1 > var1)
        {
            var = pru[i];
        }

                    }  

     printf("var es el numero mas grande de toda la lista %d", var);//
     printf("\nvar es el numero mas chico de toda la lista %d", var1);//
  

    return 0;
}