import pygame

from mesta.mapa.budova import Budova
from mesta.mapa.interakcni_zona import InterakcniZona

from master import convertFuncToStr as novyProgram

from smrt_na_silnici.Honza_smrt_na_silnici import main as minihra
from bankomat.Bankomat_obrazovka import main as ddos

def nic():
    pass

def novy_areal(global_data, kolikaty, xy):
    global_data["novy_areal"] = kolikaty
    global_data['otevrena_okna'].append(novyProgram(minihra))

    global_data["hrac"]["x"] = xy[0]
    global_data["hrac"]["y"] = xy[1]
def hacking(global_data):
    global_data['otevrena_okna'].append(novyProgram(ddos))

def mesto1Init(okno, velikost_okna, global_data):


    velikost_mapy = pygame.Rect(0, 0, 2050,1725)


    # vytvori budovy
    interakcni_zony = []

    textury = ["Frank_hnedy.png",#0
               "Martin_bily.png",#1
               "Martin_hnedy.png",#2
               "Martin_sedy.png",#3
               "Martin_zluty.png",#4
               "parkoviste.png",#5
               "banka1.png",#6
               "silnice.png",#7
               "silnice_s_kanálem.png",#8
               "zatáčka.png",#9
               "křižovatka.png",#10
               "quadroformagi.png",#11
               "temp_namko.png",#12
               "park.png",#13
               "buk.png",#14
               "smrk.png",#15
               "ker.png",#16
               "kytky.png",#17
               "lavicka.png",#18
               "chata1.png",#19
               "vodojem.png",#20
               "park_cesty.png",#21
               "radnice.png",#22
               "stanice.png",#23
               "namesti.png",#24
               "bankomat.png",#25

               ]

    textury = [pygame.image.load(f"textury\\budovy\\{textura}").convert_alpha() for textura in textury]
#NAMESTI
    scaled_banka = pygame.transform.scale(textury[6], (380, 320))
    scaled_stanice = pygame.transform.scale(textury[23],(200,320))
    #textury_itemy = [pygame.image.load(f"textury\\itemy\\{textura}").convert() for textura in textury_itemy]
    scaled_namesti = pygame.transform.scale(textury[24],(2005,1725))
    sirka_namesti = scaled_namesti.get_width()
    vyska_namesti = scaled_namesti.get_height()
    # .convert_alpha() kdyz pouziva alpha
    okno.fill((100, 150, 200))
    textury_rect = [item.get_rect() for item in textury]
    budovy = []
    #prvni horní řada domů z leva (0,0) - prvni dum v pořadí
    budovy.append(Budova(okno, 0, 0, 0, 0, textury[1]))
    budovy.append(Budova(okno, 200, 0, 200, 320, scaled_stanice))#stanice
    budovy.append(Budova(okno, 405, 0, textury_rect[22].width, textury_rect[22].height, textury[22]))#radnice
    #budovy.append(Budova(okno, 2*textury_rect[1].width, 0, textury_rect[3].width, textury_rect[3].height, textury[3]))
    #budovy.append(Budova(okno, 3*textury_rect[1].width, 0, textury_rect[4].width, textury_rect[4].height, textury[4]))
    budovy.append(Budova(okno, 4*textury_rect[1].width+10, 0, textury_rect[6].width, textury_rect[6].height, scaled_banka)) #banka
    
    #####budovy.append(Budova(okno, 4*textury_rect[1].width, 0, textury_rect[4].width, textury_rect[4].height, textury[2]))
    #####budovy.append(Budova(okno, 5*textury_rect[1].width, 0, textury_rect[4].width, textury_rect[4].height, textury[3]))
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
    #budovy.append(Budova(okno, 0, 0, textury_rect[24].width, textury_rect[24].height, textury[24]))

    budovy.append(Budova(okno, 1730,237 , textury_rect[25].width, textury_rect[25].height, textury[25]))#bankomat
#NAMESTI    
    interakcni_zony.append(InterakcniZona(0,0,sirka_namesti, vyska_namesti, nic, textura = scaled_namesti))

    interakcni_zony.append(InterakcniZona(0,1640, 1920,80, novy_areal, argumenty=[global_data, 2,(1055, 0)])) # #1. lokace - prechod z mesta na parkoviste	



    #budovy = [Budova(okno, sum([textury_rect[j].width for j in range(i)]), 0, textury_rect[i].width, textury_rect[i].height, textury[i]) for i in range(len(textury))]
    return budovy, interakcni_zony, velikost_mapy, [0, 0]

