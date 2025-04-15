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
from itemy import Itemy

def main(global_data):
        
    #itemy = bobek, ohryzek, kebab, noviny, lahev, krabicak, hodinky, tuzemak, energetak, derava_cepice, derave_tricko, derave_kalhoty, pizza, burger

    #okno
    okraje = 20

    rozliseni_x = 300 + 2*okraje
    rozliseni_y = rozliseni_x

    okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))
    pygame.display.set_caption("Looting koše")

    #class aktivace
    item = Itemy(okno)

    pocet_itemu = 9
    pocet_bobku = random.randint(1, 2)

    #item choosing system
    itemy = ["ohryzek", "kebab", "noviny", "lahev", "krabicak", "hodinky", "tuzemak", "energetak", "derava_cepice", "derave_tricko", "derave_kalhoty", "pizza", "burger"]
    bobek_sloty = random.sample(range(pocet_itemu), pocet_bobku)
    itemy_v_kosi = [None] * pocet_itemu

    for i in bobek_sloty:
        itemy_v_kosi[i] = "bobek"

    for i in range(pocet_itemu):
        if itemy_v_kosi[i] is None:
            vybrany_item = random.choice(itemy)
            itemy_v_kosi[i] = vybrany_item
            itemy.remove(vybrany_item)

    print(itemy_v_kosi)

    #priradit cislum itemy
    real_itemy = {
        'bobek': item.bobek,
        "ohryzek": item.ohryzek,
        "kebab": item.kebab,
        "noviny": item.noviny,
        "lahev": item.lahev,
        "krabicak": item.krabicak,
        "hodinky": item.hodinky,
        "tuzemak": item.tuzemak,
        "energetak": item.energetak,
        "derava_cepice": item.cepice,
        "derave_tricko": item.tricko,
        "derave_kalhoty": item.kalhoty,
        "pizza": item.pizza,
        "burger": item.burger
    }

    #pozice radek a sloupec
    cerna = (0, 0, 0)

    #grid properties
    velikost_ctverecku = 93 + 1/3
    gap = 10

    row_1 = okraje
    row_2 = okraje + velikost_ctverecku + gap
    row_3 = okraje + 2 * velikost_ctverecku + 2 * gap

    col_1 = okraje
    col_2 = okraje + velikost_ctverecku + gap
    col_3 = okraje + 2 * velikost_ctverecku + 2 * gap

    last_frame_key_pressed_1 = False
    last_frame_key_pressed_2 = False
    last_frame_key_pressed_3 = False
    last_frame_key_pressed_4 = False
    last_frame_key_pressed_5 = False
    last_frame_key_pressed_6 = False
    last_frame_key_pressed_7 = False
    last_frame_key_pressed_8 = False
    last_frame_key_pressed_9 = False

    open_slot_1 = False
    open_slot_2 = False
    open_slot_3 = False
    open_slot_4 = False
    open_slot_5 = False
    open_slot_6 = False
    open_slot_7 = False
    open_slot_8 = False
    open_slot_9 = False

    color_timer = 0

    fps_casovac = pygame.time.Clock()
    fps = 60

    while True:
        lmb = False

        udalosti = pygame.event.get()
        for udalost in udalosti:
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:
                lmb = True

        fps_casovac.tick(fps)

        mys = pygame.mouse.get_pos()

        if color_timer > 0:
            color_timer -= 1

        if color_timer <= 0:
            barva_r = random.randint(0, 255)
            barva_g = random.randint(0, 255)
            barva_b = random.randint(0, 255)

            random_barva = (barva_r, barva_g, barva_b)
            color_timer = 15

        #print(lmb)

        okno.fill(cerna)

        slot_1_r = pygame.Rect(row_1, col_1, velikost_ctverecku, velikost_ctverecku)
        slot_2_r = pygame.Rect(row_2, col_1, velikost_ctverecku, velikost_ctverecku)
        slot_3_r = pygame.Rect(row_3, col_1, velikost_ctverecku, velikost_ctverecku)

        slot_4_r = pygame.Rect(row_1, col_2, velikost_ctverecku, velikost_ctverecku)
        slot_5_r = pygame.Rect(row_2, col_2, velikost_ctverecku, velikost_ctverecku)
        slot_6_r = pygame.Rect(row_3, col_2, velikost_ctverecku, velikost_ctverecku)
        
        slot_7_r = pygame.Rect(row_1, col_3, velikost_ctverecku, velikost_ctverecku)
        slot_8_r = pygame.Rect(row_2, col_3, velikost_ctverecku, velikost_ctverecku)
        slot_9_r = pygame.Rect(row_3, col_3, velikost_ctverecku, velikost_ctverecku)

        slot_1 = pygame.draw.rect(okno, random_barva, slot_1_r)
        slot_2 = pygame.draw.rect(okno, random_barva, slot_2_r)
        slot_3 = pygame.draw.rect(okno, random_barva, slot_3_r)

        slot_4 = pygame.draw.rect(okno, random_barva, slot_4_r)
        slot_5 = pygame.draw.rect(okno, random_barva, slot_5_r)
        slot_6 = pygame.draw.rect(okno, random_barva, slot_6_r)

        slot_7 = pygame.draw.rect(okno, random_barva, slot_7_r)
        slot_8 = pygame.draw.rect(okno, random_barva, slot_8_r)
        slot_9 = pygame.draw.rect(okno, random_barva, slot_9_r)

        if lmb and slot_1_r.collidepoint(mys):
            if not last_frame_key_pressed_1:
                open_slot_1 = not open_slot_1
                last_frame_key_pressed_1 = True

        if lmb and slot_2_r.collidepoint(mys):
            if not last_frame_key_pressed_2:
                open_slot_2 = not open_slot_2
                last_frame_key_pressed_2 = True

        if lmb and slot_3_r.collidepoint(mys):
            if not last_frame_key_pressed_3:
                open_slot_3 = not open_slot_3
                last_frame_key_pressed_3 = True

        if lmb and slot_4_r.collidepoint(mys):
            if not last_frame_key_pressed_4:
                open_slot_4 = not open_slot_4
                last_frame_key_pressed_4 = True

        if lmb and slot_5_r.collidepoint(mys):
            if not last_frame_key_pressed_5:
                open_slot_5 = not open_slot_5
                last_frame_key_pressed_5 = True

        if lmb and slot_6_r.collidepoint(mys):
            if not last_frame_key_pressed_6:
                open_slot_6 = not open_slot_6
                last_frame_key_pressed_6 = True

        if lmb and slot_7_r.collidepoint(mys):
            if not last_frame_key_pressed_7:
                open_slot_7 = not open_slot_7
                last_frame_key_pressed_7 = True

        if lmb and slot_8_r.collidepoint(mys):
            if not last_frame_key_pressed_8:
                open_slot_8 = not open_slot_8
                last_frame_key_pressed_8 = True

        if lmb and slot_9_r.collidepoint(mys):
            if not last_frame_key_pressed_9:
                open_slot_9 = not open_slot_9
                last_frame_key_pressed_9 = True

        # Slot positions
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

        # Slot open states
        open_slots = [
            open_slot_1, open_slot_2, open_slot_3,
            open_slot_4, open_slot_5, open_slot_6,
            open_slot_7, open_slot_8, open_slot_9
        ]

        # Draw each item if its slot is open
        for i, is_open in enumerate(open_slots):
            if is_open:
                item_name = itemy_v_kosi[i]
                draw_function = real_itemy[item_name]
                x, y = slot_positions[i]
                draw_function(x, y)
                draw_function.append(global_data["inventory"])

        pygame.display.flip()
        # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"

if __name__ == "__main__":
    masterFunc(novyProgram(main))