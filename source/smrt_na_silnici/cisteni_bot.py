import pygame
import random
import sys

rozliseni_x = 800
rozliseni_y = 600

obrazovka = pygame.display.set_mode((rozliseni_x, rozliseni_y))

barva_pozadi = ("red")

while True:
    for udalost in pygame.event.get():
        # vypnuti krizkem nebo ALT+F4
        if udalost.type == pygame.QUIT:
            sys.exit()
        # vypnuti klavesou Escape
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                sys.exit()
    obrazovka.fill(barva_pozadi)
    pygame.display.update()
    
        
            