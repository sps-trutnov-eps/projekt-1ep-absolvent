import pygame
import random
from mince import Mince, spawn
penize = 0

pygame.init()
screen = pygame.display.set_mode((800, 500))
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("Arial", 25)
pocet_minci = random.randint(0, 10)
mince = spawn(pocet_minci) 

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #získání pozice myši
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pozice_mys = pygame.mouse.get_pos()
            # Kontrola kliknutí na každou minci
            for minci in mince[:]:  
                if minci.je_kliknuto(pozice_mys[0], pozice_mys[1]):
                    mince.remove(minci)  
                    penize += minci.hodnota
                    break  
    
    #vykreslování pozadí a vody a peněz
    screen.fill("grey")
    pygame.draw.ellipse(screen, "blue", (800/2-300, 500/2-200, 600, 400))
    text = font.render(str(penize), True, "black")
    screen.blit(text, (0, 0))
    
    #vykreslovani minci
    for minci in mince:
        minci.vykresli_se(screen)

    pygame.display.flip()
    clock.tick(60)
pygame.quit()