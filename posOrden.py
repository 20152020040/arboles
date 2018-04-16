class Nodo:
    def __init__(self, valor,izq=None,der=None):
        self.valor=valor
        self.izquierda=izq
        self.derecha=der

def posorden(arbol):
  if arbol != None:
      posorden(arbol.izquierda)
      posorden(arbol.derecha)
      print(arbol.valor)
      
posorden(Nodo(12,Nodo(9),Nodo(15)))
