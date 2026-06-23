#include <stdio.h>
int buscar(int c, int j, int matri[][2]);
int extrae(int c, int vect[]);
int main()
{
    int matri[2][2], c, j;
    int vect[5];
    c = 0;
    j = 0;
    printf("Ingresar los datos del Vector\n");
    for (c = 0; c <= 4; c++)
    {
        scanf("%d", &vect[c]);
    }
    printf("\n Ingresar los datos de la Matriz");
    for (c = 0; c <= 1; c++)
    {
        for (j = 0; j <= 1; j++)
        {
            scanf("%d", &matri[c][j]);
        }
    }
    printf("Ingresar la fila\n");
    scanf("%d", &c);
    printf("Ingresar la columna\n");
    scanf("%d", &j);
    extrae(buscar(c, j, matri), vect);
}
int buscar(int c, int j, int matri[][2])s
{
    if (c < 0 || c > 1 || j < 0 || j > 1)
    {
        return 0;
    }
    return matri[c][j];
}
int extrae(int c, int vect[])
{
    int i, contador = 0;
    for (i = 0; i < 5; i++)
    {
        if (vect[i] == c)
        {
            contador++;
        }
    }
  printf("El elemento de la matriz en la fila %d y columna %d se encuentra %d veces en el vector\n", c, j, contador);
}