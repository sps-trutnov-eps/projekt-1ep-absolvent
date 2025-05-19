import random
import pygame
pygame.font.init()
from ohen import Ohen

rozliseni_x = 800
rozliseni_y = 600

fps = 60

okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))
pygame.display.set_caption("Bobek")

ai_difficulty_ohen = random.randint(2, 5)
ohen_stage = 5

cerna = (0, 0, 0)
bila = (255, 255, 255)

font = pygame.font.SysFont("Calibri", 48)

fps_casovac = pygame.time.Clock()

ohen = Ohen(okno, rozliseni_x, rozliseni_y, fps, cerna, bila, font)

game = True
while game:
    udalosti = pygame.event.get()
    for udalost in udalosti:
        if udalost.type == pygame.QUIT:
            game = False
    
    fps_casovac.tick(fps)

    okno.fill(cerna)
    ohen_stage = ohen.ai(ai_difficulty_ohen, ohen_stage)

    pygame.display.flip()