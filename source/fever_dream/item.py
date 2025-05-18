import pygame
import random

class Item:
    def __init__(self, x, y, seznam: list, barva: hex):
        self.x = x
        self.y = y

        self.seznam = seznam
        self.barva  = barva

        self.start_pozice = (x, y)

    def nakresli(self, okno):
        pygame.draw.rect(okno, self.barva, (self.x + 1, self.y + 1, 48, 48))

        if self.seznam[0]:
            pygame.draw.rect(okno, 0xFFFFFF, (self.x + 14, self.y + 14, 3, 3))

        if self.seznam[1]:
            pygame.draw.rect(okno, 0xFFFFFF, (self.x + 14, self.y + 33, 3, 3))

        if self.seznam[2]:
            pygame.draw.rect(okno, 0xFFFFFF, (self.x + 33, self.y + 14, 3, 3))

        if self.seznam[3]:
            pygame.draw.rect(okno, 0xFFFFFF, (self.x + 33, self.y + 33, 3, 3))

    def colize(self, bod):
        item_rect = pygame.Rect(self.x, self.y, 48, 48)

        if item_rect.collidepoint(*bod):
            return True

        return False

def newItem(pozice):

    x = 40 + 115 * pozice

    return Item(x, 385, (random.randint(0, 1), random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)), random.choice(((0x111111, 0xAA0000, 0x00AA00, 0x0000AA, 0xAA00AA, 0xAAAA00, 0x00AAAA))))
