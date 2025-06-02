import pygame
import os
from mesta.mapa.budova import Budova
from mesta.mapa.interakcni_zona import InterakcniZona

from master import convertFuncToStr as novyProgram

from smrt_na_silnici.Honza_smrt_na_silnici import main as minihra




def nic():
    pass

def lore1():
    cesta = "lore\\absolvent1.txt"
    os.startfile(cesta)

    

def spusteni(global_data):
    global_data['otevrena_okna'].append(novyProgram(minihra))

def mesto1Init(okno, velikost_okna, global_data):


    velikost_mapy = pygame.Rect(0, 0, 2050,1725)

    flashka_texture = pygame.image.load("textury/itemy/flashka_typu_normalni.png")
    flashka_rescaled = pygame.transform.scale(flashka_texture, (70, 70))
    
   
   

    # vytvori budovy
    interakcni_zony = []

    interakcni_zony.append(InterakcniZona(500, 500, 500, 500, print, [2, 2]))

    # .convert_alpha() kdyz pouziva alpha
    okno.fill((100, 150, 200))

    budovy = []
    
    interakcni_zony.append(InterakcniZona(100, 100, 100, 100, lore1, textura=flashka_rescaled))


    #budovy = [Budova(okno, sum([textury_rect[j].width for j in range(i)]), 0, textury_rect[i].width, textury_rect[i].height, textury[i]) for i in range(len(textury))]
    return budovy, interakcni_zony, velikost_mapy, [0, 0]
