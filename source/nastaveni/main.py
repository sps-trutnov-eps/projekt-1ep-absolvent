import pygame
from nastaveni.button import Button

from main import focusWindow


def numNaNastaveni(i):
    if i == 0:
        return 'inventory'

    elif i == 1:
        return 'interakce'

    elif i == 2:
        return 'exit'

    elif i == 3:
        return 'nahoru'

    elif i == 4:
        return 'dolu'

    elif i == 5:
        return 'doleva'

    elif i == 6:
        return 'doprava'


def novyButtony(global_data, velikost_okna, rozmery_buttonu, texty_buttonu: list):
    buttony = []

    texty = []

    for i in range(7):
        texty.append([pygame.key.name(global_data['nastaveni'][numNaNastaveni(i)]) if texty_buttonu[i] == None else texty_buttonu[i]][0])
        buttony.append(Button(velikost_okna, velikost_okna[0] // 2 + velikost_okna[0] // 8 + rozmery_buttonu[0] // 2, (i + 1) * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = texty[i]))

        #pygame.key.name(global_data['nastaveni']['inventory']) if texty[0] == None else texty[0]
        #pygame.key.name(global_data['nastaveni']['interakce']) if texty[1] == None else texty[1]
        #pygame.key.name(global_data['nastaveni']['exit'])      if texty[2] == None else texty[2]
        #pygame.key.name(global_data['nastaveni']['nahoru'])    if texty[2] == None else texty[3]
        #pygame.key.name(global_data['nastaveni']['dolu'])      if texty[2] == None else texty[4]
        #pygame.key.name(global_data['nastaveni']['doleva'])    if texty[2] == None else texty[5]
        #pygame.key.name(global_data['nastaveni']['doprava'])   if texty[2] == None else texty[6]

    return buttony


def main(global_data):

    velikost_okna = (800, 800) # velikost okna (x, y)
    okno = pygame.display.set_mode(velikost_okna) # vytvori okno

    pygame.display.set_caption("Nastavení") # nastavy nazev okna

    hodiny = pygame.time.Clock() # vyrobi promenou pro casovani a pro limitovani fps
    fps_limit = 60 # maximalni pocet fps

    rozmery_buttonu = [velikost_okna[0] // 7, velikost_okna[1] // 30]

    nadpisy = []

    nadpisy.append(Button(velikost_okna, velikost_okna[0] // 8, 1 * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = 'Inventář', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
    nadpisy.append(Button(velikost_okna, velikost_okna[0] // 8, 2 * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = 'Interakce', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
    nadpisy.append(Button(velikost_okna, velikost_okna[0] // 8, 3 * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = 'Exit', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
    nadpisy.append(Button(velikost_okna, velikost_okna[0] // 8, 4 * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = 'Nahoru', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
    nadpisy.append(Button(velikost_okna, velikost_okna[0] // 8, 5 * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = 'Dolu', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
    nadpisy.append(Button(velikost_okna, velikost_okna[0] // 8, 6 * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = 'Doleva', barva = (0, 0, 0), barva_textu = (255, 255, 255)))
    nadpisy.append(Button(velikost_okna, velikost_okna[0] // 8, 7 * velikost_okna[1] // 8 - rozmery_buttonu[1], rozmery_buttonu[0], rozmery_buttonu[1], text = 'Doprava', barva = (0, 0, 0), barva_textu = (255, 255, 255)))

    buttony_text = [None for _ in range(len(nadpisy))]
    buttony = novyButtony(global_data, velikost_okna, rozmery_buttonu, buttony_text)

    selektnuty_tlacitko = -1

    exit_button = Button(velikost_okna, velikost_okna[0] // 2 - int(rozmery_buttonu[0] * 0.75), velikost_okna[1] - rozmery_buttonu[1] * 3, rozmery_buttonu[0] * 1.5, rozmery_buttonu[1] * 1.5, "Ukoncit Hru")

    programova_smycka = True
    while programova_smycka:
        # kontrola udalosti
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT: # kontroluje kdyz nekdo vykrizkuje z okna
                programova_smycka = False

            if udalost.type == pygame.KEYDOWN:
                global_data['nastaveni'][numNaNastaveni(selektnuty_tlacitko)] = udalost.key#

                buttony_text = [None for _ in range(len(buttony_text))]
                buttony = novyButtony(global_data, velikost_okna, rozmery_buttonu, buttony_text)

                if udalost.key == global_data['nastaveni']['exit'] and selektnuty_tlacitko == -1:
                    programova_smycka = False

                selektnuty_tlacitko = -1

        if global_data['focus_nastaveni']:
            global_data['focus_nastaveni'] = False
            focusWindow()

        if global_data['konec']:
            programova_smycka = False

        pozice_mys = pygame.mouse.get_pos()

        okno.fill((0, 0, 0)) # vybarvy okno aby se resetovalo

        for nadpis in nadpisy:
            nadpis.nakresli(okno)

        for i, button in enumerate(buttony):
            if button.zmacknuti(pozice_mys):

                buttony_text = [None for _ in range(len(buttony_text))]
                buttony_text[i] = '...'
                selektnuty_tlacitko = i

                buttony = novyButtony(global_data, velikost_okna, rozmery_buttonu, buttony_text)

            button.nakresli(okno)

        exit_button.nakresli(okno)
        if exit_button.zmacknuti(pozice_mys):
            global_data['konec'] = True


        pygame.display.update() # nakresli na monitor vsechny vykreslene obrazky

        hodiny.tick(fps_limit) # limituje maximalni pocet fps
