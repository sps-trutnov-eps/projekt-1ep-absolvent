import pygame

from mesta.mapa.budova import Budova
from mesta.mapa.interakcni_zona import InterakcniZona

from master import convertFuncToStr as novyProgram

from smrt_na_silnici.Honza_smrt_na_silnici import main as minihra

def nic():
    pass

def spusteni(global_data):
    global_data['otevrena_okna'].append(novyProgram(minihra))

def mesto1Init(okno, velikost_okna, global_data):
    velikost_mapy = pygame.Rect(0, 0, 2050,2830)
    # vytvori budovy
    interakcni_zony = []

    interakcni_zony.append(InterakcniZona(500, 500, 500, 500, print, [2, 2]))

    textury = ["Frank_hnedy.png",
               "Martin_bily.png",
               "Martin_hnedy.png",
               "Martin_sedy.png",
               "Martin_zluty.png",
               "parkoviste.png",
               "banka.png",
               "silnice.png",
               "silnice_s_kanálem.png",
               "zatáčka.png",
               "křižovatka.png",
               "quadroformagi.png",
               "temp_namko.png"
               ]

    textury = [pygame.image.load(f"textury\\budovy\\{textura}").convert() for textura in textury]
    #chopped textura parkoviste
    scaled_textura_parkoviste = pygame.transform.scale(textury[6], (800, 533))
    parkovisko_rect = textury[6].get_rect()
    parkovisko_flipped = pygame.transform.rotate(scaled_textura_parkoviste, 180)
    #silnice 
    silnice_rect = textury[7].get_rect()
    zatacka_rect = textury[9].get_rect()
    zatacka_flipped = pygame.transform.rotate(textury[9], 180)
    krizovatka_rect = textury[10].get_rect()
    guadroformagi_rect = textury[11].get_rect()
    # .convert_alpha() kdyz pouziva alpha
    print(textury)
    okno.fill((100, 150, 200))
    textury_rect = [item.get_rect() for item in textury]
    budovy = []
    #prvni horní řada domů z leva (0,0) - prvni dum v pořadí
    budovy.append(Budova(okno, 0, 0, textury_rect[1].width, textury_rect[1].height, textury[1]))
    budovy.append(Budova(okno, textury_rect[1].width, 0, textury_rect[2].width, textury_rect[2].height, textury[2]))
    budovy.append(Budova(okno, 2*textury_rect[1].width, 0, textury_rect[3].width, textury_rect[3].height, textury[3]))
    budovy.append(Budova(okno, 3*textury_rect[1].width, 0, textury_rect[4].width, textury_rect[4].height, textury[4]))
    #druha horní řada domů po mezeře (1200, 0) - prvni dum v pořadí
    budovy.append(Budova(okno, 6*textury_rect[1].width, 0, textury_rect[1].width, textury_rect[1].height, textury[1]))
    budovy.append(Budova(okno, 7*textury_rect[1].width, 0, textury_rect[2].width, textury_rect[2].height, textury[2]))
    budovy.append(Budova(okno, 8*textury_rect[1].width, 0, textury_rect[3].width, textury_rect[3].height, textury[3]))
    budovy.append(Budova(okno, 9*textury_rect[1].width, 0, textury_rect[4].width, textury_rect[4].height, textury[4]))
    #první dolní řada domů z leva (200, 1360) - prvni dum v pořadí
    budovy.append(Budova(okno, 200, 1320, textury_rect[1].width, textury_rect[1].height, textury[1]))
    budovy.append(Budova(okno, 200 + textury_rect[1].width, 1320, textury_rect[2].width, textury_rect[2].height, textury[2]))   
    budovy.append(Budova(okno, 200 + 2*textury_rect[1].width, 1320, textury_rect[3].width, textury_rect[3].height, textury[3]))
    #druhá dolní řada domů z leva (200, 1360) - prvni dum v pořadí
    budovy.append(Budova(okno, 200 + 5*textury_rect[1].width, 1320, textury_rect[1].width, textury_rect[1].height, textury[4]))
    budovy.append(Budova(okno, 200 + 6*textury_rect[1].width, 1320, textury_rect[1].width, textury_rect[1].height, textury[1]))
    budovy.append(Budova(okno, 200 + 7*textury_rect[1].width, 1320, textury_rect[1].width, textury_rect[1].height, textury[2]))
    #první sloupec domů vpravo (0, 100-chopped střechy) - prvni dum v pořadí
    budovy.append(Budova(okno, 0, textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[2]))
    budovy.append(Budova(okno, 0, 100 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[3]))
    budovy.append(Budova(okno, 0, 200 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[4]))
    #druhá část sloupců vpravo (0,1020)
    budovy.append(Budova(okno, 0, 920 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[2]))
    budovy.append(Budova(okno, 0, 1020 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[3]))
    budovy.append(Budova(okno, 0, 1120 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[4]))
    budovy.append(Budova(okno, 0, 1220 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[1]))
    #druhy sloupec domů vlevo (1800, 100-chopped střechy) - prvni dum v pořadí
    budovy.append(Budova(okno, 1800, textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[2]))
    budovy.append(Budova(okno, 1800, 100 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[3]))
    budovy.append(Budova(okno, 1800, 200 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[4]))
    #druha cast sloupcu vlevo (1800, 1020)
    budovy.append(Budova(okno, 1800, 920 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[1]))
    budovy.append(Budova(okno, 1800, 1020 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[2]))
    budovy.append(Budova(okno, 1800, 1120 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[3]))
    budovy.append(Budova(okno, 1800, 1220 + textury_rect[1].height-220, textury_rect[1].width, textury_rect[1].height, textury[4]))
    
    #silnice 
    #MODEL
    interakcni_zony.append(InterakcniZona(0, 620, 0, 0, nic, textura=textury[7]))
    interakcni_zony.append(InterakcniZona(400, 570, 1200, 500, nic, textura=textury[12]))
    #interakcni_zony.append(InterakcniZona(0, 420, 0, 0, nic, textura=zatacka_flipped))   
    #interakcni_zony.append(InterakcniZona(200, 320, 0,0,nic, textura= textury[9]))
    interakcni_zony.append(InterakcniZona(0,0, 1920,80, spusteni, argumenty=[global_data]))
    interakcni_zony.append(InterakcniZona(0,1640, 1920,80, spusteni, argumenty=[global_data]))
    #interakcni_zony.append(InterakcniZona(250, 370, 0, 0, nic, textura=textury[5]))
    #parkovisko
    #interakcni_zony.append(InterakcniZona(600, 1900, parkovisko_rect.width, parkovisko_rect.height, nic, textura=scaled_textura_parkoviste))
    #spusteni funkce
    #interakcni_zony.append(InterakcniZona(220, 340, 500, 500, spusteni, argumenty=[global_data], textura=textury[5]))



    #budovy = [Budova(okno, sum([textury_rect[j].width for j in range(i)]), 0, textury_rect[i].width, textury_rect[i].height, textury[i]) for i in range(len(textury))]
    return budovy, interakcni_zony, velikost_mapy, [0, 0]

