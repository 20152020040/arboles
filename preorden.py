class Nodo:
    def __init__(self, valor,izq=None,der=None):
        self.valor=valor
        self.izquierda=izq
        self.derecha=der
    
def preorden(arbol):
  if arbol != None:
      print(arbol.valor)
      preorden(arbol.izquierda)
      preorden(arbol.derecha)

preorden(Nodo(15,Nodo(10,Nodo(9)),Nodo(25, Nodo(20))))