def mesto2Init(okno, velikost_okna, global_data):


    velikost_mapy = pygame.Rect(0, 0, 2050,1190)


    # vytvori budovy
    interakcni_zony = []

    textury = ["Frank_hnedy.png",#0
               "Martin_bily.png",#1
               "Martin_hnedy.png",#2
               "Martin_sedy.png",#3
               "Martin_zluty.png",#4
               "parkoviste.png",#5
               "banka1.png",#6
               "silnice.png",#7
               "silnice_s_kanálem.png",#8
               "zatáčka.png",#9
               "křižovatka.png",#10
               "quadroformagi.png",#11
               "temp_namko.png",#12
               "park.png",#13
               "buk.png",#14
               "smrk.png",#15
               "ker.png",#16
               "kytky.png",#17
               "lavicka.png",#18
               "chata1.png",#19
               "vodojem.png",#20
               "park_cesty.png",#21
               "odpadak.png",#22
               "obchod.png",#23
               "bankomat.png",#24
               "sipka_fixed.png",#25
               ]

    textury = [pygame.image.load(f"textury\\budovy\\{textura}").convert_alpha() for textura in textury]
#PARKOVISTE
    scaled_textura_parkoviste = pygame.transform.scale(textury[5], (2000, 1100))
    vodojem_scaled = pygame.transform.scale(textury[20], (400, 600))
    scaled_odpadak = pygame.transform.scale(textury[22], (50, 55))
    odpadak_rect = scaled_odpadak.get_rect()
    flipped_sipka = pygame.transform.flip(textury[25], 180, True) #sipka 
    

    # .convert_alpha() kdyz pouziva alpha
    okno.fill((100, 150, 200))
    textury_rect = [item.get_rect() for item in textury]
    budovy = []
    
    
    budovy.append(Budova(okno, 1780, 2980 - 1645, odpadak_rect.width, odpadak_rect.height, scaled_odpadak))#kos
    
    
    #PARKOVISTE
    interakcni_zony.append(InterakcniZona(0, 5, 0, 0, nic, textura=scaled_textura_parkoviste))#parkoviste
    interakcni_zony.append(InterakcniZona(-100, 2150 - 1645, 0, 0, nic, textura=vodojem_scaled))
    
    #odpadaky
    budovy.append(Budova(okno, 370, 2050 - 1645, odpadak_rect.width, odpadak_rect.height, scaled_odpadak))
    budovy.append(Budova(okno, 1340, 2050 - 1645, odpadak_rect.width, odpadak_rect.height, scaled_odpadak))
    budovy.append(Budova(okno, 1950, 2615 - 1645, odpadak_rect.width, odpadak_rect.height, scaled_odpadak))

    #obchod
    budovy.append(Budova(okno, 1770, 1740 - 1645, textury_rect[23].width, textury_rect[23].height, textury[23])) #obchod
    #bankomat
    budovy.append(Budova(okno, 1775, 2560 - 1645, textury_rect[24].width, textury_rect[24].height, textury[24]))
    
    #KHOVNU VECI
    #interakcni_zony.append(InterakcniZona(0, 420, 0, 0, nic, textura=zatacka_flipped))
    #sipky-dolu
    interakcni_zony.append(InterakcniZona(902, 2665 - 1645, textury_rect[25].width,textury_rect[25].height,nic, textura= textury[25]))  
    interakcni_zony.append(InterakcniZona(1102, 2665 - 1645, textury_rect[25].width,textury_rect[25].height,nic, textura= textury[25]))
    #sipky-nahoru 
    interakcni_zony.append(InterakcniZona(952, 0, textury_rect[25].width,textury_rect[25].height,nic, textura= flipped_sipka))  
    interakcni_zony.append(InterakcniZona(1152, 0, textury_rect[25].width,textury_rect[25].height,nic, textura= flipped_sipka)) 
    #interakcni_zony.append(InterakcniZona(200, 320, 0,0,nic, textura= textury[9]))
    #interakcni_zony.append(InterakcniZona(0,0, 1920,80, spusteni, argumenty=[global_data])) #smrt na silnici
#BANKOMAT
    interakcni_zony.append(InterakcniZona(1775,916,textury_rect[24].width, textury_rect[25].height,hacking, argumenty = [global_data]))
