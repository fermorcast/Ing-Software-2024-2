def valles(lista):
    contador_valle = 0
    no_valles = 0
    for s in lista:
        if contador_valle ==  -1 and s == "U":
            no_valles = no_valles+1
        if s == "U":
            contador_valle = contador_valle+1
        else: 
            contador_valle = contador_valle-1       
    return no_valles


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izq = None
        self.der = None

class ArbolBinarioBusqueda:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izq is None:
                nodo_actual.izq = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izq)
        elif valor > nodo_actual.valor:
            if nodo_actual.der is None:
                nodo_actual.der = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.der)
         
         
    def preorden(self):
        self.lista_preorden = []
        self.preorden_recursivo(self.raiz)
        return self.lista_preorden

    def preorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self.lista_preorden.append(nodo_actual.valor)
            self.preorden_recursivo(nodo_actual.izq)
            self.preorden_recursivo(nodo_actual.der)

    def inorden(self):
        self.lista_inorden = []
        self.inorden_recursivo(self.raiz)
        return self.lista_inorden

    def inorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self.inorden_recursivo(nodo_actual.izq)
            self.lista_inorden.append(nodo_actual.valor)
            self.inorden_recursivo(nodo_actual.der)

    def postorden(self):
        self.lista_postorden = []
        self.postorden_recursivo(self.raiz)
        return self.lista_postorden

    def postorden_recursivo(self, nodo_actual):
        if nodo_actual is not None:
            self.postorden_recursivo(nodo_actual.izq)
            self.postorden_recursivo(nodo_actual.der)
            self.lista_postorden.append(nodo_actual.valor)

def main():
    print(valles("DDDUUUUDDDUU"))
    arbol = ArbolBinarioBusqueda()
    valores = [1,4,7,9,8]
    for valor in valores:
        arbol.insertar(valor)
    print(arbol.preorden())
    print(arbol.inorden())
    print(arbol.postorden())

main()