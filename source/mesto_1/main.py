import pygame
import ctypes

from mesto_1.hrac import Hrac
from mesto_1.mapa.mesto import *
from main import unfocusWindow

def main(global_data):
    velikost_okna = (1920, 1080) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna) # vytvori okno

    pygame.display.set_caption("Absolvent") # nastavy nazev okna

    rozmery_hrace = (velikost_okna[0] // (128 / 3), velikost_okna[1] // 13.5)

    hrac = Hrac(okno, velikost_okna,
                0 if global_data['hrac']['x'] == 0 else velikost_okna[0] // (1920 / global_data['hrac']['x']),
                0 if global_data['hrac']['x'] == 0 else velikost_okna[1] // (1080 / global_data['hrac']['y']),
                rozmery_hrace[0], rozmery_hrace[1], velikost_okna[0] // 192, velikost_okna[1] // 108, barva = (255, 0, 0)) # vytvori postavu ve stredu obrazovky
    # pozice hrace je levej horni roh obrazku

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    budovy, interakcni_zony, velikost_mapy, offset = mestoInicializace(okno, velikost_okna)

    # main smycka
    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

        if pygame.display.get_active() and "settings" in global_data['aktualni_okna']:
            unfocusWindow()
            global_data['focus_nastaveni'] = True

        if pygame.display.get_active() and "inventory" in global_data['aktualni_okna']:
            unfocusWindow()
            global_data['focus_inventory'] = True

        if global_data['konec']:
            programova_smycka = False

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        # ukonci hru kdyz se zmackne esc
        if klice[global_data['nastaveni']['exit']] and not ('settings' in global_data['aktualni_okna']):
            global_data['otevrena_okna'].append('settings')

        if klice[global_data['nastaveni']['inventory']] and not ('inventory' in global_data['aktualni_okna']):
            global_data['otevrena_okna'].append('inventory')

        if klice[pygame.K_g]:                                   ####################################### SMAZAT
            global_data['otevrena_okna'].append('mesto_1')      ####################################### SMAZAT

        if klice[pygame.K_h]:                                   ####################################### SMAZAT
            global_data['ulozit'] = True                        ####################################### SMAZAT

        if klice[pygame.K_r]:                                   ####################################### SMAZAT
            global_data['reset'] = True                         ####################################### SMAZAT

        veMeste(okno, velikost_okna, hrac, budovy, interakcni_zony, velikost_mapy, offset, global_data)

        global_data['hrac']['x'] = hrac.x
        global_data['hrac']['y'] = hrac.y

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps

    global_data['aktualni_okna'].remove('mesto_1') # Ulozi informaci ze okno je zavreny
