import pygame

class Slot:
    def __init__(self, x, y, sirka, vyska, textura):
        self.x = x
        self.y = y

        self.sirka = sirka
        self.vyska = vyska

        self.textura = textura

    def nakresli(self, okno):
        pygame.draw.rect(okno, self.barva, (self.x, self.y, self.sirka, self.vyska), 1)
        okno.blit(self.textura, (self.x, self.y))
