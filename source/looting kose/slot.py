import pygame

class Slot:
    def __init__(self, x, y, sirka, vyska, barva):
        self.x = x
        self.y = y

        self.sirka = sirka
        self.vyska = vyska

        self.barva = barva
        self.overlay = pygame.Surface((sirka, vyska), pygame.SRCALPHA)
        self.overlay.fill(self.barva)

    def vykresli(self, okno):
        okno.blit(self.overlay, (self.x, self.y))