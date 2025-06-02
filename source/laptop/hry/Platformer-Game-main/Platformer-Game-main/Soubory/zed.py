import pygame as pg
from hrac import Hrac

class Zed:
    def __init__(self, rozliseni_okna, x, y, sirka, vyska, block, barva = (-1, -1, -1), rychlost_x = 0, rychlost_y = 0, nazemi = True, aktivni = False, propojene_itemy = [], pozice = 0, pohybova_durace = None, kouka_vlevo = False, chodici_rychlost = 0, rychlost_nahoru = 0):
        self.rozliseni_okna = rozliseni_okna
        self.muze_zvetsovat = False

        self.delta_cas = 1

        self.x = x * rozliseni_okna[0] / 64
        self.y = y * rozliseni_okna[1] / 36

        self.originalni_y = self.y

        self.grid_x = x
        self.grid_y = y

        self.sirka = sirka * rozliseni_okna[0] / 64
        self.vyska = vyska * rozliseni_okna[1] / 36

        self.block = block
        self.nazemi = nazemi

        self.propojene_itemy = propojene_itemy.copy()
        self.aktivni = aktivni

        self.kouka_vlevo = kouka_vlevo

        if chodici_rychlost == 0 and self.block == 'Enemy':
            self.chodici_rychlost = rozliseni_okna[0] / 640

        else:
            self.chodici_rychlost = chodici_rychlost

        if rychlost_nahoru == 0 and self.block == 'Dvere':
            self.rychlost_nahoru = -rozliseni_okna[0] / 1920

        else:
            self.rychlost_nahoru = rychlost_nahoru

        self.rychlost_x = rychlost_x
        self.rychlost_y = rychlost_y

        if self.rychlost_x == 0 and self.block == 'Enemy':
            self.rychlost_x = -1

        if barva == (-1, -1, -1):
            if self.block == 'Zed':
                self.barva = (255, 0, 0)

            elif self.block == 'Krabice':
                self.barva = (0, 255, 0)

            elif self.block == 'Tlacitko':
                self.barva = (165, 3, 252)

            elif self.block == 'Dvere':
                self.barva = (252, 223, 3)

            elif self.block == 'Enemy':
                self.barva = (235, 52, 216)

            elif self.block == 'Cil':
                self.barva = (0, 0, 255)

            elif self.block == 'Tlacitko Zmensovani':
                self.barva = (150, 150, 150)

            else:
                self.barva = (255, 255, 255)

        else:
            self.barva = barva

        self.pozice = pozice

        if pohybova_durace == None:
            self.pohybova_durace = rozliseni_okna[1] / 36

        else:
            self.pohybova_durace = pohybova_durace

    def nakresly(self, okno):
        pg.draw.rect(okno, self.barva, (self.x, self.y, self.sirka, self.vyska))

    def pohni(self):

        if self.block == 'Dvere':
            if self.pozice == 0:
                self.y = self.originalni_y

            elif self.pozice == self.pohybova_durace:
                self.y = self.originalni_y - self.pohybova_durace

        self.x += self.rychlost_x * self.delta_cas
        self.y += self.rychlost_y * self.delta_cas

    def kolize(self, hrac: Hrac):

        hrac.x += hrac.rychlost_x * self.delta_cas

        zed_ctverec  = pg.Rect(self.x, self.y, self.sirka, self.vyska)
        hrac_ctverec = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if zed_ctverec.colliderect(hrac_ctverec):

            if self.block == 'Krabice':
                if hrac_ctverec.left <= zed_ctverec.right <= hrac_ctverec.right:
                    self.x = hrac.x - self.sirka # nefunguje prava kolize objektu

                if hrac_ctverec.left <= zed_ctverec.left <= hrac_ctverec.right:
                    self.x = hrac.x + hrac.sirka

            if hrac_ctverec.left <= zed_ctverec.right <= hrac_ctverec.right:
                hrac.rychlost_x = 0
                hrac.x = zed_ctverec.right

                if hrac.block == 'Enemy':
                    hrac.kouka_vlevo = False

            if hrac_ctverec.left <= zed_ctverec.left <= hrac_ctverec.right:
                hrac.rychlost_x = 0
                hrac.x = zed_ctverec.left - hrac.sirka

                if hrac.block == 'Enemy':
                    hrac.kouka_vlevo = True

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

    def tlacitkoKolize(self, hrac: Hrac, list_objektu):
            
        zed_ctverec  = pg.Rect(self.x, self.y, self.sirka, self.vyska)
        hrac_ctverec = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if self.block == 'Tlacitko':

            if self.propojene_itemy != []:
                if zed_ctverec.colliderect(hrac_ctverec):
                    for objekt in list_objektu:
                        for koordinace in self.propojene_itemy:
                            if objekt.grid_x == koordinace[0] and objekt.grid_y == koordinace[1]:
                                objekt.aktivni = True

        if self.block == 'Tlacitko Zvetsovani' and hrac.muze_zvetsovat and zed_ctverec.colliderect(hrac_ctverec) and self.rozliseni_okna[1] / 10 > hrac.vyska:
            hrac.y -= self.rozliseni_okna[1] / 5400 * self.delta_cas * 5
            hrac.x -= self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48 / 2

            hrac.doopravdycka_sirka += self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48
            hrac.doopravdycka_vyska += self.rozliseni_okna[1] / 5400 * self.delta_cas

            hrac.skakaci_rychlost -= self.rozliseni_okna[1] / 5400 * self.delta_cas / 8

            hrac.sirka = int(hrac.doopravdycka_sirka)
            hrac.vyska = int(hrac.doopravdycka_vyska)

        if self.block == 'Tlacitko Zmensovani' and zed_ctverec.colliderect(hrac_ctverec) and self.rozliseni_okna[1] / 43.2 < hrac.vyska:
            hrac.doopravdycka_sirka -= self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48
            hrac.doopravdycka_vyska -= self.rozliseni_okna[1] / 5400 * self.delta_cas

            hrac.skakaci_rychlost += self.rozliseni_okna[1] / 5400 * self.delta_cas / 8

            hrac.x += self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48 / 2

            hrac.sirka = int(hrac.doopravdycka_sirka)
            hrac.vyska = int(hrac.doopravdycka_vyska)

    def cilKolize(self, hrac: Hrac):

        zed_ctverec  = pg.Rect(self.x, self.y, self.sirka, self.vyska)
        hrac_ctverec = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if zed_ctverec.colliderect(hrac_ctverec):
            return 1

        return 0

    def zvetsovaciKolize(self, hrac: Hrac):
        if self.block == self.block == 'Tlacitko' or self.block == 'Tlacitko Zvetsovani' or self.block == 'Tlacitko Zmensovani' or self.block == 'Cil':
            return 0

        hrac.y -= self.rozliseni_okna[1] / 5400 * self.delta_cas * 5
        hrac.x -= self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48 / 2

        hrac.doopravdycka_sirka += self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48
        hrac.doopravdycka_vyska += self.rozliseni_okna[1] / 5400 * self.delta_cas

        hrac.sirka = int(hrac.doopravdycka_sirka)
        hrac.vyska = int(hrac.doopravdycka_vyska)

        zed_ctverec  = pg.Rect(self.x, self.y, self.sirka, self.vyska)
        hrac_ctverec = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

        if zed_ctverec.colliderect(hrac_ctverec):
            hrac.muze_zvetsovat = False

        hrac.doopravdycka_sirka -= self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48
        hrac.doopravdycka_vyska -= self.rozliseni_okna[1] / 5400 * self.delta_cas

        hrac.y += self.rozliseni_okna[1] / 5400 * self.delta_cas * 5
        hrac.x += self.rozliseni_okna[0] / 9600 * self.delta_cas * 0.48 / 2

        hrac.sirka = int(hrac.doopravdycka_sirka)
        hrac.vyska = int(hrac.doopravdycka_vyska)