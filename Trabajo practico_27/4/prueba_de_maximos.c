#include <stdio.h>
#include <math.h>
int main(int argc, char const *argv[])
{
  int pru [3]; 
  int var  ;
  int var1  ;
  int i;
    printf("ingrese 29 numeros\n");
     for (int i = 0; i < 3; i++)
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
 
    
    
                    }  

     printf("var es el numero mas grande de toda la lista %d", var);//
     printf("\nvar es el numero mas chico de toda la lista %d", var1);//
  

    return 0;
}

 
