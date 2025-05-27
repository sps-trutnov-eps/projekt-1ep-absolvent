import pygame
import os

from master import focusWindow, moveWindow, convertFromManager

from inventory.item import newItem
from inventory.options import Options

def main(global_data):

    slot_size = (50, 50)
    slot_offset = (slot_size[0] // 5, slot_size[1] // 5)

    inventory_xy = list(global_data["inventory_xy"]).copy()
    itemy = convertFromManager(global_data["inventory"]).copy()

    itemy[0][0] = newItem(slot_offset[0], slot_offset[1], pygame.image.load("textury/itemy/temp.png"), "temp")

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

    options = Options(0, 0, None)

    focusWindow()

    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti
        mouse_pos = pygame.mouse.get_pos()
        for udalost in pygame.event.get():
            dragging, mouse_offset = moveWindow(global_data['nastaveni']['pohyb_oken'], udalost, dragging, mouse_offset)

            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

            if udalost.type == pygame.MOUSEBUTTONUP:
                for row in itemy:
                    for item in row:
                        item_rect = pygame.Rect(item['x'], item['y'], slot_size[0], slot_size[1])
                        if item_rect.collidepoint(mouse_pos):
                            options.item = item
                            options.x = mouse_pos[0]
                            options.y = mouse_pos[1]
                            options.nakresli(okno)

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
        for row in itemy:
            for item in row:
                okno.blit(item["textura"], (item["x"], item["y"]))

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps
