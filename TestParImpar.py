from ParImpar import parImpar


def test_add():
    p = parImpar([1,2,3,4])
    assert len(p.lista) == 4
    p.add(6)
    assert len(p.lista) == 5

def test_sumaPar():
    lista = [1,2,3,4]
    p = parImpar(lista)
    assert p.sumaPar() == 6 


def test_sumaImpar():
    lista = [1,2,3,4]
    p = parImpar(lista)
    assert p.sumaImpares() == 4

def test_cuadradoLista():
    lista = [1,2,3,4]
    p = parImpar(lista)
    assert p.cuadradoLista() == [1,4,9,16]