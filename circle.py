import pygame as PG
from game import Surface as SU

class Circle():
    def __init__(self, color, radius, position, surface):
        self.colR, self.colG, self.colB = color
        self.posX, self.posY = position
        self.size = radius
        self.surf = surface

    def show(self):
        PG.draw.circle(self.surf,
                       (self.colR,self.colG,self.colB),
                       (self.posX, self.posY),
                       self.size)
    
        
    def move(self, moveX, moveY):
        self.posX += moveX
        self.posY += moveY

    def get_pos(self):
        return self.posX, self.posY
            

    def underX(self):
        width, height = self.surf.get_size()
        if self.posX  > width or self.posX  < 0 :
            return True

    def underY(self):
        width, height = self.surf.get_size()
        if self.posY  > height or self.posY  < 0 :
            return True
            
