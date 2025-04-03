class Ponto:
    """ Classe ponto com suas coordenadas"""

    def __init__(self, initX, initY): #construtor
        self.x = initX
        self.y = initY

   # pegando o valores dos pontos e colocando     
    def getX(self):
        return self.x
    
    def setX(self,x):
        self.x=x

    """ Tarefa feita """
    #Tarefa é fazer o mesmo feito no "X", Altere a classe Ponto acrescentando as funções getY e setY e uma função para calcular a distância entre dois pontos.
    def getY(self,y):
        return self.y
    def setY(self,y):
        self.y=y
    #calculando distancias
    def distancia(self,q):
        return ((self.x-q.x)**2+(self.y-q.y)**2)**0.5
    
ponto1=Ponto(4,4)
ponto2=Ponto(4,6)
print(ponto1.distancia(ponto2))