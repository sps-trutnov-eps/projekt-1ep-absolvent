import pygame
from math import *
from hrac import Hrac
from mapa.budova import Budova

def mestoInicializace(okno, velikost_okna):
    velikost_mapy = pygame.Rect(0, 0, velikost_okna[0] * 4, velikost_okna[1] * 4)

    velikost_okna = okno.get_size()

    # vytvori budovy
    budovy = []

    budovy.append(Budova(okno, velikost_okna[0] * 2, velikost_okna[1], 3 * velikost_okna[0] / 7, velikost_okna[1] / 5, (255, 255, 255)))

    budovy.append(Budova(okno, velikost_okna[0] / 96, velikost_okna[1] / 54, 3 * velikost_okna[0] / 7, velikost_okna[1] / 5, (255, 255, 255)))
    budovy.append(Budova(okno, velikost_okna[0] - velikost_okna[0] / 96 - 3 * velikost_okna[0] / 7, velikost_okna[1] / 54, 3 * velikost_okna[0] / 7, velikost_okna[1] / 5, (255, 255, 255)))
    budovy.append(Budova(okno, velikost_okna[0] / 96, 2 * velikost_okna[1] / 54 + velikost_okna[1] / 5, velikost_okna[0] / 7, velikost_okna[1] / 5, (255, 255, 255)))
    budovy.append(Budova(okno, velikost_okna[0] - velikost_okna[0] / 96 - velikost_okna[0] / 7, 2 * velikost_okna[1] / 54 + velikost_okna[1] / 5, velikost_okna[0] / 7, velikost_okna[1] / 5, (255, 255, 255)))
    budovy.append(Budova(okno, velikost_okna[0] - velikost_okna[0] / 96 - velikost_okna[0] / 4.5, velikost_okna[1] - velikost_okna[1] / 54 - velikost_okna[1] / 5, velikost_okna[0] / 4.5, velikost_okna[1] / 5, (255, 255, 255)))
    budovy.append(Budova(okno, velikost_okna[0] / 96, velikost_okna[1] - velikost_okna[1] / 5, 5 * velikost_okna[0] / 7, velikost_okna[1] / 5 - velikost_okna[1] / 54, (255, 255, 255)))

    return budovy, velikost_mapy, [0, 0]

def veMeste(okno, velikost_okna, hrac: Hrac, budovy, velikost_mapy: pygame.Rect, offset):

    klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

    hrac.rychlost_x = 0 # resetuje rychlost hrace
    hrac.rychlost_y = 0 # resetuje rychlost hrace

    # pohyb postavy
    if klice[pygame.K_w]:
        hrac.rychlost_y = -hrac.chodici_rychlost_y

    if klice[pygame.K_a]:
        hrac.rychlost_x = -hrac.chodici_rychlost_x

    if klice[pygame.K_s]:
        hrac.rychlost_y = hrac.chodici_rychlost_y

    if klice[pygame.K_d]:
        hrac.rychlost_x = hrac.chodici_rychlost_x

    if klice[pygame.K_s] and klice[pygame.K_w]:
        hrac.rychlost_y = 0

    if klice[pygame.K_a] and klice[pygame.K_d]:
        hrac.rychlost_x = 0

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

    if hrac.x - velikost_okna[0] // 2 > velikost_mapy.left and hrac.x + velikost_okna[0] // 2 + hrac.sirka < velikost_mapy.right:
        offset[0] = -hrac.x + velikost_okna[0] // 2

    if hrac.y - velikost_okna[1] // 2 > velikost_mapy.top and hrac.y + velikost_okna[1] // 2 + hrac.vyska < velikost_mapy.bottom:
        offset[1] = -hrac.y + velikost_okna[1] // 2

    for budova in budovy:
        budova.nakresli(okno, offset)

    hrac.nakresli(offset) # nakresli hrace
