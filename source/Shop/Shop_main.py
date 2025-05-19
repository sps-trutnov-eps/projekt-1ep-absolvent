from Shop import Shop    
import pygame
import sys
import random
import math
def main(global_data):
    pygame.init()
    main_buttony = {
        "option_1":button_planes,
        "pozice_option_1":pozice_planes,
        
        "option_2": button_rockets,
        "pozice_option_2":pozice_rockets,
        
        "upgrady":button_upgrades,
        "pozice_upgrady":pozice_upgrades,
        
        "preview1/2":myg,
        "preview1/1":fockerfox,
        "preview1/3": f,
        
        "preview2/1":raketa_shop1,
        "preview2/2":raketa_shop2,
        "preview2/3":raketa_shop3,

        "list2animace2/1":Raketa1,
        "list2animace2/2":Raketa2,
        "list2animace2/3":Raketa3,
        
        "option1/2button":myg_button,
        "option1/3button":fbutton,
        "option1/1button":fockerfox_button,
        
        "option2/1button":button_raketa1,
        "option2/2button":button_raketa2,
        "option2/3button":button_raketa3,

        
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
        clock.tick(60)