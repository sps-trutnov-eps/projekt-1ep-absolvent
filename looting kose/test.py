import pygame
import sys
import random

okraje = 20

rozliseni_x = 300 + 2*okraje
rozliseni_y = rozliseni_x

okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))

cerna = (0, 0, 0)

#grid properties
velikost_ctverecku = 93 + 1/3
gap = 10
velikost_gridu = 3
start_x = okraje
start_y = start_x

while True:
    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    okno.fill(cerna)

    for row in range(velikost_gridu):
        for col in range(velikost_gridu):
            x = start_x + col * (velikost_ctverecku + gap)
            y = start_y + row * (velikost_ctverecku + gap)

            barva_r = random.randint(0, 255)
            barva_g = random.randint(0, 255)
            barva_b = random.randint(0, 255)

            random_barva = (barva_r, barva_g, barva_b)

            pygame.draw.rect(okno, random_barva, (x, y, velikost_ctverecku, velikost_ctverecku))
            pygame.draw.rect(okno, random_barva, (x, y, velikost_ctverecku, velikost_ctverecku), 2)

    pygame.display.flip()