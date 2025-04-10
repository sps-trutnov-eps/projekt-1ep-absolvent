import pygame
import random
#from itemy import Itemy

#itemy = bobek, ohryzek, kebab, noviny, lahev, krabicak, hodinky, tuzemak, energetak, derava_cepice, derave_tricko, derave_kalhoty, pizza, burger

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

