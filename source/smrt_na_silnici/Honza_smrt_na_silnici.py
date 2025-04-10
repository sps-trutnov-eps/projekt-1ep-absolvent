import pygame
import random
import sys

rozliseni_x = 1920
rozliseni_y = 1080

hrac_x = 30
hrac_y = 30
hrac = pygame.Rect(rozliseni_x/2 - hrac_x/2,rozliseni_y-1.5*hrac_y, hrac_x, hrac_y)
hrac_barva = "green"
hrac_rychlost = 3


zobrazovacka = pygame.display.set_mode((rozliseni_x, rozliseni_y))
pygame.display.set_caption("ŽIVOT")#("minihra - Smrt na silnici")

silnice_x = rozliseni_x
silnice_y = 60

auticko_x = 80
auticko_y = 40
auticko_rychlost = 5
#bus = 200
#vlak = 700

vstup_x = rozliseni_x
vstup_y = 300

safeplace_x = rozliseni_x/2
safeplace_y = vstup_y

exidus_x = 300
exidus_y = vstup_y

prohra = False

hodiny = pygame.time.Clock()
pruhy = []
zivoty = 3

for i in range(16):
    pruhy.append({
        'barva': "black",
        'rect': pygame.Rect(0, (i*silnice_y+50), rozliseni_x, silnice_y),
        'autaci': []
        })

while True:
    ##########################################
    #klikanie
    ##########################################
    for udalost in pygame.event.get():
        # vypnuti krizkem nebo ALT+F4
        if udalost.type == pygame.QUIT:
            sys.exit()
        # vypnuti klavesou Escape
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                sys.exit()
    hold = pygame.key.get_pressed()
    if hold[pygame.K_UP]:
        hrac.top -= hrac_rychlost
    if hold[pygame.K_LEFT]:
        hrac.left -= hrac_rychlost
        if hrac.left <= 0:
            hrac.left = 0
    if hold[pygame.K_RIGHT]:
        hrac.right += hrac_rychlost
        if hrac.right >= rozliseni_x:
            hrac.right = rozliseni_x
    if hold[pygame.K_DOWN]:
        hrac.bottom += hrac_rychlost
    ##########################################
    ##########################################
        
    
    #vykresleni
    zobrazovacka.fill("white")
    for pruh in pruhy:
        sisedevjet = random.choice((-1,1))
        if pruh["autaci"] == []:
            if sisedevjet == 1:
                pruh["autaci"].append({
                    "rect": pygame.Rect(-auticko_x, pruh["rect"].y+10, auticko_x, auticko_y),
                    "barva": (random.randint(0, 255), random.randint(0, 255) ,random.randint(0, 255)),
                    "rychlost": random.random() * 4 + 3
                    })
            elif sisedevjet == -1:
                pruh["autaci"].append({
                    "rect": pygame.Rect(silnice_x, pruh["rect"].y+10, auticko_x, auticko_y),
                    "barva": (random.randint(0, 255), random.randint(0, 255) ,random.randint(0, 255)),
                    "rychlost": -(random.random() * 4 + 3)
                    })
        for auto in pruh["autaci"]:
            if auto["rect"].colliderect(hrac):
                hrac = pygame.Rect(rozliseni_x/2 - hrac_x/2,rozliseni_y-1.5*hrac_y, hrac_x, hrac_y)
                zivoty -= 1
                if zivoty == 0:
                    prohra = True
                
            
            
        pygame.draw.rect(zobrazovacka, pruh["barva"], pruh["rect"])
        for autako in pruh["autaci"]:
            autako["rect"].x += autako["rychlost"]
            pygame.draw.rect(zobrazovacka, autako["barva"], autako["rect"])
            if autako["rect"].x < -auticko_x or autako["rect"].x > silnice_x:
                pruh["autaci"].remove(autako)
            
    pygame.draw.rect(zobrazovacka, hrac_barva,hrac)
    if prohra == True:
        zobrazovacka.fill("black")
        pygame.display.set_caption("NO ŽIVOT")
    
    pygame.display.update()
    hodiny.tick(60)
    
    

