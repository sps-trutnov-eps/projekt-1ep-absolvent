import pygame
import random
from itemy import Itemy

#itemy = bobek, ohryzek, kebab, noviny, lahev, krabicak, hodinky, tuzemak, energetak, derava_cepice, derave_tricko, derave_kalhoty, pizza, burger

#textury
textura_bobku = pygame.image.load("looting kose//textury//bobek.png")
textura_ohryzku = pygame.image.load("looting kose//textury//ohryzek.png")
textura_kebabu = pygame.image.load("looting kose//textury//kebab.png")
textura_novin = pygame.image.load("looting kose//textury//noviny.png")
textura_lahve = pygame.image.load("looting kose//textury//lahev.png")
textura_krabicaku = pygame.image.load("looting kose//textury//krabicak.png")
textura_hodinek = pygame.image.load("looting kose//textury//hodinky.png")
textura_tuzemaku = pygame.image.load("looting kose//textury//tuzemak.png")
textura_energetaku = pygame.image.load("looting kose//textury//energetak.png")
textura_derave_cepice = pygame.image.load("looting kose//textury//cepice.png")
textura_derave_tricko = pygame.image.load("looting kose//textury//tricko.png")
textura_derave_kalhoty = pygame.image.load("looting kose//textury//kalhoty.png")
textura_pizza = pygame.image.load("looting kose//textury//pizza.png")
textura_burger = pygame.image.load("looting kose//textury//burger.png")

#okno
okraje = 20

rozliseni_x = 300 + 2*okraje
rozliseni_y = rozliseni_x

okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))

#class aktivace
item = Itemy(okno, textura_bobku, textura_ohryzku, textura_kebabu, textura_novin, textura_lahve, textura_krabicaku, textura_hodinek, textura_tuzemaku, textura_energetaku, textura_derave_cepice, textura_derave_tricko, textura_derave_kalhoty, textura_pizza, textura_burger)

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
