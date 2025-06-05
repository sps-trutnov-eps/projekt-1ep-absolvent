import pygame



class Button :
    def __init__(self,x,y,textura):
        self.x=x
        self.y=y
        self.textura=textura
        self.rect=pygame.Rect(self.x, self.y, self.textura.get_width(), self.textura.get_height())
        self.funkce=funkce
    
    def draw(self,okno):
        okno.blit(self.textura,(self.rect))
    
    def collide(self,pos):
        
        return self.rect.collidepoint(pos[0],pos[1])
<<<<<<< HEAD
    
    def ktery_button(self,jaka_funkce):
        if jaka_funkce == 1:
            
        if jaka_funkce == 2:

        if jaka_funkce == 3:
=======
        
    
    
        
    
>>>>>>> origin/jirous
