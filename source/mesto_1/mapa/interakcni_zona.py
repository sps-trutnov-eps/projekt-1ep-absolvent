import pygame as pg
from mesto_1.hrac import Hrac

class InterakcniZona:
    def __init__(self, vlevo_x, nahore_y, sirka, vyska, spustena_funkce, argumenty: list = None):
        self.obdelnik = pg.Rect(vlevo_x, nahore_y, sirka, vyska)
        self.funkce = spustena_funkce
        self.argumenty = argumenty

    def interakce(self, hrac: Hrac, kondice_splnena: bool = True):

        interakcni_rect = self.obdelnik.copy()
        hrac_rect = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if kondice_splnena and interakcni_rect.colliderect(hrac_rect):
            if self.argumenty != None:
                self.funkce(*self.argumenty)

            else:
                self.funkce()