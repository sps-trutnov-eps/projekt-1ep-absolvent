import pygame
import sys

from button import Button
def Blitni (moznosti,kterou):
    return moznosti[kterou]
textury = [
    {
        "button_1_1":pygame.image.load("textury/voda_button.png"),
        "button_1_2":pygame.image.load("textury/kafe_button.png"),
        "button_1_3":pygame.image.load("textury/energy_maly_button.png"),
        "button_1_4":pygame.image.load("textury/velky_energy.png"),
    },
    
    {
        "button_2_1":pygame.image.load("textury/rohlik_button.png"),
        "button_2_2":pygame.image.load("textury/konzerva_button.png"),
        "button_2_3":pygame.image.load("textury/rohlik_button.png"),
        "button_2_4":pygame.image.load("textury/pizza_button.png"),
    },
    {
        "button_3_1":pygame.image.load("textury/button_batoh_small 1.png"),
        "button_3_2":pygame.image.load("textury/button_batoh_medium 1.png"),
        "button_3_3":pygame.image.load("textury/button_batoh_large 1.png"),
    },
    {
        "preview_1_1":pygame.transform.scale(pygame.image.load("textury/voda1.jpg"),(100,100)),
        "preview_1_2":pygame.transform.scale(pygame.image.load("textury/Kafe250ml.png"),(100,100)),
        "preview_1_3":pygame.transform.scale(pygame.image.load("textury/energy 0,25.png"),(100,100)),
        "preview_1_4":pygame.transform.scale(pygame.image.load("textury/energy 0,5.png"),(100,100)),
    },
    {
        "preview_2_1":pygame.transform.scale(pygame.image.load("textury/rohlik.png"),(100,100)),
        "preview_2_2":pygame.transform.scale(pygame.image.load("textury/konzerva.png"),(100,100)),
        "preview_2_3":pygame.transform.scale(pygame.image.load("textury/rohlik.png"),(100,100)),
        "preview_2_4":pygame.transform.scale(pygame.image.load("textury/pizza.png"),(100,100)),
    },
    {
        "preview_3_1":pygame.transform.scale(pygame.image.load("textury/small batoh-pixilart.png"),(100,100)),
        "preview_3_2":pygame.transform.scale(pygame.image.load("textury/mid batoh-pixilart.png"),(100,100)),
        "preview_3_3":pygame.transform.scale(pygame.image.load("textury/big batoh-pixilar.png"),(100,100)),
        
    },
    {
        "selection_button_1":pygame.image.load("textury/batoh_button - kopie.png"),
        "selection_button_2":pygame.image.load("textury/pití_button - kopie.png"),
        "selection_button_2":pygame.image.load("textury/jídlo_button - kopie.png"),
    },
    {
        "buy_button":pygame.image.load("textury/pizza.png")
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
buttony3 = []
selection_buttons=[]

previews1=[]
previews2=[]
previews3=[]


for j, key in enumerate(textury[0]):
    buttony1.append(Button(100, j*100, textury[0][key]))
    
for j, key in enumerate(textury[1]):
    buttony2.append(Button(100, j * 100, textury[1][key]))

for j, key in enumerate(textury[2]):
    buttony3.append(Button(100, j * 100, textury[2][key]))


moznosti1 = []
moznosti2 = []
moznosti3 = []
moznosti_list= []

for i, key in enumerate(textury[0]):
    moznosti1.append(Button(500, 100*i, textury[0][f"button_1_{i+1}"]))  # "+1" protože klíče mají index od 1
for i, key in enumerate(textury[1]):
    moznosti2.append(Button(500, 100*i, textury[1][f"button_2_{i+1}"]))
for i, key in enumerate(textury[2]):
    moznosti3.append(Button(500, 100*i, textury[2][f"button_3_{i+1}"]))

    
moznosti_list.append(moznosti1)
moznosti_list.append(moznosti2)
moznosti_list.append(moznosti3)
Buy_button = []





for j, key in enumerate(textury[3]):
    previews1.append(textury[3][key])
    
for j, key in enumerate(textury[4]):
    previews2.append(textury[4][key])

for j, key in enumerate(textury[5]):
    previews3.append(textury[5][key])
    
    
for j, key in enumerate(textury[6]):
    selection_buttons.append(Button(50, j * 200, textury[6][key]))
    
for j, key in enumerate(textury[6]):
    Buy_button.append(Button(200, 500, textury[6][key]))


previws_list =[]
previws_list.append(previews1)
previws_list.append(previews2)
previws_list.append(previews3)
    


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