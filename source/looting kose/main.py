import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

# sem piste importy
import pygame
import random
import sys
from itemy import Item
from itemy import textury
from slot import Slot

def main(global_data):
    #itemy = bobek, ohryzek, kebab, noviny, lahev, krabicak, hodinky, tuzemak, energetak, derava_cepice, derave_tricko, derave_kalhoty, pizza, burger

    #barvicky
    cerna = (0, 0, 0)
    transparent_gray = pygame.Color(143, 133, 125, 110)

    #grid properties
    velikost_ctverecku = 93 + 1/3
    gap = 10

    open_slots = [False] * 9
    last_frame_pressed = [False] * 9

    fps_casovac = pygame.time.Clock()
    fps = 60

    #okno
    okraje = 20

    rozliseni_x = 300 + 2*okraje
    rozliseni_y = rozliseni_x

    okno = pygame.display.set_mode((rozliseni_x, rozliseni_y), pygame.SRCALPHA)
    pygame.display.set_caption("Looting koše")
    bg = pygame.image.load("source//textury//Minigame_bg.png")


    pocet_itemu = 9
    pocet_bobku = random.randint(1, 2)

    row_1 = okraje
    row_2 = okraje + velikost_ctverecku + gap
    row_3 = okraje + 2 * velikost_ctverecku + 2 * gap

    col_1 = okraje
    col_2 = okraje + velikost_ctverecku + gap
    col_3 = okraje + 2 * velikost_ctverecku + 2 * gap


    slot_positions = [
        (row_1, col_1),
        (row_2, col_1),
        (row_3, col_1),
        (row_1, col_2),
        (row_2, col_2),
        (row_3, col_2),
        (row_1, col_3),
        (row_2, col_3),
        (row_3, col_3)
    ]

    #item choosing system
    itemy_v_kosi = []
    
    for i in range(pocet_itemu):
        item_nazev = random.choice(list(textury))
        itemy_v_kosi.append(Item(textury[item_nazev], slot_positions[i], item_nazev))


    sloty = []

    for i in range(len(slot_positions)):
        sloty.append(Slot(slot_positions[i][0], slot_positions[i][1], velikost_ctverecku, velikost_ctverecku, transparent_gray))

    x = 0

    main_loop = True
    while main_loop:
        lmb = False

        if len(global_data['inventory'][x]) >= global_data['inventory_xy'][1]:
            x += 1

        udalosti = pygame.event.get()
        for udalost in udalosti:
            if udalost.type == pygame.QUIT:
                main_loop = False

            if udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:
                lmb = True

        fps_casovac.tick(fps)

        mys = pygame.mouse.get_pos()

        #print(lmb)

        okno.fill(cerna)
        okno.blit(bg, (0, 0))

        #povrch = pygame.Surface()

        slot_1_r = pygame.Rect(row_1, col_1, velikost_ctverecku, velikost_ctverecku)
        slot_2_r = pygame.Rect(row_2, col_1, velikost_ctverecku, velikost_ctverecku)
        slot_3_r = pygame.Rect(row_3, col_1, velikost_ctverecku, velikost_ctverecku)

        slot_4_r = pygame.Rect(row_1, col_2, velikost_ctverecku, velikost_ctverecku)
        slot_5_r = pygame.Rect(row_2, col_2, velikost_ctverecku, velikost_ctverecku)
        slot_6_r = pygame.Rect(row_3, col_2, velikost_ctverecku, velikost_ctverecku)
        
        slot_7_r = pygame.Rect(row_1, col_3, velikost_ctverecku, velikost_ctverecku)
        slot_8_r = pygame.Rect(row_2, col_3, velikost_ctverecku, velikost_ctverecku)
        slot_9_r = pygame.Rect(row_3, col_3, velikost_ctverecku, velikost_ctverecku)
      
        slot_rects = [
            slot_1_r, slot_2_r, slot_3_r,
            slot_4_r, slot_5_r, slot_6_r,
            slot_7_r, slot_8_r, slot_9_r
        ]

        for slot in sloty:
            slot.vykresli(okno)

        for i, rect in enumerate(slot_rects):
            if lmb and rect.collidepoint(mys):
                if not last_frame_pressed[i]:
                    open_slots[i] = not open_slots[i]
                    last_frame_pressed[i] = True

                    if itemy_v_kosi[i].nazev != 'bobek':
                        global_data['inventory'][x].append(itemy_v_kosi[i].nazev)

        print(global_data['inventory'])

        # Draw each item if its slot is open
        for i, is_open in enumerate(open_slots):
            if is_open:
                itemy_v_kosi[i].vykresli(okno)

                if itemy_v_kosi[i].textura == textury["bobek"]:
                    global_data["nasel_bobek"] = True
                    return 0

        pygame.display.flip()
        # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"

    global_data['ulozit'] = True

if __name__ == "__main__":
    masterFunc(novyProgram(main))