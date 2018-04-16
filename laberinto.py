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
    if laberinto[listax[0]-1][listax[1]]=="0":
        ##return laberinto[listax[0]-1][listax[1]]
        print ("oka")
    if laberinto[listax[0]+1][listax[1]]=="0":
        ##return laberinto[listax[0]+1][listax[1]]
        print ("oke")
    if laberinto[listax[0]][listax[1]-1]=="0":
        ##return laberinto[listax[0]][listax[1]-1]
        print ("oko")
    if laberinto[listax[0]][listax[1]+1]=="0":
       ## return laberinto[listax[0]][listax[1]-1]
        print ("oki")
    


salida = []
with open('laberinto.txt', 'r') as f:
    laberinto = [linea.split() for linea in f]

print(buscarX(laberinto))
buscarCeros(laberinto,buscarX(laberinto))
