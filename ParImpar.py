
class parImpar:
    
    lista = []

    def __init__(self, lista):
        self.lista = lista

    def add(self, n):
        self.lista.append(n)
    
    def sumaPar(self):
        suma = 0
        for n in self.lista:
            if n % 2 == 0:
                suma += n
        return suma
    
    def sumaImpares(self):
        suma = 0
        for n in self.lista:
            if n % 2 != 0:
                suma += n
        return suma
    
    def cuadradoLista(self):
        listaCuadrado = []
        for n in self.lista:
            listaCuadrado.append(n*n)
        return listaCuadrado
