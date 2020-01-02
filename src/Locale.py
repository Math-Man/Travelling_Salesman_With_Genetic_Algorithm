import math;


class Locale:

    posX = 0;
    posY = 0;

    def __init__(self, posX, posY):
        self.posX = posX;
        self.posY = posY;
        print

    #Euclidian distance calculation
    def calcDistanceFromLocale(self, other):
        return ( math.sqrt(((other.posX - self.posX)**2) + ((other.posY - self.posY)**2)) );
