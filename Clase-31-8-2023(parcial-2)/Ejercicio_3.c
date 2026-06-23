/* Aspectos procedimentales
Ejercicio 1
Desarrollar el siguiente ejercicio: 
Cargar un vector en memoria de 10 elementos, con numeros enteros. Se desea: 
1- Encontrar la posición del mayor de los números cargados en el vector. (En caso de que 
se repita, devolver la última posición).
2- A partir del número encontrado en el punto 1, crear un vector con ese tamaño y 
llenarlos con valores que se incrementan en uno, a partir del cero.
Importante: Utilizar funciones para desarrollar los puntos. 
(Desarrollarlo en C, solo el codigo del programa principal se realiza en diagrama) */

#include <stdio.h>
int main() {
    int vector[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int numero = 10;
    int posicionM = Pmayor(vector, numero);
    printf("La ubicacion del mayor numero dentro del vector es:: %d\n", posicionM);
    Forvector(vector, posicionM + 1);    
    printf("El nuevo vector es: ");
    for (int i = 0; i < posicionM + 1; i++) {
        printf("%d ", vector[i]);
    }
    return 0;
}
void Forvector(int vector[], int  numero) {
    for (int i = 0; i <  numero; i++) {
        vector[i] = i;
    }
}
int Pmayor(int vector[], int numero) {
    int mayor = vector[0];
    int p = 0;
    for (int i = 1; i < numero; i++) {
        if (vector[i] >= mayor) {
            mayor = vector[i];
            p = i;
        }
    }
    return p;
}