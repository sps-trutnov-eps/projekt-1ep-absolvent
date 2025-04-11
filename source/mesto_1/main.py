import pygame

from hrac import Hrac
from mapa.mesto import *

def main():
    velikost_okna = (960, 540) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna) # vytvori okno

    pygame.display.set_caption("Jaroslav NoHouse") # nastavy nazev okna

    rozmery_hrace = (velikost_okna[0] // 36, velikost_okna[1] // 18)

    hrac = Hrac(okno, velikost_okna, velikost_okna[0] // 2, velikost_okna[1] // 2, rozmery_hrace[0], rozmery_hrace[1], velikost_okna[0] // 192, velikost_okna[1] // 108, barva = (255, 0, 0)) #, x = velikost_okna[0] // 2, y = velikost_okna[1] // 2) # vyroby postavu ve stredu obrazovky
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

        veMeste(okno, velikost_okna, hrac, budovy, velikost_mapy, offset)

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps

if __name__ == "__main__":
    main()
