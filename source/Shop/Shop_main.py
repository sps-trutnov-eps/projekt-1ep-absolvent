from Shop import Shop    
import pygame
import sys
import random
import math
def main(global_data):
    pygame.init()
    main_buttony = {
        "letadla":button_planes,
        "pozice_letadla":pozice_planes,
        
        "rakety": button_rockets,
        "pozice_rakety":pozice_rockets,
        
        "upgrady":button_upgrades,
        "pozice_upgrady":pozice_upgrades,
        
        "myg25":myg,
        "fockerfox":fockerfox,
        "F23": f,
        
        "raketa1":raketa_shop1,
        "raketa2":raketa_shop2,
        "raketa3":raketa_shop3,

        "raketa11":Raketa1,
        "raketa22":Raketa2,
        "raketa33":Raketa3,
        
        "myg_button":myg_button,
        "f_button":fbutton,
        "fockerfox_button":fockerfox_button,
        
        "r_b_1":button_raketa1,
        "r_b_2":button_raketa2,
        "r_b_3":button_raketa3,

        
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