#SMRT NA SILNICI
    interakcni_zony.append(InterakcniZona(0,0, 1645,10, novy_areal, argumenty=[global_data, 1, (970, 1565)])) #2. lokace - prechod z parkoviste do mesta
    interakcni_zony.append(InterakcniZona(0,1030, 1645,80, novy_areal, argumenty=[global_data, 3, (950, 0)])) #2. lokace - prechod do parku
    #interakcni_zony.append(InterakcniZona(250, 370, 0, 0, nic, textura=textury[5]))
    #parkovisko
    #interakcni_zony.append(InterakcniZona(600, 1900, parkovisko_rect.width, parkovisko_rect.height, nic, textura=scaled_textura_parkoviste))
    #spusteni funkce
    #interakcni_zony.append(InterakcniZona(220, 340, 500, 500, spusteni, argumenty=[global_data], textura=textury[5]))



    #budovy = [Budova(okno, sum([textury_rect[j].width for j in range(i)]), 0, textury_rect[i].width, textury_rect[i].height, textury[i]) for i in range(len(textury))]
    return budovy, interakcni_zony, velikost_mapy, [0, 0]
    
def mesto3Init(okno, velikost_okna, global_data):


    velikost_mapy = pygame.Rect(0, 0, 2050,1175)


    # vytvori budovy
    interakcni_zony = []

    textury = ["Frank_hnedy.png",#0
               "Martin_bily.png",#1
               "Martin_hnedy.png",#2
               "Martin_sedy.png",#3
               "Martin_zluty.png",#4
               "parkoviste.png",#5
               "banka1.png",#6
               "silnice.png",#7
               "silnice_s_kanálem.png",#8
               "zatáčka.png",#9
               "křižovatka.png",#10
               "quadroformagi.png",#11
               "temp_namko.png",#12
               "park.png",#13
               "buk.png",#14
               "smrk.png",#15
               "ker.png",#16
               "kytky.png",#17
               "lavicka.png",#18
               "chata1.png",#19
               "vodojem.png",#20
               "park_cesty.png",#21
               "najezd.png",#22
               "odpadak.png",#23,
               "info_cedule.png" #24

               ]

    textury = [pygame.image.load(f"textury\\budovy\\{textura}").convert_alpha() for textura in textury]

    # .convert_alpha() kdyz pouziva alpha
    okno.fill((100, 150, 200))
    textury_rect = [item.get_rect() for item in textury]
    budovy = []

#PARK
    scaled_park = pygame.transform.scale(textury[13], (1050, 1090))
    scaled_cesty = pygame.transform.scale(textury[21], (1660, 740))
    scaled_kytky = pygame.transform.scale(textury[17], (40, 40))
    scaled_odpadak = pygame.transform.scale(textury[23], (40, 45))
    odpadak_rect = scaled_odpadak.get_rect()
    scaled_info_cedule = pygame.transform.scale(textury[24], (80, 80))
    info_cedule_rect = scaled_info_cedule.get_rect()
