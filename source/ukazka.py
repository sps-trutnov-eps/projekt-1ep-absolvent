import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram


import pygame

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

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        if klice[global_data['nastaveni']['exit']] or klice[global_data['nastaveni']['inventory']]:
            programova_smycka = False

        okno.fill((0, 0, 0)) # vybarvy okno aby se resetovalo

        pygame.draw.rect(okno, (255, 255, 255), (100, 100, 100, 100))

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps

if __name__ == "__main__":
    masterFunc(novyProgram(main))
