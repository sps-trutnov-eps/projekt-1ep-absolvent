import pygame

class Options:
    def __init__(self, x, y, item):
        self.x = x
        self.y = y
        self.item = item

    def nakresli(self, okno):
        pygame.draw.rect(okno, 0x111111, (self.x, self.y, 100, 50))