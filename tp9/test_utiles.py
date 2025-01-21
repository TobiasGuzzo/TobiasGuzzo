from utiles import *

def test_invertir_cadena_tipo():
    dato = invertir_cadena("")
    assert type(dato) is str

def test_invertir_cadena_longitud():
    assert len(invertir_cadena("rata"))==len("rata")

def test_invertir_cadena_rata():
    assert invertir_cadena("rata") == "atar"

def test_invertir_cadena_palindromo():
    assert invertir_cadena("alli va ramon y no maravilla") == "allivaram on y nomar av illa"

def test_cuenta_vocales_tipo():
    dato = cuenta_vocales("")
    assert type(dato) is int

def test_cuenta_vocales_tipo():
    dato = cuenta_vocales("")
    assert type(dato) is int

def test_cuenta_vocales_cero():
    assert cuenta_vocales("crtpl twmncvzb")==0

def test_cuenta_vocales_3a():
    assert cuenta_vocales("satarsa")==3

def test_cuenta_vocales_aeiou():
    assert cuenta_vocales("aeiou")==5

def test_cuenta_vocales_aeiou_mayusculas():
    assert cuenta_vocales("AEIOU")==5

def test_cuenta_menores_tipo():
    dato = cuenta_menores([],0)
    assert type(dato) is int

def test_cuenta_menores_123_4():
    assert cuenta_menores([1,2,3],4)==3

def test_cuenta_menores_123_1():
    assert cuenta_menores([1,2,3],1)==0

def test_contiene_numero_tipo():
    dato = contiene_numero([],0)
    assert type(dato) is bool

def test_contiene_numero_0():
    assert contiene_numero([0],0)

def test_not_contiene_numero_1():
    assert not contiene_numero([0],1)

def test_contiene_numero_1():
    assert contiene_numero([0,1,2,3,4,5],1)

def test_not_contiene_numero_23():
    assert not contiene_numero([0,1,2,3,4,5],23)

def test_contiene_numero_23():
    assert contiene_numero([0,1,23,3,4,5],23)
