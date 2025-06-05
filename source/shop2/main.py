import pygame
import sys 
from button import Button

textury = [
    {
        "button_1_1":pygame.image.load("textury/batoh1.png"),
        "button_1_2":pygame.image.load("textury/batoh2.png"),
        "button_1_3":pygame.image.load("textury/batoh3.png"),
        "button_1_4":pygame.image.load("textury/batoh4.png"),
    },
    {
        "button_2_1":pygame.image.load("textury/pití1.png"),
        "button_2_2":pygame.image.load("textury/pití2.png"),
        "button_2_3":pygame.image.load("textury/pití3.png"),
        "button_2_4":pygame.image.load("textury/pití4.png"),
    },
    {
        "preview_1_1":pygame.transform.scale(pygame.image.load("textury/batoh1.png"),(100,100)),
        "preview_1_2":pygame.transform.scale(pygame.image.load("textury/batoh2.png"),(100,100)),
        "preview_1_3":pygame.transform.scale(pygame.image.load("textury/batoh3.png"),(100,100)),
        "preview_1_4":pygame.transform.scale(pygame.image.load("textury/batoh4.png"),(100,100)),
    },
    {
        "preview_2_1":pygame.transform.scale(pygame.image.load("textury/pití1.png"),(100,100)),
        "preview_2_2":pygame.transform.scale(pygame.image.load("textury/pití2.png"),(100,100)),
        "preview_2_3":pygame.transform.scale(pygame.image.load("textury/pití3.png"),(100,100)),
        "preview_2_4":pygame.transform.scale(pygame.image.load("textury/pití4.png"),(100,100)),
    },
    {
        "selection_button_1":pygame.image.load("textury/Button_back.png"),
        "selection_button_2":pygame.image.load("textury/Button_back.png"),
    }
]

textury[0]["button_1_1"]

backround=pygame.image.load("textury/pozadí_shopu.png")

shop = True 
x,y = 800,600
buttony = []
buttony2 = []

for j, i in enumerate(textury):
    buttony.append(Button(100, j*100, textury[0][i]))
    buttony2.append(Button(100, j*100, textury[1][i]))

    


screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("Cigansky obchod")

while shop:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shop = False

    click = pygame.mouse.get_pressed()

    screen.blit(backround, (0, 0))
    for i in buttony:
        i.draw(screen)

    if i.collide(mouse_pos) and click[0]:
        i.funkce()

            
    









    pygame.display.flip()

pygame.quit()
sys.exit()