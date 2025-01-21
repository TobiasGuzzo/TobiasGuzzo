#include <stdio.h>


int main(int argc, char const *argv[]) {
    int numTemperaturas = 10;
    int contador = 0;
    int temperatura;
    int temperaturaMinima = 20;  // Inicializamos con un valor alto
    int temperaturaMaxima = -5;  // Inicializamos con un valor bajo
    int contadorTemperaturasEntre0y5 = 0;

    while (contador < numTemperaturas) {
        printf("Ingrese la temperatura %d: ", contador + 1);
        scanf("%d", &temperatura);

        // Verificar si es la temperatura mínima
        if (temperatura < temperaturaMinima) {
            temperaturaMinima = temperatura;
        }

        // Verificar si es la temperatura máxima
        if (temperatura > temperaturaMaxima) {
            temperaturaMaxima = temperatura;
        }

        // Verificar si la temperatura está entre 0 y 5
        if (temperatura >= 0 && temperatura <= 5) {
            contadorTemperaturasEntre0y5++;
        }

        contador++;
    }

    printf("Temperatura mínima: %d\n", temperaturaMinima);
    printf("Temperatura máxima: %d\n", temperaturaMaxima);
    printf("Cantidad de temperaturas entre 0 y 5: %d\n", contadorTemperaturasEntre0y5);

    return 0;
}