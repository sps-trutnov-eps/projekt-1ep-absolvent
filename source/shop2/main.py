import pygame
import sys

from button import Button
def Blitni (moznosti,kterou):
    return moznosti[kterou]
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
    },
    {
        "buy_button":pygame.image.load("textury/Button_back.png")
    }
]






shop = True 
x, y = 1920, 1080
backround = pygame.image.load("textury/pozadí_shopu.png")
backround = pygame.transform.scale(backround, (x, y))


chosen=0
choise = 0
buttony1 = []
buttony2 = []
selection_buttons=[]

previews1=[]
previews2=[]

for j, key in enumerate(textury[0]):
    buttony1.append(Button(100, j*100, textury[0][key]))
    
for j, key in enumerate(textury[1]):
    buttony2.append(Button(100, j * 100, textury[1][key]))

moznosti1 = []
moznosti2 = []
moznosti_list= []

for i in range(1,5):
    moznosti1.append(Button(500,100*i, textury[0][f"button_1_{i}"] ))
    moznosti2.append(Button(500,100*i, textury[1][f"button_2_{i}"] ))
    
moznosti_list.append(moznosti1)
moznosti_list.append(moznosti2)
Buy_button = []





for j, key in enumerate(textury[2]):
    previews1.append(textury[2][key])
    
for j, key in enumerate(textury[3]):
    previews2.append(textury[3][key])
    
for j, key in enumerate(textury[4]):
    selection_buttons.append(Button(50, j * 200, textury[4][key]))
    
for j, key in enumerate(textury[5]):
    Buy_button.append(Button(200, 500, textury[5][key]))


previws_list =[]
previws_list.append(previews1)
previws_list.append(previews2)
    


screen = pygame.display.set_mode((x, y))
pygame.display.set_caption("obchod")

while shop:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shop = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            klik = True
        else:
            klik= False



    screen.blit(backround, (0, 0))
    
    for j,i in enumerate(selection_buttons):
        i.draw(screen)
        if i.collide(mouse_pos) and klik:
            choise=j

    for j,i in enumerate(Blitni(moznosti_list,choise)):
        i.draw(screen)

        if i.collide(mouse_pos) and klik:
            chosen=j
    for j,i in enumerate (Buy_button):
        i.draw(screen)
        if i.collide(mouse_pos) and klik:
            huijk=4

    screen.blit(previws_list[choise][chosen],(100,500))











    pygame.display.flip()

pygame.quit()
sys.exit()