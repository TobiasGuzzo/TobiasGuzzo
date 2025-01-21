from cripto import *

def test_encriptar_tipo():
    dato = encriptar("abcde",1)
    # La función debe devolver str (tipo de dato str)
    assert isinstance(dato, str)
    dato = encriptar("abcdefghijklmn",5)
    assert isinstance(dato, str)
    dato = encriptar("",20)
    assert isinstance(dato, str)

def test_encriptar_longitud():
    # El texto encriptado debe tener la misma longitud que el original
    assert len(encriptar("",1))==0
    assert len(encriptar("papa",2))==len("papa")
    assert len(encriptar("un dia como cualquier otro",3))==len("un dia como cualquier otro")

def test_encriptar():
    dato = encriptar("abcde",1)
    # abcde,1 debe devolver bcdef
    assert dato == "bcdef"
    dato = encriptar("alkeewor",2)
    # alkeewor,2 debe devolver cniggyqt
    assert dato == "cnmggyqt"

def test_desencriptar_tipo():
    dato = desencriptar("bcdef",2)
    # La función debe devolver str (tipo de dato str)
    assert isinstance(dato, str)
    dato = desencriptar("bcdef",9)
    assert isinstance(dato, str)
    dato = desencriptar("",2)
    assert isinstance(dato, str)

def test_desencriptar_longitud():
    # El texto desencriptado debe tener la misma longitud que el encriptado
    assert len(desencriptar("",1))==0
    assert len(desencriptar("sdkjwnjer",2))==len("sdkjwnjer")
    assert len(desencriptar("un dia como cualquier otro",3))==len("un dia como cualquier otro")

def test_desencriptar():
    dato = desencriptar("bcdef",1)
    # abcde,1 debe devolver bcdef
    assert dato == "abcde"
    dato = desencriptar("cnmggyqt",2)
    # cniggyqt,2 debe devolver alkeewor
    assert dato == "alkeewor"
