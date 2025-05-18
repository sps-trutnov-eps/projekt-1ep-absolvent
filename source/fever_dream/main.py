import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import convertFuncToStr as novyProgram, main as masterFunc, moveWindow, focusWindow

import pygame
import os

from itertools import combinations

from okraj import Okraj
from item  import *

def main(global_data):

    pygame.font.init()
    pygame.mixer.init()

    vlajky = pygame.NOFRAME

    velikost_okna = (500, 500) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna, vlajky) # vytvori okno

    pygame.display.set_caption("Minihra") # nastavy nazev okna

    win_x, win_y = 100, 100
    os.environ['SDL_VIDEO_WINDOW_POS'] = f"{win_x},{win_y}"
    dragging = False
    mouse_offset = (0, 0)

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    focusWindow()

    kreslene_objekty = []

    kreslene_objekty.append(Okraj(40,  385, 50, 50))
    kreslene_objekty.append(Okraj(155, 385, 50, 50))
    kreslene_objekty.append(Okraj(270, 385, 50, 50))
    kreslene_objekty.append(Okraj(385, 385, 50, 50))

    kreslene_objekty.append(Okraj(120, 60,  100, 100))
    kreslene_objekty.append(Okraj(280, 220, 100, 100))
    kreslene_objekty.append(Okraj(280, 60,  100, 100))
    kreslene_objekty.append(Okraj(120, 220, 100, 100))

