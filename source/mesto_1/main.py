import pygame

import multiprocessing
from mesto_1.hrac import Hrac
from mesto_1.mapa.mesto import *

def main(global_data):
    velikost_okna = (1920, 1080) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna) # vytvori okno

    pygame.display.set_caption("Absolvent") # nastavy nazev okna

    rozmery_hrace = (velikost_okna[0] // (128 / 3), velikost_okna[1] // 13.5)

    hrac = Hrac(okno, velikost_okna, 0 if global_data['hrac']['x'] == 0 else 1920 // (1920 / global_data['hrac']['x']), 0 if global_data['hrac']['x'] == 0 else 1080 // (1080 / global_data['hrac']['y']), rozmery_hrace[0], rozmery_hrace[1], velikost_okna[0] // 192, velikost_okna[1] // 108, barva = (255, 0, 0)) # vyroby postavu ve stredu obrazovky
    # pozice hrace je levej horni roh obrazku

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    budovy, velikost_mapy, offset = mestoInicializace(okno, velikost_okna)

    # main smycka
    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        # ukonci hru kdyz se zmackne esc
        if klice[pygame.K_ESCAPE]:
            programova_smycka = False

        if klice[pygame.K_g]:
            global_data['otevrena_okna'].append('mesto_1')

        if klice[pygame.K_h]:
            global_data['ulozit'] = True

        veMeste(okno, velikost_okna, hrac, budovy, velikost_mapy, offset)
        global_data['hrac']['x'] = hrac.x
        global_data['hrac']['y'] = hrac.y

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps
 
    print(global_data['aktualni_okna'])
    global_data['aktualni_okna'].remove('mesto_1')
    print(global_data['aktualni_okna'])

if __name__ == "__main__":
    main({
        "otevrena_okna": ["mesto_1"],
        "konec": False,
        "ulozit": False,
        "penize": 0,
        "hrac": {
            "x": 960,
            "y": 540
        }
    }
)
