class Nodo:
    def __init__(self, valor,izq=None,der=None):
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

def inorden(arbol):
  if arbol != None:
      inorden(arbol.izquierda)
      print(arbol.valor)
      inorden(arbol.derecha)

inorden(Nodo(15,Nodo(10,Nodo(9)),Nodo(25, Nodo(20))))

