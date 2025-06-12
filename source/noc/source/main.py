import random
import pygame
pygame.font.init()
from source.ohen import Ohen

rozliseni_x = 800
rozliseni_y = 600

fps = 60

okno = pygame.display.set_mode((rozliseni_x, rozliseni_y))
pygame.display.set_caption("Bobek")

ai_difficulty_ohen = random.randint(2, 6)
ohen_stage = 5

ohen_blit_timer = fps / (17 / 10)
faze = 0

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

    #img load
    if ohen_stage != 0:
        file_name = f"ohen_S{ohen_stage}//ohen_S{ohen_stage}_F{faze}"

    ohen_img = pygame.image.load(f"source//noc//textury//{file_name}.png")
    ohen_img_rect = ohen_img.get_rect(center= ((rozliseni_x / 2), (rozliseni_y / 2)))

    if ohen_blit_timer > 0:
        ohen_blit_timer -= 1

    if ohen_blit_timer <= 0:
        faze += 1
        ohen_blit_timer = fps / (17 / 10)

    if faze > 2:
        faze = 0

    if ohen_stage < 1:
        game = False

    okno.blit(ohen_img, ohen_img_rect)

    pygame.display.flip()