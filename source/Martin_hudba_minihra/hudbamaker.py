import pygame
import random

hudba1=[]
clock = pygame.time.Clock()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Pohyb obdélníků nad a pod středem")

time=0

while True:
    time+=1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:

                print(hudba1)
                hudba1.append([random.randint(1,5),time])
            
    pygame.display.flip()
    clock.tick(60)
