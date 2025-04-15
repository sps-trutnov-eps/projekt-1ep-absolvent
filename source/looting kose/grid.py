import pygame
import random
import sys
from itemy import Itemy

#itemy = bobek, ohryzek, kebab, noviny, lahev, krabicak, hodinky, tuzemak, energetak, derava_cepice, derave_tricko, derave_kalhoty, pizza, burger

#okno
okraje = 20

rozliseni_x = 300 + 2*okraje
rozliseni_y = rozliseni_x

okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))

#class aktivace
item = Itemy(okno)

#item choosing system
itemy = ['bobek', "ohryzek", "kebab", "noviny", "lahev", "krabicak", "hodinky", "tuzemak", "energetak", "derava_cepice", "derave_tricko", "derave_kalhoty", "pizza", "burger"]
itemy_v_kosi = []

vybrane_itemy = 0
while vybrane_itemy < 9:
    vybrany_item = random.choice(itemy)

    itemy_v_kosi.append(vybrany_item)
    itemy.remove(vybrany_item)

    vybrane_itemy += 1

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
bila = (255, 255, 255)

#grid properties
velikost_ctverecku = 93 + 1/3
gap = 10
velikost_gridu = 3

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

while True:
    lmb = False

    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if udalost.type == pygame.MOUSEBUTTONDOWN and udalost.button == 1:
            lmb = True

    mys = pygame.mouse.get_pos()

    #print(lmb)

    okno.fill(bila)

    slot_1_r = pygame.Rect(row_1, col_1, velikost_ctverecku, velikost_ctverecku)
    slot_2_r = pygame.Rect(row_2, col_1, velikost_ctverecku, velikost_ctverecku)
    slot_3_r = pygame.Rect(row_3, col_1, velikost_ctverecku, velikost_ctverecku)

    slot_4_r = pygame.Rect(row_1, col_2, velikost_ctverecku, velikost_ctverecku)
    slot_5_r = pygame.Rect(row_2, col_2, velikost_ctverecku, velikost_ctverecku)
    slot_6_r = pygame.Rect(row_3, col_2, velikost_ctverecku, velikost_ctverecku)
    
    slot_7_r = pygame.Rect(row_1, col_3, velikost_ctverecku, velikost_ctverecku)
    slot_8_r = pygame.Rect(row_2, col_3, velikost_ctverecku, velikost_ctverecku)
    slot_9_r = pygame.Rect(row_3, col_3, velikost_ctverecku, velikost_ctverecku)

    slot_1 = pygame.draw.rect(okno, cerna, slot_1_r)
    slot_2 = pygame.draw.rect(okno, cerna, slot_2_r)
    slot_3 = pygame.draw.rect(okno, cerna, slot_3_r)

    slot_4 = pygame.draw.rect(okno, cerna, slot_4_r)
    slot_5 = pygame.draw.rect(okno, cerna, slot_5_r)
    slot_6 = pygame.draw.rect(okno, cerna, slot_6_r)

    slot_7 = pygame.draw.rect(okno, cerna, slot_7_r)
    slot_8 = pygame.draw.rect(okno, cerna, slot_8_r)
    slot_9 = pygame.draw.rect(okno, cerna, slot_9_r)

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

    pygame.display.flip()