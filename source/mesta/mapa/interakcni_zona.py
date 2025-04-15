import pygame as pg
from mesta.mapa.hrac import Hrac

class InterakcniZona:
    def __init__(self, vlevo_x, nahore_y, sirka, vyska, spustena_funkce, argumenty: list = None, textura = None):
        self.obdelnik = pg.Rect(vlevo_x, nahore_y, sirka, vyska)
        self.funkce = spustena_funkce
        self.argumenty = argumenty
        self.textura = textura

    def interakce(self, hrac: Hrac, kondice_splnena: bool = True):

        interakcni_rect = self.obdelnik.copy()
        hrac_rect = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if kondice_splnena and interakcni_rect.colliderect(hrac_rect):
            if self.argumenty != None:
                self.funkce(*self.argumenty)

            else:
                self.funkce()

    def nakresli(self, okno, offset = [0, 0]):
        if self.textura != None:
            okno.blit(self.textura, (self.obdelnik.x + offset[0], self.obdelnik.y + offset[1]))

    def nakresliHitbox(self, okno, offset = [0, 0]):
        pg.draw.rect(okno, self.barva, (self.obdelnik.x + offset[0], self.obdelnik.y + offset[1], self.obdelnik.width, self.obdelnik.height))
