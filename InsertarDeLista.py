class Nodo:
    def __init__(self, valor,izq=None,der=None):
        self.valor=valor
        self.izquierda=izq
        self.derecha=der

def insertar (arbol,valor):
    if arbol==None:
        return Nodo(valor)
    if valor<arbol.valor:
        return Nodo(arbol.valor,insertar(arbol.izquierda,valor),arbol.derecha)
    return Nodo(arbol.valor,arbol.izquierda,insertar(arbol.derecha,valor))

def inorden(arbol):
  if arbol != None:
      inorden(arbol.izquierda)
      print(arbol.valor)
      inorden(arbol.derecha)
      
def listar(arbol,lista):
    if lista==[]:
        return arbol
    else:
        return listar(insertar(arbol,lista[0]),lista[1:])
    
   


    
inorden(listar((Nodo(15,Nodo(10,Nodo(9)),Nodo(25, Nodo(20)))),[21,7,46,34,2000]))
