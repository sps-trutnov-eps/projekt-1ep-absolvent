import pygame

class Hrac:
    def __init__(self, pozice_x, pozice_y, sirka, vyska, chodici_rychlost_x, chodici_rychlost_y, textury, barva_hitboxu = (255, 255, 255), rychlost_x = 0, rychlost_y = 0, je_nazemi = False, smer_otoceni = 1):
        self.barva = barva_hitboxu # barva hitboxu
        self.textury = textury

        self.smer_otoceni = smer_otoceni

        # misto v mape
        self.x = pozice_x
        self.y = pozice_y

        # rozmery postavy
        self.sirka = sirka
        self.vyska = vyska

        # o kolik se postava posouva danym smerem kazdy frame
        self.rychlost_x = rychlost_x
        self.rychlost_y = rychlost_y

        self.chodici_rychlost_x = chodici_rychlost_x # rychlost postavi kdyz chodi po ose x
        self.chodici_rychlost_y = chodici_rychlost_y # rychlost postavi kdyz chodi po ose y

        # kontrola aby postava mohla skakat jen kdyz je na zemi
        self.nazemi = je_nazemi

    def nakresli(self, okno, offset = [0, 0]):
        okno.blit(self.textury[self.smer_otoceni], (self.x + offset[0], self.y + offset[1]))

    def nakresliHitbox(self, okno, offset = [0, 0]):
        pygame.draw.rect(okno, self.barva, (self.x + offset[0], self.y + offset[1], self.sirka, self.vyska))
