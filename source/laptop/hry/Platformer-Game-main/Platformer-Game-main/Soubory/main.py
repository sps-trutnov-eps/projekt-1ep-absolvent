import os
import pygame as pg

from hrac import Hrac
from zed import Zed
from tlacitko import Tlacitko

def konec():
    pg.quit()
    quit()

rozliseni_okna = [1920, 1080]
okno = pg.display.set_mode(rozliseni_okna)
pg.display.set_caption("Platformer-Game")

posledni_cas = pg.time.get_ticks()

fps = 60
hodiny = pg.time.Clock()

zakladni_gravitace = rozliseni_okna[1] / 900
padaci_limit = zakladni_gravitace * 36

aktualni_level = 1

escape_menu = True
edituje = False
v_nastaveni = False
level_menu = False
nehraje = False

druh_levelu = 0

aktualni_hrac = 0
nastaveni_tab = 0

cekani = None

drzi_cislo = 1

# Zed
# Krabice
# Tlacitko
# Dvere
# Hrac
# Cil

item_cisla = [
    'Zed',
    'Krabice',
    'Tlacitko',
    'Tlacitko Zvetsovani',
    'Tlacitko Zmensovani',
    'Dvere',
    'Enemy',
    'Hrac',
    'Cil'
]

opacne_item_cisla = {
    ' ': '-',
    'Zed': 1,
    'Krabice': 2,
    'Tlacitko': 3,
    'Tlacitko Zvetsovani': 4,
    'Tlacitko Zmensovani': 5,
    'Dvere': 6,
    'Enemy': 7,
    'Hrac': 8,
    'Cil': 9
}

nastaveni_hry = {
    'Hraci': [{
        'doleva': pg.K_a,
        'doprava': pg.K_d,
        'skakani': pg.K_w
    },

    {
        'doleva': pg.K_LEFT,
        'doprava': pg.K_RIGHT,
        'skakani': pg.K_UP
    }],
    'restart': pg.K_r
}

zmenit_kabel_xy = True
kabel_xy = []

