import pygame

from mesta.mapa.hrac import Hrac
from mesta.mapa.mesto import *
from mesta.mapa.mista_inicializace import *

import nastaveni.main as Nastaveni
import inventory.main as Inventory

from master import convertFuncToStr as novyProgram

def ulozitData(global_data, not_global_data):
    global_data['x'] = not_global_data['x']
    global_data['y'] = not_global_data['y']

def main(global_data):
    nastaveni = dict(global_data['nastaveni'])

    vlajky = pygame.SCALED | pygame.HWSURFACE | pygame.DOUBLEBUF

    velikost_okna = (1920, 1080) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna, vlajky) # vytvori okno

    pygame.display.set_caption("Absolvent") # nastavy nazev okna

    rozmery_hrace = (velikost_okna[0] // (128 / 3), velikost_okna[1] // 13.5)

    # .convert_alpha() kdyz pouziva alpha
    textury_hrac = [
        pygame.image.load("textury\\hrac\\temp.png").convert(),   # textura otocenej nahoru
        pygame.image.load("textury\\hrac\\temp.png").convert(),   # textura otocenej dolu
        pygame.image.load("textury\\hrac\\temp.png").convert(),   # textura otocenej doleva
        pygame.image.load("textury\\hrac\\temp.png").convert()    # textura otocenej doprava
    ]

    hrac = Hrac(0 if global_data['hrac']['x'] == 0 else velikost_okna[0] // (1920 / global_data['hrac']['x']),
                0 if global_data['hrac']['x'] == 0 else velikost_okna[1] // (1080 / global_data['hrac']['y']),
                rozmery_hrace[0], rozmery_hrace[1], velikost_okna[0] // 192, velikost_okna[1] // 108, textury = textury_hrac) # vytvori postavu ve stredu obrazovky
    # pozice hrace je levej horni roh obrazku

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    budovy, interakcni_zony, velikost_mapy, offset = mesto3Init(okno, velikost_okna, global_data)

    ulozit_hru = False

    # main smycka
    programova_smycka = True
    while programova_smycka:
        fps = hodiny.get_fps()

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        # kontrola udalosti
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

        if novyProgram(Nastaveni.main) in global_data['aktualni_okna']:
            nastaveni = dict(global_data['nastaveni'])

        else:
            # otevre nastaveni
            if klice[nastaveni['exit']]:
                global_data['otevrena_okna'].append(novyProgram(Nastaveni.main))

        if not ('inventory' in global_data['aktualni_okna']):
            if klice[nastaveni['inventory']]:
                global_data['otevrena_okna'].append(novyProgram(Inventory.main))

        if global_data['konec']:
            programova_smycka = False

        if klice[pygame.K_g]:                                   ####################################### SMAZAT
            global_data['otevrena_okna'].append('mesto_1')      ####################################### SMAZAT

        if klice[pygame.K_h]:                                   ####################################### SMAZAT
            ulozit_hru = True                                   ####################################### SMAZAT
            ulozitData(global_data, {"x": hrac.x, "y": hrac.y}) ####################################### SMAZAT
            global_data['ulozit'] = True                        ####################################### SMAZAT

        if klice[pygame.K_r]:                                   ####################################### SMAZAT
            global_data['reset'] = True                         ####################################### SMAZAT


        veMeste(okno, velikost_okna, hrac, budovy, interakcni_zony, velikost_mapy, offset, nastaveni)
        if ulozit_hru:
            global_data['hrac']['x'] = hrac.x                   # PREMISTIT NA MISTO UKLADANI
            global_data['hrac']['y'] = hrac.y                   # PREMISTIT NA MISTO UKLADANI

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps
