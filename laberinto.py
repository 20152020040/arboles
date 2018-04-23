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
        #if laberinto[listax[0]-1][listax[1]]=="0":
            #print ("arrib")
            #return buscarCeros(laberinto,(listax[0]-1,listax[1])) 
        if laberinto[listax[0]+1][listax[1]]=="0":
            print ("abaj")
            listarep.append([listax])
            print(listarep)
            return buscarCeros(laberinto,(listax[0]+1,listax[1])) 
        ##if laberinto[listax[0]][listax[1]-1]=="0":
            #print ("izq")
            #return buscarCeros(laberinto,(listax[0],listax[1]-1))
        if laberinto[listax[0]][listax[1]+1]=="0":
            print ("dere")
            listarep.append([listax])
            print(listarep)
            return buscarCeros(laberinto,(listax[0],listax[1]+1))
    


salida = []
with open('laberinto.txt', 'r') as f:
    laberinto = [linea.split() for linea in f]

print(buscarX(laberinto))
buscarCeros(laberinto,buscarX(laberinto))