hlavni_smycka = True
while hlavni_smycka:

    pocet_main_levelu = 0
    pocet_custom_levelu = 0
    pocet_2_player_levelu = 0

    slozka_levelu = "levely"
    slozka_custom_levelu = "levely\\custom"
    slozka_2_player_levelu = "levely\\2_player"

    for item in os.listdir(slozka_levelu):
        item_path = os.path.join(slozka_levelu, item)

        if os.path.isfile(item_path):
            pocet_main_levelu += 1

    for item in os.listdir(slozka_custom_levelu):
        item_path = os.path.join(slozka_custom_levelu, item)

        if os.path.isfile(item_path):
            pocet_custom_levelu += 1

    for item in os.listdir(slozka_2_player_levelu):
        item_path = os.path.join(slozka_2_player_levelu, item)

        if os.path.isfile(item_path):
            pocet_2_player_levelu += 1

    nehraje = False

    zdi = []
    grid = [[' '] * 36 for _ in range(64)]

    konec_mapy = False
    koordinace_tlacitka = []
    byl_charakter = True

    if aktualni_level == -1:
        aktualni_level = 1

    soubor = None
    if druh_levelu == 0:
        if aktualni_level <= pocet_main_levelu:
            soubor = f"levely\\level_{aktualni_level}.txt"

    elif druh_levelu == 2:
        if aktualni_level < pocet_custom_levelu:
            soubor = f"levely\\custom\\level_{aktualni_level}.txt"

    elif druh_levelu == 1:
        if aktualni_level < pocet_2_player_levelu:
            soubor = f"levely\\2_player\\level_{aktualni_level}.txt"

    if soubor == None:
        soubor = f"levely\\level_1.txt"

    with open(soubor) as level:
        for sloupec_cislo, sloupec in enumerate(level):
            sloupec = sloupec.rstrip("\n")

            if koordinace_tlacitka != []:
                for zed in zdi:
                    if zed.block == 'Tlacitko' or zed.block == 'Tlacitko Zvetsovani' or zed.block == 'Tlacitko Zmensovani' or zed.block == 'Cil':

                        if zed.grid_x == koordinace_tlacitka[0] and zed.grid_y == koordinace_tlacitka[1]:
                            zed.propojene_itemy.append([koordinace_tlacitka[2], koordinace_tlacitka[3]])

            koordinace_tlacitka = []
            cislo_tlacitko = []

            tl = False

            radek_cislo = 0
            for sloupec, charakter in enumerate(sloupec):

                if tl:

                    try:
                        int(charakter)
                        cislo_tlacitko.append(charakter)

                    except:

                        if cislo_tlacitko != []:
                            koordinace_tlacitka.append(int(''.join(cislo_tlacitko)))

                        cislo_tlacitko = []

                if konec_mapy:
                    if charakter == 'L' and posledni_charakter == 'T':
                        tl = True

                    posledni_charakter = charakter

                else:

                    byl_charakter = False

                    if charakter != ' ':
                        for i in range(len(item_cisla)):

                            if charakter == str(i + 1):
                                zdi.append(Zed(rozliseni_okna, radek_cislo, sloupec_cislo, 1, 1, item_cisla[i]))
                                grid[radek_cislo][sloupec_cislo] = item_cisla[i]

                        radek_cislo += 1
                        byl_charakter = True

                    if byl_charakter == False:
                        konec_mapy = True

    i = 0

    hraci = []
    for zed in zdi:
        if zed.block == 'Hrac':
            try:
                hraci.append(Hrac(zed.x, zed.y, rozliseni_okna[0] / 80, rozliseni_okna[1] / 21.6, rozliseni_okna[0] / 384, -rozliseni_okna[1] / 90, nastaveni = nastaveni_hry['Hraci'][i]))
                i += 1

            except:
                hraci.append(Hrac(zed.x, zed.y, rozliseni_okna[0] / 80, rozliseni_okna[1] / 21.6, rozliseni_okna[0] / 384, -rozliseni_okna[1] / 90))

    temp_zdi = zdi.copy()
    for zed in zdi:
        if zed.block == 'Hrac':
            temp_zdi.remove(zed)

    zdi = temp_zdi.copy()
    i = 0
    pocet_hracu = len(hraci)



    if escape_menu:
        tlacitka = []
        tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] / 2 - rozliseni_okna[0] / 20, 1 * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Hrat'))
        tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] / 2 - rozliseni_okna[0] / 20, 1.75 * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Levely'))
        tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] / 2 - rozliseni_okna[0] / 20, 2.5 * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Editor'))
        tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] / 2 - rozliseni_okna[0] / 20, 3.25 * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Nastaveni'))
        tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] / 2 - rozliseni_okna[0] / 20, 4 * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Ukoncit Hru'))

    while escape_menu:
        hodiny.tick(fps)

        soucasny_cas = pg.time.get_ticks()
        delta_cas = (soucasny_cas - posledni_cas) / 1000.0  # Convert to seconds
        posledni_cas = soucasny_cas

        klice = pg.key.get_pressed()

        for udalost in pg.event.get():
            if udalost.type == pg.QUIT:
                konec()

        #if klice[pg.K_ESCAPE]:
        #    escape_menu = False

        okno.fill((0, 0, 0))

        pozice_mys = pg.mouse.get_pos()

        for tlacitko in tlacitka:
            tlacitko.nakresly(okno)

            if tlacitko.zmacknuti(pozice_mys):
                escape_menu = False

                if tlacitko.text == 'Levely':
                    level_menu = True

                elif tlacitko.text == 'Editor':
                    edituje = True

                elif tlacitko.text == 'Nastaveni':
                    v_nastaveni = True

                elif tlacitko.text == 'Ukoncit Hru':
                    konec()

        pg.display.flip()



    if level_menu:
        nacist_tlacitka = True

    while level_menu:
        hodiny.tick(fps)

        soucasny_cas = pg.time.get_ticks()
        delta_cas = (soucasny_cas - posledni_cas) / 1000.0  # Convert to seconds
        posledni_cas = soucasny_cas

        klice = pg.key.get_pressed()

        for udalost in pg.event.get():
            if udalost.type == pg.QUIT:
                konec()

        if klice[pg.K_ESCAPE]:
            nehraje = True
            level_menu = False
            escape_menu = True

        okno.fill((0, 0, 0))

        pozice_mys = pg.mouse.get_pos()

        for tlacitko in tlacitka:
            tlacitko.nakresly(okno)

            if tlacitko.zmacknuti(pozice_mys):

                if tlacitko.level != -1:
                    if isinstance(tlacitko.level, int):

                        nehraje = True
                        aktualni_level = tlacitko.level
                        level_menu = False

                else:
                    if tlacitko.text == "main":
                        druh_levelu = 0
                        nacist_tlacitka = True

                    elif tlacitko.text == "custom":
                        druh_levelu = 2
                        nacist_tlacitka = True

                    elif tlacitko.text == "2 player":
                        druh_levelu = 1
                        nacist_tlacitka = True

        if nacist_tlacitka:
            tlacitka = []

            tlacitka.append(Tlacitko(rozliseni_okna, 1 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, "main", barva = (0, 0, 0), barva_textu = (255, 255, 255)))
            tlacitka.append(Tlacitko(rozliseni_okna, 3 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, "custom", barva = (0, 0, 0), barva_textu = (255, 255, 255)))
            tlacitka.append(Tlacitko(rozliseni_okna, 2 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, "2 player", barva = (0, 0, 0), barva_textu = (255, 255, 255)))

            if druh_levelu == 0:
                for level_cislo in range(pocet_main_levelu):
                    tlacitka.append(Tlacitko(rozliseni_okna, ((level_cislo % 5) + 1) * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, ((int(level_cislo // 5)) + 1) * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, f"level - {level_cislo + 1}", level_cislo + 1))

            elif druh_levelu == 2:
                for level_cislo in range(pocet_custom_levelu - 1):
                    tlacitka.append(Tlacitko(rozliseni_okna, ((level_cislo % 5) + 1) * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, ((int(level_cislo // 5)) + 1) * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, f"level - {level_cislo + 1}", level_cislo + 1))

            elif druh_levelu == 1:
                for level_cislo in range(pocet_2_player_levelu - 1):
                    tlacitka.append(Tlacitko(rozliseni_okna, ((level_cislo % 5) + 1) * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, ((int(level_cislo // 5)) + 1) * rozliseni_okna[1] / 7 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, f"level - {level_cislo + 1}", level_cislo + 1))

            nacist_tlacitka = False

        if druh_levelu == 0:
            pg.draw.rect(okno, (0, 0, 200), (1 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 40, rozliseni_okna[1] / 15, rozliseni_okna[0] / 20, rozliseni_okna[1] / 96))

        elif druh_levelu == 1:
            pg.draw.rect(okno, (0, 0, 200), (2 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 40, rozliseni_okna[1] / 15, rozliseni_okna[0] / 20, rozliseni_okna[1] / 96))

        elif druh_levelu == 2:
            pg.draw.rect(okno, (0, 0, 200), (3 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 40, rozliseni_okna[1] / 15, rozliseni_okna[0] / 20, rozliseni_okna[1] / 96))

        pg.display.flip()



    if v_nastaveni:
        nacist_tlacitka = True

    while v_nastaveni:
        hodiny.tick(fps)

        soucasny_cas = pg.time.get_ticks()
        delta_cas = (soucasny_cas - posledni_cas) / 1000.0  # Convert to seconds
        posledni_cas = soucasny_cas

        klice = pg.key.get_pressed()

        mys_1_zmacknuto = False
        for udalost in pg.event.get():
            if udalost.type == pg.QUIT:
                konec()

            if udalost.type == pg.KEYDOWN:
                zmacknute_tlacitko = udalost.key

            elif udalost.type == pg.MOUSEBUTTONDOWN:
                if udalost.button == 1:
                    mys_1_zmacknuto = True

        if klice[pg.K_ESCAPE]:
            nehraje = True
            v_nastaveni = False
            escape_menu = True

        okno.fill((0, 0, 0))

        pozice_mys = pg.mouse.get_pos()

        for tlacitko in tlacitka:
            tlacitko.nakresly(okno)

            if tlacitko.zmacknuti(pozice_mys) and mys_1_zmacknuto:
                if tlacitko.text == 'Hlavni':
                    nacist_tlacitka = True
                    nastaveni_tab = 0

                elif tlacitko.text == 'Hrac':
                    nacist_tlacitka = True
                    nastaveni_tab = 1

                elif tlacitko.text == '→':
                    nacist_tlacitka = True
                    aktualni_hrac += 1

                    try:
                        nastaveni_hry['Hraci'][aktualni_hrac]

                    except:
                        nastaveni_hry['Hraci'].append({
                            'doleva': None,
                            'doprava': None,
                            'skakani': None
                        })

                elif tlacitko.text == '←':
                    nacist_tlacitka = True
                    aktualni_hrac -= 1

                    if nastaveni_hry['Hraci'][len(nastaveni_hry['Hraci']) - 1] == {
                        'doleva': None,
                        'doprava': None,
                        'skakani': None
                    }:
                        nastaveni_hry['Hraci'].pop()

                if tlacitko.level != -1:
                    cekani = tlacitko.level
                    zmacknute_tlacitko = None

                    if tlacitko.level == 'reset':
                        nastaveni_hry['restart'] = None

                    else:
                        nastaveni_hry['Hraci'][aktualni_hrac][tlacitko.level] = None

        if cekani != None:
            if zmacknute_tlacitko != None and zmacknute_tlacitko != pg.K_ESCAPE:

                if cekani == 'reset':
                    nastaveni_hry['restart'] = zmacknute_tlacitko

                else:
                    nastaveni_hry['Hraci'][aktualni_hrac][cekani] = zmacknute_tlacitko

                nacist_tlacitka = True
                cekani = None

        if nastaveni_tab == 0:
            pg.draw.rect(okno, (0, 0, 200), (1 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 40, rozliseni_okna[1] / 15, rozliseni_okna[0] / 20, rozliseni_okna[1] / 96))

        elif nastaveni_tab:
            pg.draw.rect(okno, (0, 0, 200), (2 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 40, rozliseni_okna[1] / 15, rozliseni_okna[0] / 20, rozliseni_okna[1] / 96))

        if nacist_tlacitka:
            tlacitka = []

            if nastaveni_tab == 0:

                if nastaveni_hry['restart'] != None:
                    reset = pg.key.name(nastaveni_hry['restart'])

                else:
                    reset = '...'

                tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] - (1.5 * rozliseni_okna[0] / 6 + rozliseni_okna[0] / 20), 10 * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, text = reset, level = 'reset'))

                tlacitka.append(Tlacitko(rozliseni_okna, 1.5 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, 10 * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Reset', barva = (0, 0, 0), barva_textu = (255, 255, 255)))

            if nastaveni_tab == 1:

                tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] - (rozliseni_okna[0] / 20), 9 * rozliseni_okna[1] / 10, rozliseni_okna[0] / 30, rozliseni_okna[1] / 24, '→'))

                if aktualni_hrac > 0:
                    tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] / 20, 9 * rozliseni_okna[1] / 10, rozliseni_okna[0] / 30, rozliseni_okna[1] / 24, '←'))

                tlacitka.append(Tlacitko(rozliseni_okna, 1.5 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, 5 * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Skok', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
                tlacitka.append(Tlacitko(rozliseni_okna, 1.5 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, 10 * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Doleva', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
                tlacitka.append(Tlacitko(rozliseni_okna, 1.5 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, 15 * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Doprava', barva = (0, 0, 0), barva_textu = (255, 255, 255)))

                if nastaveni_hry['Hraci'][aktualni_hrac]["skakani"] != None:
                    skakani = pg.key.name(nastaveni_hry['Hraci'][aktualni_hrac]["skakani"])

                else:
                    skakani = '...'

                if nastaveni_hry['Hraci'][aktualni_hrac]["doleva"] != None:
                    doleva = pg.key.name(nastaveni_hry['Hraci'][aktualni_hrac]["doleva"])

                else:
                    doleva = '...'

                if nastaveni_hry['Hraci'][aktualni_hrac]["doprava"] != None:
                    doprava = pg.key.name(nastaveni_hry['Hraci'][aktualni_hrac]["doprava"])

                else:
                    doprava = '...'

                tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] - (1.5 * rozliseni_okna[0] / 6 + rozliseni_okna[0] / 20), 5  * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, text = skakani, level = "skakani"))
                tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] - (1.5 * rozliseni_okna[0] / 6 + rozliseni_okna[0] / 20), 10 * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, text = doleva, level = "doleva"))
                tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] - (1.5 * rozliseni_okna[0] / 6 + rozliseni_okna[0] / 20), 15 * rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, text = doprava, level = "doprava"))

            tlacitka.append(Tlacitko(rozliseni_okna, 1 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, "Hlavni", barva = (0, 0, 0), barva_textu = (255, 255, 255)))
            tlacitka.append(Tlacitko(rozliseni_okna, 2 * rozliseni_okna[0] / 6 - rozliseni_okna[0] / 20, rozliseni_okna[1] / 36, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, "Hrac", barva = (0, 0, 0), barva_textu = (255, 255, 255)))

        pg.display.flip()



    if edituje:
        tlacitka_mapa = []
        kabel_xy = []

    while edituje:
        hodiny.tick(fps)

        soucasny_cas = pg.time.get_ticks()
        delta_cas = (soucasny_cas - posledni_cas) / 1000.0  # Convert to seconds
        posledni_cas = soucasny_cas

        klice = pg.key.get_pressed()

        tlacitko_2 = False
        for udalost in pg.event.get():
            if udalost.type == pg.QUIT:
                konec()

            if udalost.type == pg.MOUSEBUTTONDOWN:
                if udalost.button == 5:  # Scroll Down

                    if drzi_cislo < len(item_cisla) - 1:
                        drzi_cislo += 1

                    else:
                        drzi_cislo = 0

                elif udalost.button == 4:  # Scroll Up

                    if drzi_cislo > 0:
                        drzi_cislo -= 1

                    else:
                        drzi_cislo = len(item_cisla) - 1

                if udalost.button == 2:
                    tlacitko_2 = True

        drzi = item_cisla[drzi_cislo]

        if klice[pg.K_ESCAPE]:

            tlacitka = []
            tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] * 1 / 3 - rozliseni_okna[0] / 20, rozliseni_okna[1] / 2 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Ulozit'))
            tlacitka.append(Tlacitko(rozliseni_okna, rozliseni_okna[0] * 2 / 3 - rozliseni_okna[0] / 20, rozliseni_okna[1] / 2 - rozliseni_okna[1] / 48, rozliseni_okna[0] / 10, rozliseni_okna[1] / 24, 'Neukladat'))

            ukladani = True
            while ukladani:
                hodiny.tick(fps)

                soucasny_cas = pg.time.get_ticks()
                delta_cas = (soucasny_cas - posledni_cas) / 1000.0  # Convert to seconds
                posledni_cas = soucasny_cas

                klice = pg.key.get_pressed()
                pozice_mys = pg.mouse.get_pos()

                for udalost in pg.event.get():
                    if udalost.type == pg.QUIT:
                        konec()

                okno.fill((0, 0, 0))

                for tlacitko in tlacitka:
                    tlacitko.nakresly(okno)

                    if tlacitko.zmacknuti(pozice_mys):

                        nehraje = True
                        edituje = False
                        escape_menu = True
                        ukladani = False

                        if tlacitko.text == 'Ulozit':

                            with open(f"levely\\custom\\level_{pocet_custom_levelu}.txt", 'w') as level:
                                for radek in zip(*grid):
                                    for charakter in radek:

                                        level.write(str(opacne_item_cisla[charakter]))

                                    level.write('\n')

                                if tlacitka_mapa != []:
                                    level.write('\nTL - start\n')
                                    for item in tlacitka_mapa:
                                        level.write(f"TL {item['x']}, {item['y']} - {item['pozice veci']}")

                                        level.write('\n')
                                    level.write("TL - end\n")

                        break

                pg.display.flip()

            break

        okno.fill((0, 0, 0))

        for zed in zdi:
            zed.nakresly(okno)


        pozice_mys = pg.mouse.get_pos()

        if pg.mouse.get_pressed()[0]:

            zed_x = int(pozice_mys[0] / (rozliseni_okna[0] / 64))
            zed_y = int(pozice_mys[1] / (rozliseni_okna[1] / 36))

            try:
                if  grid[zed_x][zed_y] != drzi:
                    grid[zed_x][zed_y] = drzi

                    temp_zdi = zdi.copy()

                    for zed1 in zdi:
                        if drzi == 'Hrac':
                            if (zed1.x / (rozliseni_okna[0] / 64) == zed_x and
                                zed1.y / (rozliseni_okna[1] / 36) == zed_y + 1):

                                temp_zdi.remove(zed1)

                        if (zed1.x / (rozliseni_okna[0] / 64) == zed_x and
                            zed1.y / (rozliseni_okna[1] / 36) == zed_y):

                            temp_zdi.remove(zed1)

                    zdi = temp_zdi.copy()

                    if drzi == 'Hrac':
                        zdi.append(Zed(rozliseni_okna, zed_x, zed_y, 0.8, 36 / 21.6, drzi, (255, 255, 255)))

                    else:
                        zdi.append(Zed(rozliseni_okna, zed_x, zed_y, 1, 1, drzi))

            except:
                pass

        if tlacitko_2: # middle tlacitko na mysi
            zmenit_kabel_xy = not zmenit_kabel_xy

            mys_grid = [int(pozice_mys[0] / (rozliseni_okna[0] / 64)), int(pozice_mys[1] / (rozliseni_okna[1] / 36))]

            if kabel_xy != [] and mys_grid != kabel_xy:

                try:
                    tlacitka_mapa.remove({
                        'x': kabel_xy[0],
                        'y': kabel_xy[1],
                        'pozice veci': mys_grid
                    })

                except:
                    tlacitka_mapa.append({
                        'x': kabel_xy[0],
                        'y': kabel_xy[1],
                        'pozice veci': mys_grid
                    })

                    print("kabel polozen")

                kabel_xy = []

            elif kabel_xy != []:
                kabel_xy = []

            if zmenit_kabel_xy:
                kabel_xy = mys_grid

        if pg.mouse.get_pressed()[2]:

            zed_x = int(pozice_mys[0] / (rozliseni_okna[0] / 64))
            zed_y = int(pozice_mys[1] / (rozliseni_okna[1] / 36))

            try:
                grid[zed_x][zed_y] = ' '

                temp_zdi = zdi.copy()

                for zed1 in zdi:
                    if (zed1.x / (rozliseni_okna[0] / 64) == zed_x and
                        zed1.y / (rozliseni_okna[1] / 36) == zed_y):

                        temp_zdi.remove(zed1)

                zdi = temp_zdi.copy()

            except:
                pass
        for hrac in hraci:
            hrac.nakresly(okno)

        if tlacitka_mapa != []:
            for tlacitko_mapa in tlacitka_mapa:
                pg.draw.line(okno, (255, 0, 0),
                            (tlacitko_mapa['x'] * rozliseni_okna[0] / 64 + rozliseni_okna[0] / 128, tlacitko_mapa['y'] * rozliseni_okna[1] / 36 + rozliseni_okna[1] / 72),
                            (tlacitko_mapa['pozice veci'][0] * rozliseni_okna[0] / 64 + rozliseni_okna[0] / 128, tlacitko_mapa['pozice veci'][1] * rozliseni_okna[1] / 36 + rozliseni_okna[1] / 72))

        pg.display.flip()



    tlacitka = []

    vyhral = False

    hraje = True
    while hraje:
        if nehraje:
            break

        hodiny.tick(fps)

        soucasny_cas = pg.time.get_ticks()
        delta_cas = (soucasny_cas - posledni_cas) / 16  # Convert to seconds

        posledni_cas = soucasny_cas

        gravitace = zakladni_gravitace * delta_cas
        padaci_limit = gravitace * 36

        for hrac in hraci:
            hrac.delta_cas = delta_cas

        for zed in zdi:
            zed.delta_cas = delta_cas

        klice = pg.key.get_pressed()

        for udalost in pg.event.get():
            if udalost.type == pg.QUIT:
                konec()

        if klice[pg.K_ESCAPE]:
            escape_menu = True
            hraje = False

        if klice[nastaveni_hry['restart']]:
            hraje = False

        for hrac in hraci:
            muze_dostran = True

            hrac.rychlost_x = 0
            if not hrac.nazemi and not hrac.rychlost_y > padaci_limit:
                hrac.rychlost_y += gravitace

            elif hrac.nazemi:
                hrac.muze_skocit = True

            if hrac.nastaveni['doleva'] != None and hrac.nastaveni['doprava'] != None:
                if klice[hrac.nastaveni['doleva']] and klice[hrac.nastaveni['doprava']]:
                    muze_dostran = False

            if muze_dostran:
                if hrac.nastaveni['doleva'] != None:
                    if klice[hrac.nastaveni['doleva']]:
                        hrac.rychlost_x = -hrac.chodici_rychlost

                if hrac.nastaveni['doprava'] != None:
                    if klice[hrac.nastaveni['doprava']]:
                        hrac.rychlost_x = hrac.chodici_rychlost

            if hrac.nastaveni['skakani'] != None:
                if klice[hrac.nastaveni['skakani']] and hrac.muze_skocit:
                    hrac.muze_skocit = False
                    hrac.rychlost_y = hrac.skakaci_rychlost

            hrac.nazemi = False
            hrac.muze_zvetsovat = True

        okno.fill((0, 0, 0))

        hraci_v_cili = 0

        for zed in zdi:
            if zed.block == 'Tlacitko' or 'Tlacitko Zvetsovani' or 'Tlacitko Zmensovani' or 'Cil':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Krabice':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Enemy':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Zed':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Dvere':
                zed.nakresly(okno)

        for zed in zdi:

            for hrac in hraci:
                zed.zvetsovaciKolize(hrac)

            if zed.block == 'Dvere':
                zed.rychlost_y = 0

            if zed.aktivni:
                if zed.block == 'Dvere' and zed.pozice < zed.pohybova_durace:
                    zed.rychlost_y = zed.rychlost_nahoru
                    zed.pozice += 1

            else:
                if zed.pozice > 0:
                    zed.rychlost_y = -zed.rychlost_nahoru
                    zed.pozice -= 1

            zed.aktivni = False

            zed.nazemi = False

            for hrac in hraci:
                if zed.block != 'Tlacitko' and zed.block != 'Tlacitko Zvetsovani' and zed.block != 'Tlacitko Zmensovani' and zed.block != 'Cil':
                    zed.kolize(hrac)

                elif zed.block == 'Tlacitko' or zed.block == 'Tlacitko Zvetsovani' or zed.block == 'Tlacitko Zmensovani':
                    zed.tlacitkoKolize(hrac, zdi)

                elif zed.block == 'Cil':
                    hraci_v_cili += zed.cilKolize(hrac)

            if hraci_v_cili == pocet_hracu != 0:
                vyhral = True

                if hraci_v_cili > 1:
                    vyherni_text = 'Vyhrali Jste'

                else:
                    vyherni_text = 'Vyhral Jsi'

            if zed.block == 'Zed':
                zed.rychlost_x = 0
                zed.rychlost_y = 0

            elif zed.block == 'Enemy':
                if zed.kouka_vlevo:
                    zed.rychlost_x = -zed.chodici_rychlost

                else:
                    zed.rychlost_x = zed.chodici_rychlost

            zed.pohni()

            for zed1 in zdi:
                for hrac in hraci:
                    if zed.block == 'Dvere' and zed1.block == 'Krabice':
                        dvere_ctverec = pg.Rect(zed.x, zed.y, zed.sirka, zed.rychlost_y)
                        krabice_ctverec = pg.Rect(zed1.x, zed1.y, zed1.sirka, zed1.vyska)

                        if dvere_ctverec.colliderect(krabice_ctverec):
                            zed1.nazemi = True
                            zed1.rychlost_y = zed.rychlost_y
                            zed1.pohni()

                    if (zed.block == 'Dvere' or 'Krabice'):
                        dvere_ctverec = pg.Rect(zed.x, zed.y, zed.sirka, zed.rychlost_y)
                        hrac_ctverec  = pg.Rect(hrac.x, hrac.y, hrac.sirka, hrac.vyska)

                        if dvere_ctverec.colliderect(hrac_ctverec):
                            hrac.nazemi = True
                            if hrac.rychlost_y >= 0:
                                hrac.rychlost_y = zed.rychlost_y

                    if (zed1.block == 'Krabice' or zed1.block == 'Enemy') and zed1 != zed:

                        if zed.block != 'Tlacitko' and zed.block != 'Tlacitko Zvetsovani' and zed.block != 'Tlacitko Zmensovani' and zed.block != 'Cil':
                            if hrac.kolize(zed1):
                                hrac.y = 12 * rozliseni_okna[1]

                            zed.kolize(zed1)

                        elif zed.block == 'Tlacitko' or zed.block == 'Tlacitko Zvetsovani' or zed.block == 'Tlacitko Zmensovani':
                            zed.tlacitkoKolize(zed1, zdi)

            if (zed.block == 'Krabice' or zed.block == 'Enemy') and not zed.nazemi and not zed.rychlost_y > padaci_limit:
                zed.rychlost_y += gravitace

        for zed in zdi:
            if zed.block == 'Tlacitko' or 'Tlacitko Zvetsovani' or 'Tlacitko Zmensovani' or 'Cil':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Krabice':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Enemy':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Zed':
                zed.nakresly(okno)

        for zed in zdi:
            if zed.block == 'Dvere':
                zed.nakresly(okno)

        for hrac in hraci:
            hrac.pohni()
            hrac.nakresly(okno)

        if vyhral:
            okno.fill((0, 0, 0))

            tlacitka.append(Tlacitko(rozliseni_okna,
                                     rozliseni_okna[0] / 32,
                                     rozliseni_okna[1] / 18,
                                     rozliseni_okna[0] - rozliseni_okna[0] / 16,
                                     rozliseni_okna[1] - rozliseni_okna[1] / 9,
                                     vyherni_text,
                                     barva = (0, 0, 0),
                                     barva_textu = (255, 255, 255),
                                     font = pg.font.SysFont('Arial',int(rozliseni_okna[0] / 32))))

            if len(tlacitka) > 1:
                tlacitka.pop()

        for tlacitko in tlacitka:
            tlacitko.nakresly(okno)

        pg.display.flip()