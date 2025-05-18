import pygame

class Okraj:
    def __init__(self, x, y, sirka, vyska, tlustota = 1, barva = (255, 255, 255)):
        self.x = x
        self.y = y

        self.sirka = sirka
        self.vyska = vyska

        self.tlustota = tlustota
        self.barva = barva

    def nakresli(self, okno):
        pygame.draw.rect(okno, self.barva, (self.x, self.y, self.sirka, self.vyska), self.tlustota)
