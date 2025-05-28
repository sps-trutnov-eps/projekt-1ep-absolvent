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


    velikost_mapy = pygame.Rect(0, 0, 2050,3950)


    # vytvori budovy
    interakcni_zony = []

    interakcni_zony.append(InterakcniZona(500, 500, 500, 500, print, [2, 2]))

    textury = ["Frank_hnedy.png",
               "Martin_bily.png",
               "Martin_hnedy.png",
               "Martin_sedy.png",
               "Martin_zluty.png",
               "parkoviste.png",
               "banka1.png",
               "silnice.png",
               "silnice_s_kanálem.png",
               "zatáčka.png",
               "křižovatka.png",
               "quadroformagi.png",
               "temp_namko.png",
               "park.png",
               "buk.png",
               "smrk.png",
               "ker.png",
               "kytky.png",
               "lavicka.png",
               "chata1.png",
               "vodojem.png",
               "park_cesty.png"
               ]

    textury = [pygame.image.load(f"textury\\budovy\\{textura}").convert_alpha() for textura in textury]
#NAMESTI
    scaled_banka = pygame.transform.scale(textury[6], (380, 320))
    #textury_itemy = [pygame.image.load(f"textury\\itemy\\{textura}").convert() for textura in textury_itemy]
#PARKOVISTE
    scaled_textura_parkoviste = pygame.transform.scale(textury[5], (2000, 1100))
    parkovisko_rect = textury[6].get_rect()
    parkovisko_flipped = pygame.transform.rotate(scaled_textura_parkoviste, 180)
    vodojem_scaled = pygame.transform.scale(textury[20], (400, 600))
    #silnice 
    silnice_rect = textury[7].get_rect()
    zatacka_rect = textury[9].get_rect()
    zatacka_flipped = pygame.transform.rotate(textury[9], 180)
    krizovatka_rect = textury[10].get_rect()
    guadroformagi_rect = textury[11].get_rect()
#PARK
    scaled_park = pygame.transform.scale(textury[13], (1050, 1090))
    scaled_cesty = pygame.transform.scale(textury[21], (1660, 740))
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
    budovy.append(Budova(okno, 4*textury_rect[1].width+10, 0, textury_rect[6].width, textury_rect[6].height, scaled_banka)) #banka
    
    #budovy.append(Budova(okno, 4*textury_rect[1].width, 0, textury_rect[4].width, textury_rect[4].height, textury[2]))
    #budovy.append(Budova(okno, 5*textury_rect[1].width, 0, textury_rect[4].width, textury_rect[4].height, textury[3]))
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
    interakcni_zony.append(InterakcniZona(0, 620, 0, 0, nic, textura=textury[7]))#silnice
    interakcni_zony.append(InterakcniZona(400, 570, 1200, 500, nic, textura=textury[12]))#temp namko
    #PARKOVISTE
    interakcni_zony.append(InterakcniZona(0, 1650, 0, 0, nic, textura=scaled_textura_parkoviste))#parkoviste
    interakcni_zony.append(InterakcniZona(-100, 2150, 0, 0, nic, textura=vodojem_scaled))
    #PARK
    interakcni_zony.append(InterakcniZona(0, 2780, 0, 0, nic, textura=scaled_park))#park pt. 1
    interakcni_zony.append(InterakcniZona(1020, 2780, 0, 0, nic, textura=scaled_park))#park pt. 2
    interakcni_zony.append(InterakcniZona(160, 2980, 0, 0, nic, textura=scaled_cesty))
    ##stromy
    ###prvni sloupec stromů
    mezera = 10
    for i in range(7):
        textura = textury[14]
        y = 2820 + i * (textury_rect[14].height+ mezera)
        interakcni_zony.append(InterakcniZona(40, y, 0, 0, nic, textura=textura))
    ###druhy sloupec stromů
    for i in range(7):
        textura = textury[15]
        y = 2820 + i * (textury_rect[15].height+ mezera)
        interakcni_zony.append(InterakcniZona(1960-100, y, 0, 0, nic, textura=textura))
    #### dolní řada stromů
    for i in range(15):
        textura = textury[14] if i % 2 == 0 else textury[15]
        x = 40 + i * (textury_rect[15].height+ mezera)
        interakcni_zony.append(InterakcniZona(x, 3730, 0, 0, nic, textura=textura))
    #### horní řada stromů - pt. 1
    for i in range(6):
        textura = textury[14] if i % 2 == 0 else textury[15]
        x = 40 + i * (textury_rect[15].height+ mezera)
        interakcni_zony.append(InterakcniZona(x, 2820, 0, 0, nic, textura=textura))
    #### horní řada stromů - pt. 2
    for i in range(5):
        textura = textury[14] if i % 2 == 0 else textury[15]
        x = 1166 + i * (textury_rect[15].height+ mezera)
        interakcni_zony.append(InterakcniZona(x, 2820, 0, 0, nic, textura=textura))

    interakcni_zony.append(InterakcniZona(1690, 3570, 0, 0, nic, textura=textury[19]))#chata
    #interakcni_zony.append(InterakcniZona(0, 420, 0, 0, nic, textura=zatacka_flipped))   
    #interakcni_zony.append(InterakcniZona(200, 320, 0,0,nic, textura= textury[9]))
    interakcni_zony.append(InterakcniZona(0,0, 1920,80, spusteni, argumenty=[global_data])) #smrt na silnici
    interakcni_zony.append(InterakcniZona(0,1640, 1920,80, spusteni, argumenty=[global_data])) #smrt na silnici
    #interakcni_zony.append(InterakcniZona(250, 370, 0, 0, nic, textura=textury[5]))
    #parkovisko
    #interakcni_zony.append(InterakcniZona(600, 1900, parkovisko_rect.width, parkovisko_rect.height, nic, textura=scaled_textura_parkoviste))
    #spusteni funkce
    #interakcni_zony.append(InterakcniZona(220, 340, 500, 500, spusteni, argumenty=[global_data], textura=textury[5]))



    #budovy = [Budova(okno, sum([textury_rect[j].width for j in range(i)]), 0, textury_rect[i].width, textury_rect[i].height, textury[i]) for i in range(len(textury))]
    return budovy, interakcni_zony, velikost_mapy, [0, 0]

