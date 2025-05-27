import pygame as pg

pg.init()

class Tlacitko:
    def __init__(self, rozliseni_okna, x, y, sirka, vyska, text = '', level = -1, barva = (255, 255, 255), barva_textu = (0, 0, 0), font = None):
        self.x = x
        self.y = y

        self.text = text

        self.level = level

        self.sirka = sirka
        self.vyska = vyska

        self.barva = barva
        self.barva_textu = barva_textu

        if font == None:
            self.font = pg.font.SysFont('Arial', int(rozliseni_okna[0] / 64))

        else:
            self.font = font

        self.obdelnik = pg.Rect(x, y, sirka, vyska)

        self.text_font = self.font.render(self.text, True, self.barva_textu)
        self.text_rect = self.text_font.get_rect(center = self.obdelnik.center)

    def zmacknuti(self, pozice_mys):
        return self.obdelnik.collidepoint(pozice_mys) and pg.mouse.get_pressed()[0]

    def nakresly(self, okno):

        pg.draw.rect(okno, self.barva, self.obdelnik)

        self.font.render(self.text, True, self.barva_textu)
        okno.blit(self.text_font, self.text_rect)