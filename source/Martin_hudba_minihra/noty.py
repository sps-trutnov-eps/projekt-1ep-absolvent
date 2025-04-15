import pygame

class nota:
    def __init__(self,šířka):
        
        self.poloha_x=poloha_x
        self.poloha_y=0
        self.ktera_nota = 1
        self.aktivní = 0
        
    def cas_na_start(self,hudba,kdy):
        
        if hudba[self.ktera_nota][kdy]:
            self.aktivní = 1
            self.poloha_y=kde_start*50
            
    def pohyb(self):
        
        if self.aktivní ==1:
            self.pohyb_x-=10