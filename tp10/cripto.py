abecedario = "abcdefghijklmnopqrstuvwxyz "
def encriptar(texto, clave):
	"""Encripta el texto con metodo caesar usando clave numerica k"""
	mensaje =  texto.lower()
	encriptado=""
	for i in range(len(texto)):
		letra = texto[i]
		print(letra)
		pos = 0
		ubicacion = False
		while ( not ubicacion):
			if( letra == abecedario[pos]):
				ubicacion = True
			else:
				pos += 1
		npos = pos + clave
		if (npos > 26):
			npos = (npos - 27)
		if (npos < 1):
			npos = (npos + 27)
		nencriptada = abecedario[npos]
		encriptado = encriptado + nencriptada
	return encriptado
def desencriptar(texto, clave):
	"DesEncripta el texto con metodo caesar usando clave numerica k"
	mensaje =  texto.lower()
	desencriptado = ""
	for i in range(len(texto)):
		letra = texto[i]
		print(letra)
		ubicacion = False
		pos = 0
		while (ubicacion == False):
			if(letra == abecedario[pos]):
				ubicacion = True
			else:
				pos += 1
			npos = pos - clave
			if (npos < 0):
				npos = (npos + 27)
		ndesencriptada = abecedario[npos]
		desencriptado = desencriptado + ndesencriptada
	return desencriptado
