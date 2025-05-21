import pygame
import random
from mince import Mince, spawn, nastav_sance, ziskej_sance


pygame.init()
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kasna s mincemi")
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("Arial", 25)
font_velky = pygame.font.SysFont("Arial", 32)
pocet_minci = random.randint(0, 8)
mince = spawn(pocet_minci) 
penize = 0


kasna = pygame.image.load("kasna.png").convert_alpha()
zem = pygame.image.load("zem.png").convert_alpha()


def main():
    global running, penize  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pozice_mys = pygame.mouse.get_pos()

            for minci in mince[:]: 
                if minci.je_kliknuto(pozice_mys[0], pozice_mys[1]):
                    mince.remove(minci)  
                    penize += minci.hodnota
                    break  

    screen.blit(zem, (0, 0))
    pygame.draw.ellipse(screen, "blue", (-1, 2.5, 800, 500))
    
    screen.blit(kasna, (0, 0))
    text = font.render(f"{penize} Kč", True, "white")
    screen.blit(text, (20, 20))

    for minci in mince:
        minci.vykresli_se(screen)
    
    pygame.display.flip()
    clock.tick(60)

    #global_data['penize'] = penize     # tadyto se bude ukladat v json slozce samo
    #global_data['otevrena_okna'].append('libovolny nazev programu')     # tadyto otevre novy program 'libovolny nazev programu' 

while running:
    main()
pygame.quit()