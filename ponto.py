class Ponto:
    """ Classe ponto com suas coordenadas"""

    def __init__(self, initX, initY):

        self.x = initX
        self.y = initY

    def getX(self):
        return self.x
    
    def setX(self,x):
        self.x=x

    def getY(self,y):
        return self.y

    def setY(self,y):
        self.y=y
    def distancia(self,q):
        return ((self.x-q.x)**2+(self.y-q.y)**2)**0.5
    
ponto1=Ponto(4,4)
ponto2=Ponto(4,6)
print(ponto1.distancia(ponto2))