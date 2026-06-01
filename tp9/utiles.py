#tobias guzzo
"""
Desarrollas las siguientes funciones sin recurrir a metodos de los tipos de datos
es decir sin usar los metodos split() reverse() del tipo de dato str
y sin usar los metodos del tipo de dato list como sort()

Se espera que la implementación de estas funciones solo haga uso de la sintaxis
del estilo array o arreglos

Ej:
Para obener un valor de un tipo secuenciable hacer
elemento = variable[posicion]

Para asignar un valor a un tipo secuenciable hacer
variable[posicion]= valor
"""
## TODO: Implementar
def invertir_cadena(cadena):
	"""Esta funcion recibe una cadena como parametro y devuelve una cadena con el contenido invertido
	Param: Recibe una cadena y devuelve una cadena

	Ej: si recibe "rata" devuelve "atar"
	Ej: si recibe "animal" devuelve "lamina"
	"""
	cn =""
	for i in range(len(cadena)-1,-1,-1):
		cn = cn + cadena[i]
	return cn
## TODO: Implementar
def cuenta_vocales(cadena):
	"""Recibe una cadena y devuelve la cantidad de vocales que tiene la cadena
	Param: Recibe una cadena y devuelve un numero entero

	Ej: si recibe "rata" devuelve 2
	"""
	contador = 0
	vocales = "aeiouAEIOU"
	for i in range(len(cadena)):
		letra = cadena[i]
		if letra in vocales:
			contador +=1
	return contador
## TODO: Implementar
def cuenta_menores(lista, numero):
    """Recibe una lista de enteros y un numero, devuelve la cantidad de numeros que son menores a dicho numero
    Param: Recibe una lista y un numero y devuelve un numero entero

    Ej: si recibe ([3,5,6,9,1],4) entonces devuelve 2
    """
    contador = 0
    for i in range(len(lista)):
        if(lista[i] < numero):
            contador += 1
    return contador

## TODO: Implementar
def contiene_numero(lista, numero):
    """Recibe una lista de enteros y un numero, indica si el numero se encuentra en la lista
    Param: Recibe una lista y un numero y devuelve True o False

    Ej: si recibe ([3,5,6,9,1],4) entonces devuelve False
    Ej: si recibe ([3,5,6,9,1],5) entonces devuelve True
    """
    contador = False
    for i in range(len(lista)):
        if(lista[i] == numero and contador == False):
            contador = True
    return contador
