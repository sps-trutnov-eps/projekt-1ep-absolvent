from Shop import Shop    
import pygame
import sys
import random
import math

pygame.init()
option_1 = pygame.image.load("batoh1.png")
preview1_1 = pygame.image.load("batoh2.png")
preview1_2 = pygame.image.load("batoh3.png")
preview1_3 = pygame.image.load("batoh4.png")
pozice_option_1 =option_1.get_rect(topleft=(200, 200))

option_2 = pygame.image.load("pití1.png")
preview2_1 = pygame.image.load("pití2.png")
preview2_2 = pygame.image.load("pití3.png")
preview2_3 = pygame.image.load("pití4.png")
pozice_option_2 =option_2.get_rect(topleft=(200, 400))





Button_leave = pygame.image.load("Button_back.png")

pozice1 = preview1_1.get_rect(topleft=(200, 878))
pozice2 = preview1_1.get_rect(topleft=(200, 744))
pozice3 = preview1_1.get_rect(topleft=(200, 615))

main_buttony = {
"option_1":option_1,
"pozice_option_1":pozice_option_1,#nazev_obrazku.get_rect(topleft=(pozice_x, pozice_y))

"option_2": option_2,
"pozice_option_2":pozice_option_2,

"preview1_1":preview1_1,
"preview1_2":preview1_2,
"preview1_3": preview1_3,

"preview2_1":preview2_1,
"preview2_2":preview2_2,
"preview2_3":preview2_3,

"option_1_1_button":preview1_1,
"option_1_2_button":preview1_2,
"option_1_3_button":preview1_3,

"option2_1button":preview2_1,
"option2_2button":preview2_2,
"option2_3button":preview2_3,


"pozice_buttonu1":pozice1,
"pozice_buttonu2":pozice2,
"pozice_buttonu3":pozice3,
}

obrazovka = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Shop")
Obchod = Shop(main_buttony,shop_image)

while shop:
    
    for udalost in pygame.event.get():

        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    white = (255,255,255)    
    obrazovka.fill( white )        
    Obchod.draw_shop(obrazovka)
    Obchod.choose(udalost,obrazovka)
    Obchod.opustit_shop(obrazovka,Button_leave,udalost)

    shop = Obchod.shop
    Lobby = Obchod.lobby


    pygame.display.flip()

    # Nastavení FPS
