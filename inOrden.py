class Nodo:
    def __init__(self, valor,izq=None,der=None):
        self.valor=valor
        self.izquierda=izq
        self.derecha=der
        
def inorden(arbol):
  if arbol != None:
      inorden(arbol.izquierda)
      print(arbol.valor)
      inorden(arbol.derecha)

inorden(Nodo(15,Nodo(10,Nodo(9)),Nodo(25, Nodo(20))))
