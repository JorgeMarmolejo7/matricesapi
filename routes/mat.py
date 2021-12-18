from fastapi import APIRouter

mat = APIRouter()




matrizA = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
matrizB = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
matrizC = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]


a = 0
posx = 0
posy = 0

@mat.get('/pide')
def mulmat():
    for i in range(len(matrizA)):
        for j in range(len(matrizB)):
            for k in range(len(matrizB)):
                matrizC[i][j] += matrizA[i][k]*matrizB[k][j]
    
    return str(matrizC)

@mat.post('/actualizam')
def actualiza(nuevo,x,y):
    matrizC[int(x)][int(y)] = nuevo
    return "Posición fila: "+ str(int(x))+ " Posición columna: "+str(int(y))+" Nuevo valor: "+str(int(matrizC[int(x)][int(y)]))

@mat.get('/devmat')
def devmat():
    return str(matrizC)

@mat.get('/coord')
def devc():
    
    global posx
    global posy
    global a

    if (posy == 4):
        posy = -1
        posx += 1
        

    if (posx == 5):
        return "No hay más posiciones"


    if (posy == 0 and a == 0):
        a+=1
        return "Posición x: ["+ str(int(posx))+ "] Posición y: ["+str(int(posy))+"] Valor: "+str(int(matrizC[int(posx)][int(posy)]))

    if(posy < 4 and a == 1):
        posy += 1
        
    return "Posición x: ["+ str(int(posx))+ "] Posición y: ["+str(int(posy))+"] Valor: "+str(int(matrizC[int(posx)][int(posy)]))