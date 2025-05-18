import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

import pygame
import os
from master import moveWindow, focusWindow

from slot import Slot

def main(global_data):

    vlajky = pygame.NOFRAME

    velikost_okna = (500, 500) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna, vlajky) # vytvori okno

    pygame.display.set_caption("shop") # nastavy nazev okna

    win_x, win_y = 100, 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{win_x},{win_y}"
    dragging = False
    mouse_offset = (0, 0)

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    slots = []

    slots.append(Slot)

    focusWindow()

    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

            dragging, mouse_offset = moveWindow(global_data['nastaveni']['pohyb_oken'], udalost, dragging, mouse_offset)

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        if klice[global_data['nastaveni']['exit']]:
            programova_smycka = False

        okno.fill((0, 0, 0)) # vybarvy okno aby se resetovalo


        for slot in slots:
            slot.nakresli(okno)


        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps

if __name__ == "__main__":
    masterFunc(novyProgram(main))