#    kreslene_objekty.append(Cara((220, 110), (280, 110)))
#    kreslene_objekty.append(Cara((220, 270), (280, 270)))
#    kreslene_objekty.append(Cara((170, 160), (170, 220)))
#    kreslene_objekty.append(Cara((330, 160), (330, 220)))

    itemy = []

    for i in range(4):
        itemy.append(newItem(i))

    sloty = []

    sloty.append(pygame.Rect(120, 60,  50, 50))
    sloty.append(pygame.Rect(170, 60,  50, 50))
    sloty.append(pygame.Rect(170, 110, 50, 50))
    sloty.append(pygame.Rect(120, 110, 50, 50))
 
    sloty.append(pygame.Rect(280, 220, 50, 50))
    sloty.append(pygame.Rect(330, 220, 50, 50))
    sloty.append(pygame.Rect(330, 270, 50, 50))
    sloty.append(pygame.Rect(280, 270, 50, 50))

    sloty.append(pygame.Rect(280, 60,  50, 50))
    sloty.append(pygame.Rect(330, 60,  50, 50))
    sloty.append(pygame.Rect(330, 110, 50, 50))
    sloty.append(pygame.Rect(280, 110, 50, 50))

    sloty.append(pygame.Rect(120, 220, 50, 50))
    sloty.append(pygame.Rect(170, 220, 50, 50))
    sloty.append(pygame.Rect(170, 270, 50, 50))
    sloty.append(pygame.Rect(120, 270, 50, 50))

    drzi = -1

    plnost_sloty = [[-1, -1, -1, -1],
                    [-1, -1, -1, -1],
                    [-1, -1, -1, -1],
                    [-1, -1, -1, -1]]

    score = 0

    score_size = 1
    font = pygame.font.SysFont('Arial', 20)
    score_font = pygame.font.SysFont('Arial', 20)
    score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
    score_original_size = score_text.get_size()
    score_font = pygame.font.SysFont('Arial', 100)

    overlay_alpha = 0
    overlay = pygame.Surface((500, 500))
    overlay.set_alpha(overlay_alpha)
    overlay.fill(0x000000)

    konec = False
    multiplier = 1
    score_cords = (10, 10)

    combo_sound_path = os.path.join("zvuky", "combo.wav")
    combo_sound = pygame.mixer.Sound(combo_sound_path)

    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti

        mouse_buttons = pygame.mouse.get_pressed()
        mouse_pos = pygame.mouse.get_pos()

        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

            dragging, mouse_offset = moveWindow(global_data['nastaveni']['pohyb_oken'], udalost, dragging, mouse_offset)

        klice = pygame.key.get_pressed() # kontrola zmacknuti tlacitek drzenim tlacitka se opaku udalost

        if klice[global_data['nastaveni']['exit']]:
            programova_smycka = False

        okno.fill((0, 0, 0)) # vybarvy okno aby se resetovalo

        for objekt in kreslene_objekty:
            objekt.nakresli(okno)

        moved_item = False
        for i, item in enumerate(itemy.copy()):
            item.nakresli(okno)

            if not konec:
                if mouse_buttons[0] and item.start_pozice[1] >= 385 and ((item.colize((mouse_pos)) and drzi == -1) or drzi == i):

                    collided = True
                    for j, slot in enumerate(sloty):
                        if slot.collidepoint(*mouse_pos):
                            item.x = slot.x
                            item.y = slot.y

                            collided = False
                            break

                    if collided:
                        item.x += mouse_pos[0] - item.pozice[0]
                        item.y += mouse_pos[1] - item.pozice[1]

                    drzi = i

                elif item.start_pozice[1] >= 385:
                    for j, slot in enumerate(sloty):
                        if item.x == slot.x and item.y == slot.y and plnost_sloty[j//4][j%4] == -1:
                            plnost_sloty[j//4][j%4] = item
                            itemy.append(newItem((item.start_pozice[0] - 40) // 115))
                            moved_item = True
                            item.start_pozice = (slot.x, slot.y)

                if not (mouse_buttons[0] and item.start_pozice[1] >= 385 and ((item.colize((mouse_pos)) and drzi == -1) or drzi == i)):
                    item.x = item.start_pozice[0]
                    item.y = item.start_pozice[1]

            item.pozice = mouse_pos

        if not mouse_buttons[0] or konec:
            drzi = -1

        temp_itemy = itemy.copy()


        if moved_item and not konec:
            temp_multiplier = multiplier
            for slot in plnost_sloty:

                for x, y, z, w in combinations(slot, 4):
                    if x != -1 and y != -1 and z != -1 and w != -1:
                        suma = tuple(a + b + c + d for a, b, c, d in zip(x.seznam, y.seznam, z.seznam, w.seznam))
                        if suma == (1, 1, 1, 1) or (x.barva == y.barva == z.barva == w.barva):
                            try:
                                if suma == (1, 1, 1, 1):
                                    if x.barva == y.barva == z.barva == w.barva:
                                        multiplier *= 5

                                    score += multiplier * 10
                                    multiplier *= 10

                                else:
                                    multiplier *= 8
                                    score += multiplier

                                slot[slot.index(w)] = -1 if w in slot else w
                                temp_itemy.remove(w)
                                slot[slot.index(z)] = -1 if z in slot else z
                                temp_itemy.remove(z)
                                slot[slot.index(y)] = -1 if y in slot else y
                                temp_itemy.remove(y)
                                slot[slot.index(x)] = -1 if x in slot else x
                                temp_itemy.remove(x)

                            except:
                                pass

                for x, y, z in combinations(slot, 3):
                    if x != -1 and y != -1 and z != -1:
                        suma = tuple(a + b + c for a, b, c in zip(x.seznam, y.seznam, z.seznam))
                        if suma == (1, 1, 1, 1):
                            try:
                                if x.barva == y.barva == z.barva:
                                    multiplier *= 3

                                score += multiplier * 4
                                multiplier *= 4

                                slot[slot.index(z)] = -1 if z in slot else z
                                temp_itemy.remove(z)
                                slot[slot.index(y)] = -1 if y in slot else y
                                temp_itemy.remove(y)
                                slot[slot.index(x)] = -1 if x in slot else x
                                temp_itemy.remove(x)

                            except:
                                pass

                for x, y in combinations(slot, 2):
                    if x != -1 and y != -1:
                        suma = tuple(a + b for a, b in zip(x.seznam, y.seznam))
                        if suma == (1, 1, 1, 1) or (x.seznam == y.seznam and x.barva == y.barva):
                            try:
                                if x.barva == y.barva and x.seznam != y.seznam:
                                    multiplier *= 2

                                score += multiplier * 2
                                multiplier *= 2

                                slot[slot.index(y)] = -1 if y in slot else y
                                temp_itemy.remove(y)
                                slot[slot.index(x)] = -1 if x in slot else x
                                temp_itemy.remove(x)

                            except:
                                pass

            if temp_multiplier == multiplier:
                multiplier //= 4
                multiplier = max(1, multiplier)

            else:
                combo_sound.play()

        konec = not any(-1 in slot for slot in plnost_sloty)

        itemy = temp_itemy.copy()

        okno.blit(font.render(f"Combo: {multiplier}x", True, (255, 255, 255)), (10, 35))

        if konec:
            if score_cords[0] < 250 - score_text.get_width() // 2:
                score_size += 0.01
                score_cords = (score_cords[0]+1, score_cords[1]+1.2)

                overlay_alpha += 2
                overlay.set_alpha(overlay_alpha)

            okno.blit(overlay, (0, 0))

        else:
            score_font = pygame.font.SysFont('Arial', 20)
            score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
            score_original_size = score_text.get_size()
            score_font = pygame.font.SysFont('Arial', 100)

        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255))
        score_text = pygame.transform.smoothscale(score_text, (score_original_size[0] * score_size, score_original_size[1] * score_size))

        okno.blit(score_text, score_cords)

        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps

if __name__ == "__main__":
    masterFunc(novyProgram(main))
