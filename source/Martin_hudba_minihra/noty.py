import pygame

class nota:
    def __init__(self):
        
        self.poloha_x=poloha_x
        self.poloha_y=600
        self.ktera_nota = 1
        self.aktivní = 0
        
    def cas_na_start(self,hudba,kdy):
        
        if hudba[self.ktera_nota][1]==kdy:
            self.aktivní = 1
            self.poloha_y=hudba[self.ktera_nota][0]*50
            self.ktera_nota += 1
    def pohyb(self):
        
        if self.aktivní ==1:
            self.pohyb_x-=10