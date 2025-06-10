import pygame as pg

class Hrac:
    def __init__(self, x, y, sirka, vyska, chodici_rychlost, skakaci_rychlost, barva = (255, 255, 255), rychlost_x = 0, rychlost_y = 0, nazemi = False, muze_skocit = False,
                 nastaveni = {
                     'doleva': None,
                     'doprava': None,
                     'skakani': None
                 }):

        self.delta_cas = 1

        self.x = x
        self.y = y

        self.nazemi = nazemi
        self.muze_skocit = muze_skocit

        self.sirka = sirka
        self.vyska = vyska

        self.doopravdycka_sirka = sirka
        self.doopravdycka_vyska = vyska

        self.muze_skocit = False

        self.rychlost_x = rychlost_x
        self.rychlost_y = rychlost_y

        self.chodici_rychlost = chodici_rychlost
        self.skakaci_rychlost = skakaci_rychlost

        self.barva = barva
        self.block = 'Hrac'

        self.nastaveni = nastaveni
        self.muze_zvetsovat = True

    def pohni(self):
        self.x += self.rychlost_x * self.delta_cas
        self.y += self.rychlost_y * self.delta_cas

    def nakresly(self, okno):
        pg.draw.rect(okno, self.barva, (self.x, self.y, self.sirka, self.vyska))

    def kolize(self, hrac):
        hrac.x += hrac.rychlost_x * self.delta_cas

        zed_ctverec  = pg.Rect(self.x, self.y, self.sirka, self.vyska)
        hrac_ctverec = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if zed_ctverec.colliderect(hrac_ctverec):

            if hrac.block == 'Enemy':
                return 1

            if hrac_ctverec.left <= zed_ctverec.right <= hrac_ctverec.right:
                hrac.rychlost_x = 0
                hrac.x = zed_ctverec.right

            elif hrac_ctverec.left <= zed_ctverec.left <= hrac_ctverec.right:
                hrac.rychlost_x = 0
                hrac.x = zed_ctverec.left - hrac.sirka

        hrac.x -= hrac.rychlost_x * self.delta_cas
        hrac.y += hrac.rychlost_y * self.delta_cas

        zed_ctverec  = pg.Rect(self.x, self.y, self.sirka, self.vyska)
        hrac_ctverec = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if zed_ctverec.colliderect(hrac_ctverec):

            if hrac_ctverec.top <= zed_ctverec.top <= hrac_ctverec.bottom:
                hrac.rychlost_y = 0
                hrac.nazemi = True
                hrac.y = zed_ctverec.top - hrac.vyska

            elif hrac_ctverec.top <= zed_ctverec.bottom <= hrac_ctverec.bottom:
                hrac.rychlost_y = 0
                hrac.y = zed_ctverec.bottom

        hrac.y -= hrac.rychlost_y * self.delta_cas

        return 0