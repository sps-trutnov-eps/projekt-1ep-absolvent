import pygame

import inventory.item

from main import focusWindow

def main(global_data):

    velikost_okna = (400, 400) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna) # vytvori okno

    pygame.display.set_caption("Inventář") # nastavy nazev okna

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

        if global_data['focus_inventory']:
            global_data['focus_inventory'] = False
            focusWindow()

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        if global_data['konec']:
            programova_smycka = False

        if klice[global_data['nastaveni']['exit']] or klice[global_data['nastaveni']['inventory']]:
            programova_smycka = False

        okno.fill((0, 0, 0)) # vybarvy okno aby se resetovalo

        ########################################################################### NAKRESLI GRID

        for item in global_data['inventory']:
            item.nakresli(okno, velikost_okna)

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps



    global_data['aktualni_okna'].remove('inventory') # Ulozi informaci ze okno je zavreny