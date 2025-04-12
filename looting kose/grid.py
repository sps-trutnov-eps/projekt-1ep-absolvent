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
itemy = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
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
    0: item.bobek,
    1: item.ohryzek,
    2: item.kebab,
    3: item.noviny,
    4: item.lahev,
    5: item.krabicak,
    6: item.hodinky,
    7: item.tuzemak,
    8: item.energetak,
    9: item.cepice,
    10: item.tricko,
    11: item.kalhoty,
    12: item.pizza,
    13: item.burger
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

col_1 = row_1
col_2 = row_2
col_3 = row_3

while True:
    lmb = False

    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if udalost.type == pygame.MOUSEBUTTONUP and udalost.button == 1:
            lmb = True

    mys = pygame.mouse.get_pos()

    #print(lmb)

    okno.fill(bila)

    slot_1_r = pygame.Rect(row_1, col_1, velikost_ctverecku, velikost_ctverecku)
    slot_2_r = pygame.Rect(row_1, col_2, velikost_ctverecku, velikost_ctverecku)
    slot_3_r = pygame.Rect(row_1, col_3, velikost_ctverecku, velikost_ctverecku)

    slot_4_r = pygame.Rect(row_2, col_1, velikost_ctverecku, velikost_ctverecku)
    slot_5_r = pygame.Rect(row_2, col_2, velikost_ctverecku, velikost_ctverecku)
    slot_6_r = pygame.Rect(row_2, col_3, velikost_ctverecku, velikost_ctverecku)
    
    slot_7_r = pygame.Rect(row_3, col_1, velikost_ctverecku, velikost_ctverecku)
    slot_8_r = pygame.Rect(row_3, col_1, velikost_ctverecku, velikost_ctverecku)
    slot_9_r = pygame.Rect(row_3, col_3, velikost_ctverecku, velikost_ctverecku)

    if not slot_1_r.collidepoint(mys) and not lmb:
        slot_1 = pygame.draw.rect(okno, cerna, slot_1_r)
    if not slot_2_r.collidepoint(mys) and not lmb:
        slot_2 = pygame.draw.rect(okno, cerna, slot_3_r)
    if not slot_3_r.collidepoint(mys) and not lmb:
        slot_3 = pygame.draw.rect(okno, cerna, slot_3_r)

    slot_4 = pygame.draw.rect(okno, cerna, slot_4_r)
    slot_5 = pygame.draw.rect(okno, cerna, slot_5_r)
    slot_6 = pygame.draw.rect(okno, cerna, slot_6_r)

    slot_7 = pygame.draw.rect(okno, cerna, slot_8_r)
    slot_8 = pygame.draw.rect(okno, cerna, slot_8_r)
    slot_9 = pygame.draw.rect(okno, cerna, slot_9_r)

    print(row_2, col_1)
    print(row_2, col_3)

    pygame.display.flip()