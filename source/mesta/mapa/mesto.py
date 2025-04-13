import pygame
from math import *
from mesta.mapa.hrac import Hrac
from mesta.mapa.budova import Budova
from mesta.mapa.interakcni_zona import InterakcniZona

NAHORU  = 0
DOLU    = 1
DOLEVA  = 2
DOPRAVA = 3

def veMeste(okno, velikost_okna, hrac: Hrac, budovy, interakcni_zony, velikost_mapy: pygame.Rect, offset, nastaveni: dict):

    klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

    hrac.rychlost_x = 0 # resetuje rychlost hrace
    hrac.rychlost_y = 0 # resetuje rychlost hrace

    interaguje = False   # jestli hrac chce s necim interaktovat - "e" je zmacknute

    # pohyb postavy
    if klice[nastaveni['nahoru']]:
        hrac.rychlost_y = -hrac.chodici_rychlost_y
        hrac.smer_otoceni = NAHORU

    if klice[nastaveni['doleva']]:
        hrac.rychlost_x = -hrac.chodici_rychlost_x
        hrac.smer_otoceni = DOLEVA

    if klice[nastaveni['dolu']]:
        hrac.rychlost_y = hrac.chodici_rychlost_y
        hrac.smer_otoceni = DOLU

    if klice[nastaveni['doprava']]:
        hrac.rychlost_x = hrac.chodici_rychlost_x
        hrac.smer_otoceni = DOPRAVA

    if klice[nastaveni['dolu']] and klice[nastaveni['nahoru']]:
        hrac.rychlost_y = 0

    if klice[nastaveni['doleva']] and klice[nastaveni['doprava']]:
        hrac.rychlost_x = 0

    if klice[nastaveni['interakce']]:
        interaguje = True

    # zabrani hraci aby nechodil rychleji sikmo
    if hrac.rychlost_x != 0 and hrac.rychlost_y != 0:
        prepona = sqrt(hrac.rychlost_x**2 + hrac.rychlost_y**2) # vypocita preponu trojuhelniku o odvesen delky - hrac.rychlost_x a hrac.rychlost_y

        # nastavi rychlost hrace aby mel rychlost stejnou i kdyz jde sikmo
        hrac.rychlost_x /= prepona
        hrac.rychlost_y /= prepona

        hrac.rychlost_x *= hrac.chodici_rychlost_x
        hrac.rychlost_y *= hrac.chodici_rychlost_y

    okno.fill((0, 0, 0)) # vybarvy okno aby se resetovalo

    for budova in budovy:
        budova.hitbox(hrac)

    hrac.x += hrac.rychlost_x
    hrac.y += hrac.rychlost_y

    # kontrola kdyz hrac neni na strane mapy
    if hrac.x - velikost_okna[0] // 2 > velikost_mapy.left and hrac.x + velikost_okna[0] // 2 + hrac.sirka < velikost_mapy.right:
        offset[0] = -hrac.x + velikost_okna[0] // 2

    if hrac.y - velikost_okna[1] // 2 > velikost_mapy.top and hrac.y + velikost_okna[1] // 2 + hrac.vyska < velikost_mapy.bottom:
        offset[1] = -hrac.y + velikost_okna[1] // 2

    for budova in budovy:
        budova.nakresli(okno, offset) # nakresli budovy

    for zona in interakcni_zony:
        zona.interakce(hrac, interaguje)

    # zabrani hraci jit mimo mapu
    if hrac.x < velikost_mapy.left:
        hrac.x = velikost_mapy.left
    elif hrac.x > velikost_mapy.right - 2 * hrac.sirka :
        hrac.x = velikost_mapy.right - 2 * hrac.sirka

    if hrac.y < velikost_mapy.top:
        hrac.y = velikost_mapy.top
    elif hrac.y > velikost_mapy.bottom - 2 * hrac.vyska:
        hrac.y = velikost_mapy.bottom - 2 * hrac.vyska

    hrac.nakresli(okno, offset) # nakresli hrace
