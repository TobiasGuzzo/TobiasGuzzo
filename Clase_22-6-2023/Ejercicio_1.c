#include<conio.h>
#include<stdlib.h>
#include <stdio.h>

int main() {
  int matriz[3][3] = 
  {
    {0, 0, 0},
    {0, 0, 0},
    {0, 0, 0}
  };
  
  matriz[0][0] = 1;
  matriz[1][1] = 1;
  matriz[2][2] = 1;

 printf("Matriz:\n");
  for (int f = 0; f < 3; f++) {

    for (int c = 0; c < 3; c++) {
      printf("%d ", matriz[f][c]);
    }
    printf("\n");
  }

  return 0;
}