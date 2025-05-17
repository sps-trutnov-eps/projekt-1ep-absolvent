import pygame
import os

from inventory.item import newItem

from master import focusWindow, moveWindow

def main(global_data):

    slot_size = (50, 50)
    slot_offset = (slot_size[0] // 5, slot_size[1] // 5)

    inventory_xy = list(global_data["inventory_xy"]).copy()
    itemy = list(global_data["inventory"]).copy()

    slot_image = pygame.image.load("textury/itemy/slot.png")

    vlajky = pygame.NOFRAME

    velikost_okna = ((slot_size[0] + slot_offset[0]) * inventory_xy[0] + slot_offset[0],
                     (slot_size[1] + slot_offset[1]) * inventory_xy[1] + slot_offset[1]) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna, vlajky) # vytvori okno

    pygame.display.set_caption("Inventář") # nastavy nazev okna

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    # Inicializace posouvani oken
    win_x, win_y = 100, 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{win_x},{win_y}"
    dragging = False
    mouse_offset = (0, 0)

    focusWindow()

    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti
        for udalost in pygame.event.get():
            dragging, mouse_offset = moveWindow(pygame.K_LALT, udalost, dragging, mouse_offset)

            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        if global_data['konec']:
            programova_smycka = False

        if klice[global_data['nastaveni']['exit']] or klice[global_data['nastaveni']['inventory']]:
            programova_smycka = False

        okno.fill((0, 0, 0)) # vybarvy okno aby se resetovalo

        for i in range(inventory_xy[0]):
            for j in range(inventory_xy[1]):
                okno.blit(slot_image, (slot_offset[0] + i * (slot_offset[0] + slot_size[0]),
                                       slot_offset[1] + j * (slot_offset[1] + slot_size[1])))

        for item in itemy:
            okno.blit(item["textura"], [item["x"], item["y"]])

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps
