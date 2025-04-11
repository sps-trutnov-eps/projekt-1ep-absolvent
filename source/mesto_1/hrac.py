import pygame

class Hrac:
    def __init__(self, okno, velikost_okna, pozice_x, pozice_y, sirka, vyska, chodici_rychlost_x, chodici_rychlost_y, x = 0, y = 0, barva = (255, 255, 255), rychlost_x = 0, rychlost_y = 0, je_nazemi = False):
        self.okno = okno # okno na ktery se bude kreslit
        self.velikost_okna = velikost_okna # rozliseni okna (sirka, vyska) neboli (x, y)

        self.barva = barva # barva hrace pozdeji se vymeni za obrazek

        # misto v mape
        self.x = x
        self.y = y

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

    def nakresli(self, offset = [0, 0]):
        pygame.draw.rect(self.okno, self.barva, (self.x + offset[0], self.y + offset[1], self.sirka, self.vyska))

    def pohni(self, jen_xy = 0):

        if jen_xy == 1:
            self.x += self.rychlost_x
            self.x += self.rychlost_x

            # zabrani hraci jit mimo obrazovku
            self.x = max(self.x, 0)
            self.x = min(self.x, self.velikost_okna[0] - self.sirka)

        elif jen_xy == 2:
            self.y += self.rychlost_y
            self.y += self.rychlost_y

            # zabrani hraci jit mimo obrazovku
            self.y = max(self.y, 0)
            self.y = min(self.y, self.velikost_okna[1] - self.vyska)

        else:
            self.x += self.rychlost_x
            self.y += self.rychlost_y

            # zabrani hraci jit mimo obrazovku
            self.x = max(self.x, 0)
            self.x = min(self.x, self.velikost_okna[0] - self.sirka)

            self.y = max(self.y, 0)
            self.y = min(self.y, self.velikost_okna[1] - self.vyska)
