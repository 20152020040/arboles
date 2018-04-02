class nodo:
    def__init__(self, valor,izq=none,der=none):
        self.valor=valor
        self.izquierda=izq
        self.derecha=der

def buscar(arbol,valor):
    if arbol==None:
        return False
    if arbol.valor==valor:
        return True
    if valor<arbol.valor:
        return buscar(arbol.izquierda,valor)
    return buscar(arbol.derecha,valor)

def insertar (arbol,valor):
    if arbol==None:
        return nodo(arbol.valor,insertar(arbol.izquierda,valor),arbol.derecha)
    return nodo(arbol.valor,arbol.izquierda,insertar(arbol.derecha,valor))
