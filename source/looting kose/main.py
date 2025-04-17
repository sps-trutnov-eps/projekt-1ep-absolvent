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
from slot import Slot

def main(global_data):
    #itemy = bobek, ohryzek, kebab, noviny, lahev, krabicak, hodinky, tuzemak, energetak, derava_cepice, derave_tricko, derave_kalhoty, pizza, burger

    #okno
    okraje = 20

    rozliseni_x = 300 + 2*okraje
    rozliseni_y = rozliseni_x

    okno = pygame.display.set_mode((rozliseni_x, rozliseni_y), pygame.SRCALPHA)
    pygame.display.set_caption("Looting koše")
    bg = pygame.image.load("source//textury//Minigame_bg.png")

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

    #barvicky
    cerna = (0, 0, 0)
    transparent_gray = pygame.Color(143, 133, 125, 110)

    #grid properties
    velikost_ctverecku = 93 + 1/3
    gap = 10

    row_1 = okraje
    row_2 = okraje + velikost_ctverecku + gap
    row_3 = okraje + 2 * velikost_ctverecku + 2 * gap

    col_1 = okraje
    col_2 = okraje + velikost_ctverecku + gap
    col_3 = okraje + 2 * velikost_ctverecku + 2 * gap

    open_slots = [False] * 9
    last_frame_pressed = [False] * 9

    fps_casovac = pygame.time.Clock()
    fps = 60

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

    sloty = []

    for i in range(len(slot_positions)):
        sloty.append(Slot(slot_positions[i][0], slot_positions[i][1], velikost_ctverecku, velikost_ctverecku, transparent_gray))

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

        # Draw each item if its slot is open
        for i, is_open in enumerate(open_slots):
            if is_open:
                item_name = itemy_v_kosi[i]
                draw_function = real_itemy[item_name]
                x, y = slot_positions[i]
                draw_function(x, y)

                if item_name == "bobek":
                    global_data["nasel_bobek"] = True
                    return 0

        pygame.display.flip()
        # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"

if __name__ == "__main__":
    masterFunc(novyProgram(main))