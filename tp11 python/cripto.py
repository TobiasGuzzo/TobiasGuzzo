
abecedario = "abcdefghijklmnñopqrstuvwxyz "

def encriptar(texto, k):
	"""Encripta el texto con el metodo caesar usando clave numerica k

			Parameters:
                    texto (str):  Texto a encriptar
                    k (int): clave a ser utilizada en el metodo caesar

            Returns:
                    (str): texto encriptado
	"""
	assert isinstance(texto, str)
	assert isinstance(k, int)

	mensaje = texto.lower()
	encriptado= ""

	for letra in mensaje:
		if letra not in abecedario:
			raise Exception(f"La letra {letra} no se encuentra en el abecedario")
		encontrado = False
		pos = 0
		while not encontrado:
			if letra == abecedario[pos]:
				encontrado = True
			else:
				pos += 1

		nueva_pos = pos + k
		if nueva_pos > 27:
			nueva_pos = nueva_pos - 28

		letra_encriptada = abecedario[nueva_pos]
		encriptado = encriptado + letra_encriptada

	return encriptado

def desencriptar(texto, k):
	"""DesEncripta el texto con el metodo caesar usando clave numerica k
			Parameters:
                    texto (str):  Texto a desencriptar
                    k (int): clave a ser utilizada en el metodo caesar

            Returns:
                    (str): texto desencriptado
	"""
	assert isinstance(texto, str)
	assert isinstance(k, int)

	desencriptado = ""
	mensaje = texto.lower()

	for letra in mensaje:
		encontrado = False
		pos = 0
		while encontrado == False:
			if letra == abecedario[pos]:
				encontrado = True
			else:
				pos += 1

		nueva_pos = pos - k
		if nueva_pos < 0:
			nueva_pos = nueva_pos + 28

		letra_desencriptada = abecedario[nueva_pos]
		desencriptado = desencriptado + letra_desencriptada

	return desencriptado
