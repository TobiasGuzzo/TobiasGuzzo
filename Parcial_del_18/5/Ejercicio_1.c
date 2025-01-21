//Evaluacion del dia 18/5/2023
#include <stdio.h>

int main(int argc, char const *argv[]) {
    
    int numFacturas = 10;
    int contador = 0;
    int numArticulo;
    int cantidad;
    int articuloMasFacturo = 0;
    int precio;
    int facturacion;
    float facturacionTotal = 0;
    float facturacionArticulo1 = 0;
    float facturacionArticulo2 = 0;
    float maxFacturacion = 0;
    

    while (contador < numFacturas) {
        printf("Ingrese los datos de la factura %d:\n", contador + 1);

        printf("Número de artículo: ");
        scanf("%d", &numArticulo);

        printf("\nCantidad vendida del artículo: ");
        scanf("%d", &cantidad);

        printf("\nPrecio unitario del artículo: ");
        scanf("%f", &precio);

        facturacion = cantidad * precio;
        facturacionTotal += facturacion;

        if (numArticulo == 1) {
            facturacionArticulo1 += facturacion;
        } else if (numArticulo == 2) {
            facturacionArticulo2 += facturacion;
        }

        if (facturacion > maxFacturacion) {
            maxFacturacion = facturacion;
            articuloMasFacturo = numArticulo;
        }

        printf("\n");
        contador++;
    }

    float promedioFacturacion = facturacionTotal / numFacturas;

    printf("\nFacturación total: %.2f", facturacionTotal);
    printf("\nFacturación del artículo 1: %.2f", facturacionArticulo1);
    printf("\nFacturación del artículo 2: %.2f", facturacionArticulo2);
    printf("\nArtículo que más facturó: %d", articuloMasFacturo);
    printf("\nPromedio de facturación: %.2f", promedioFacturacion);

    return 0;
}