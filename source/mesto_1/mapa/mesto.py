import pygame
from math import *
from hrac import Hrac
from mapa.budova import Budova

def mestoInicializace(okno, velikost_okna):
    velikost_mapy = pygame.Rect(0, 0, velikost_okna[0] * 1.5, velikost_okna[1] * 1.5)

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

    return budovy, velikost_mapy

def veMeste(okno, hrac: Hrac, budovy, velikost_mapy: pygame.Rect):

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
        pygame.draw.rect(okno, budova.barva, budova.obdelnik)
        budova.hitbox(hrac)

    # posune budovy pro symulaci pohybu
    if hrac.true_y > velikost_mapy.top and hrac.true_y + hrac.vyska < velikost_mapy.bottom:
        for budova in budovy:
            budova.obdelnik.y -= hrac.rychlost_y

        hrac.true_y += hrac.rychlost_y
        hrac.rychlost_y = 0
    
    else:
        hrac.pohni(2)

    if hrac.true_x > velikost_mapy.left and hrac.true_x + hrac.sirka < velikost_mapy.right:
        for budova in budovy:
            budova.obdelnik.x -= hrac.rychlost_x

        hrac.true_x += hrac.rychlost_x
        hrac.rychlost_x = 0

    else:
        hrac.pohni(1)

    hrac.nakresli() # nakresli hrace

    print()
    print(hrac.true_x)
    print(hrac.true_y)
    print(velikost_mapy)