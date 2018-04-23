class Nodo_n:
    def init (self, valor, hijos=[]):
        self.valor=valor
        self.hijos=hijos

def buscarX(lista):
    for x in range(len(laberinto)):
        for y in range(len(laberinto[x])):
            if "x" in str(laberinto[x][y]) :
                return [x,y]

    
def buscarCeros(laberinto,listax):
    if ("x" in laberinto[listax[0]][listax[1]] or "0" in laberinto[listax[0]][listax[1]]):
        if laberinto[listax[0]][listax[1]+1]=="Y" or laberinto[listax[0]][listax[1]-1]=="Y" or laberinto[listax[0]+1][listax[1]]=="Y" or laberinto[listax[0]-1][listax[1]]=="Y":
            print("Se puede solucionar el Laberinto")
        if laberinto[listax[0]-1][listax[1]]=="0":
            if([(listax[0]-1,listax[1])] in listarep):
                print (" ")
            else:
                print ("arrib")
                listarep.append([(listax[0]-1,listax[1])])
                print(listarep)
                return buscarCeros(laberinto,(listax[0]-1,listax[1]))
            
        if laberinto[listax[0]+1][listax[1]]=="0":
            if([(listax[0]+1,listax[1])] in listarep):
                print (" ")
            else:
                print ("abaj")
                listarep.append([(listax[0]+1,listax[1])])
                print(listarep)
                return buscarCeros(laberinto,(listax[0]+1,listax[1]))
            
        if laberinto[listax[0]][listax[1]-1]=="0":
            if([(listax[0],listax[1]-1)] in listarep):
                print (" ")
            else:
                print ("izq")
                listarep.append([(listax[0],listax[1]-1)])
                print(listarep)
                return buscarCeros(laberinto,(listax[0],listax[1]-1))
            
        if laberinto[listax[0]][listax[1]+1]=="0":
            if([(listax[0],listax[1]+1)] in listarep):
                print (" ")
            else:
                print ("dere")
                listarep.append([(listax[0],listax[1]+1)])
                print(listarep)
                return buscarCeros(laberinto,(listax[0],listax[1]+1))
       
    


salida = []
with open('laberinto.txt', 'r') as f:
    laberinto = [linea.split() for linea in f]

listarep=[buscarX(laberinto) ]
print(buscarX(laberinto))
buscarCeros(laberinto,buscarX(laberinto))
