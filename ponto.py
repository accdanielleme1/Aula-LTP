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
        return ((self.x**2-q.x**2)+(self.y**2-q.y**2))**0.5
    
ponto1=Ponto(4,4)

p = Ponto(7,6)

p.setX(5)

print(p.getX())