import pygame

from mesta.mapa.budova import Budova
from mesta.mapa.interakcni_zona import InterakcniZona

def mesto1Init(okno, velikost_okna):
    velikost_mapy = pygame.Rect(0, 0, velikost_okna[0] * 4, velikost_okna[1] * 4)

    # vytvori budovy
    interakcni_zony = []

    interakcni_zony.append(InterakcniZona(500, 500, 500, 500, print, [2, 2]))

    textura = pygame.image.load("textury\\budovy\\temp.png").convert()
    # .convert_alpha() kdyz pouziva alpha

    budovy = []

    budovy.append(Budova(okno, velikost_okna[0] * 2, velikost_okna[1], 3 * velikost_okna[0] / 7, velikost_okna[1] / 5, textura))

    budovy.append(Budova(okno, velikost_okna[0] / 96, velikost_okna[1] / 54, 3 * velikost_okna[0] / 7, velikost_okna[1] / 5, textura))
    budovy.append(Budova(okno, velikost_okna[0] - velikost_okna[0] / 96 - 3 * velikost_okna[0] / 7, velikost_okna[1] / 54, 3 * velikost_okna[0] / 7, velikost_okna[1] / 5, textura))
    budovy.append(Budova(okno, velikost_okna[0] / 96, 2 * velikost_okna[1] / 54 + velikost_okna[1] / 5, velikost_okna[0] / 7, velikost_okna[1] / 5, textura))
    budovy.append(Budova(okno, velikost_okna[0] - velikost_okna[0] / 96 - velikost_okna[0] / 7, 2 * velikost_okna[1] / 54 + velikost_okna[1] / 5, velikost_okna[0] / 7, velikost_okna[1] / 5, textura))
    budovy.append(Budova(okno, velikost_okna[0] - velikost_okna[0] / 96 - velikost_okna[0] / 4.5, velikost_okna[1] - velikost_okna[1] / 54 - velikost_okna[1] / 5, velikost_okna[0] / 4.5, velikost_okna[1] / 5, textura))
    budovy.append(Budova(okno, velikost_okna[0] / 96, velikost_okna[1] - velikost_okna[1] / 5, 5 * velikost_okna[0] / 7, velikost_okna[1] / 5 - velikost_okna[1] / 54, textura))

    return budovy, interakcni_zony, velikost_mapy, [0, 0]