#PARK
    interakcni_zony.append(InterakcniZona(0, 0, 0, 0, nic, textura=scaled_park))#park pt. 1
    interakcni_zony.append(InterakcniZona(1020, 0, 0, 0, nic, textura=scaled_park))#park pt. 2
    interakcni_zony.append(InterakcniZona(160, 2980 - 2780, 0, 0, nic, textura=scaled_cesty))
    interakcni_zony.append(InterakcniZona(810, 2765 - 2780, 0, 0, nic, textura=textury[22]))#najezd
    ##stromy
    ###prvni sloupec stromů
    mezera = 10
    for i in range(7):
        textura = textury[14]
        y = 2820 - 2780 + i * (textury_rect[14].height+ mezera)
        budovy.append(Budova(okno, 40, y,textury_rect[15].width,textury_rect[15].height, textura=textura))
    ###druhy sloupec stromů
    for i in range(7):
        textura = textury[15]
        y = 2820 - 2780 + i * (textury_rect[15].height+ mezera)
        budovy.append(Budova(okno, 1860, y,textury_rect[15].width,textury_rect[15].height, textura=textura))
    #### dolní řada stromů
    for i in range(15):
        textura = textury[14] if i % 2 == 0 else textury[15]
        x = 40 + i * (textury_rect[15].height+ mezera)
        budovy.append(Budova(okno, x, 3730,textury_rect[15].width,textury_rect[15].height, textura=textura))
    #### horní řada stromů - pt. 1
    for i in range(6):
        textura = textury[14] if i % 2 == 0 else textury[15]
        x = 40 + i * (textury_rect[15].height+ mezera)
        budovy.append(Budova(okno, x, 2820 - 2780,textury_rect[15].width,textury_rect[15].height, textura=textura))
    #### horní řada stromů - pt. 2
    for i in range(5):
        textura = textury[14] if i % 2 == 0 else textury[15]
        x = 1240 + i * (textury_rect[15].height+ mezera)
        budovy.append(Budova(okno, x, 2820 - 2780,textury_rect[15].width,textury_rect[15].height, textura=textura))
    #info cedule
    budovy.append(Budova(okno, 1150, 2850 - 2780, info_cedule_rect.width, info_cedule_rect.height, scaled_info_cedule))
    #kytky - pravy/horni sektor
    interakcni_zony.append(InterakcniZona(495, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(520, 3190 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(545, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(570, 3190 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(600, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(625, 3190 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(650, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    #kytky - pravy/dolni sektor
    interakcni_zony.append(InterakcniZona(495, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(520, 3520 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(545, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(570, 3520 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(600, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(625, 3520 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(650, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    #kytky - levi/horni sektor
    interakcni_zony.append(InterakcniZona(1280, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1305, 3190 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1330, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1355, 3190 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1380, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1405, 3190 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1430, 3140 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    #kytky - levi/dolni sektor
    interakcni_zony.append(InterakcniZona(1280, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1305, 3520 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1330, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1355, 3520 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1380, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1405, 3520 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    interakcni_zony.append(InterakcniZona(1430, 3470 - 2780, textury_rect[17].width,textury_rect[17].height , nic, textura=scaled_kytky))
    #kere - 1 rada
    budovy.append(Budova(okno, 335, 3140 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 335, 3190 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 335, 3470 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 335, 3520 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    #kere - 2 rada
    budovy.append(Budova(okno, 795, 3140 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 795, 3190 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 795, 3470 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 795, 3520 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    #kere - 3 rada
    budovy.append(Budova(okno, 1120, 3140 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 1120, 3190 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 1120, 3470 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 1120, 3520 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    #kere - 4 rada
    budovy.append(Budova(okno, 1585, 3140 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 1585, 3190 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 1585, 3470 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    budovy.append(Budova(okno, 1585, 3520 - 2780, textury_rect[16].width, textury_rect[16].height, textury[16]))
    #lavicky - 1 rada
    budovy.append(Budova(okno, 395, 3130 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    budovy.append(Budova(okno, 395, 3460 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    #lavicky - 2 rada
    budovy.append(Budova(okno, 690, 3130 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    budovy.append(Budova(okno, 690, 3460 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    #lavicky - 3 rada
    budovy.append(Budova(okno, 1180, 3130 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    budovy.append(Budova(okno, 1180, 3460 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    #lavicky - 4 rada
    budovy.append(Budova(okno, 1480, 3130 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    budovy.append(Budova(okno, 1480, 3460 - 2780, textury_rect[18].width, textury_rect[18].height, textury[18]))
    #kose - 1 rada
    budovy.append(Budova(okno, 160, 2980 - 2780, odpadak_rect.width-10, odpadak_rect.height-10, scaled_odpadak))
    budovy.append(Budova(okno, 160, 3665 - 2780, odpadak_rect.width-10, odpadak_rect.height-10, scaled_odpadak))
    #kose - 2 rada
    budovy.append(Budova(okno, 1780, 2980 - 2780, odpadak_rect.width, odpadak_rect.height, scaled_odpadak))
    #budovy.append(Budova(okno, 1480, 3460, textury_rect[18].width, textury_rect[18].height, textury[18]))



    budovy.append(Budova(okno, 1700, 3565 - 2780,0,0, textura=textury[19]))
#Prechod na parkoviste
    interakcni_zony.append(InterakcniZona(0,2780 - 2780, 1645,80, novy_areal, argumenty=[global_data, 2, (1045, 1030)])) #3. lokace - prechod z parku
    #interakcni_zony.append(InterakcniZona(250, 370, 0, 0, nic, textura=textury[5]))
    #parkovisko
    #interakcni_zony.append(InterakcniZona(600, 1900, parkovisko_rect.width, parkovisko_rect.height, nic, textura=scaled_textura_parkoviste))
    #spusteni funkce
    #interakcni_zony.append(InterakcniZona(220, 340, 500, 500, spusteni, argumenty=[global_data], textura=textury[5]))



    #budovy = [Budova(okno, sum([textury_rect[j].width for j in range(i)]), 0, textury_rect[i].width, textury_rect[i].height, textury[i]) for i in range(len(textury))]
    return budovy, interakcni_zony, velikost_mapy, [0, 0]