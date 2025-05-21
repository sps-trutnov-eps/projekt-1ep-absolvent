import pygame
import random
from mince import Mince, spawn, nastav_sance, ziskej_sance
penize = 0

# Inicializace
pygame.init()
width, height = 800, 500
screen = pygame.display.set_mode((width, height))
menu_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Kasna s mincemi")
clock = pygame.time.Clock()
running = True
font = pygame.font.SysFont("Arial", 25)
font_velky = pygame.font.SysFont("Arial", 32)
pocet_minci = random.randint(0, 8)
mince = spawn(pocet_minci) 

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Získání pozice myši
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pozice_mys = pygame.mouse.get_pos()
                
            # Kontrola kliknutí na každou minci
            for minci in mince[:]:  
                if minci.je_kliknuto(pozice_mys[0], pozice_mys[1]):
                    mince.remove(minci)  
                    penize += minci.hodnota
                    break  
    

    screen.fill("grey")
    pygame.draw.ellipse(screen, "blue", (width/2-300, height/2-200, 600, 400))
    

    text = font.render(f"{penize} Kč", True, "black")
    screen.blit(text, (20, 20))
    
    # Vykreslovani minci
    for minci in mince:
        minci.vykresli_se(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()