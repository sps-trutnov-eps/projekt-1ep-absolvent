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
                color =random.randint(1,3000)
                if color<=1000:
                    color=1
                elif color<=2000:
                    color=2
                else:
                    color=3

                print(hudba1)
                hudba1.append([random.randint(1,5),time,color])
            
    pygame.display.flip()
    clock.tick(60)
