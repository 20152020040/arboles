# arboles
juan camilo espitia montoya  20152020040  
Angie Gabriela Antolinez Segura 20151020061



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
        if laberinto[listax[0]-1][listax[1]]=="0":
            print ("arrib")
            return buscarCeros(laberinto,(listax[0]-1,listax[1]))
        if laberinto[listax[0]+1][listax[1]]=="0":
            print ("abaj")
            return buscarCeros(laberinto,(listax[0]+1,listax[1]))
        if laberinto[listax[0]][listax[1]-1]=="0":
            print ("izqu")
            return buscarCeros(laberinto,(listax[0],listax[1]-1))
        if laberinto[listax[0]][listax[1]+1]=="0":
            print ("dere")
            return buscarCeros(laberinto,(listax[0],listax[1]+1))
           ## return laberinto[listax[0]][listax[1]-1]
           
    


salida = []
with open('laberinto.txt', 'r') as f:
    laberinto = [linea.split() for linea in f]

print(buscarX(laberinto))
buscarCeros(laberinto,buscarX(laberinto))
