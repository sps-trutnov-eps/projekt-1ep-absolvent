import pygame

class nota:
    def __init__(self,poloha_x,poloha_y):
        
        self.poloha_x=poloha_x
        self.poloha_y=poloha_y
        self.ktera_nota = 1
        self.aktivní = 0
        
    def pohyb(self):
        
        if self.aktivní ==1:
            self.pohyb_x-=10