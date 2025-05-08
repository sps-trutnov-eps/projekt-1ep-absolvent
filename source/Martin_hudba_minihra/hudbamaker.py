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
                height = random.randint(1,5)
                if height <= 2:
                    color=(255,0,0)
                elif height >= 3:
                    color=(0,0,255)
                if  height == 3:
                    color=(255,0,250)

                print(hudba1)
                hudba1.append([height,time,color])
            
    pygame.display.flip()
    clock.tick(60)
