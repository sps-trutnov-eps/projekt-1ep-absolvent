import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

# sem piste importy
import pygame
import random
import sys

def main(global_data):
    rozliseni_x = 1920
    rozliseni_y = 1080

    hrac_x = 30
    hrac_y = 30
    hrac = pygame.Rect(rozliseni_x/2 - hrac_x/2,rozliseni_y-1.5*hrac_y, hrac_x, hrac_y)
    hrac_barva = "green"
    hrac_rychlost = 3


    zobrazovacka = pygame.display.set_mode((rozliseni_x, rozliseni_y))
    pygame.display.set_caption("ŽIVOT")#("minihra - Smrt na silnici")
    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)

    silnice_x = rozliseni_x
    silnice_y = 60
    silnice = pygame.image.load("silnice3.png")
    #zacatek silnice = 50
    #konec silnice = 950
    chodnik = pygame.image.load("chodnik.png").convert_alpha()
    
    auticko_x = 80
    auticko_y = 40
    #bus = 200
    #vlak = 700
    obrazky_aut = [
        pygame.image.load("tyrak.png").convert_alpha(),
        pygame.image.load("kia.png").convert_alpha(),
        pygame.image.load("f1.png").convert_alpha(),
        pygame.image.load("911.png").convert_alpha(),
        pygame.image.load("smart.png").convert_alpha(),
        pygame.image.load("tyrak-bedna.png").convert_alpha(),
        ]

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
            smer = random.choice((-1,1))
            if pruh["autaci"] == []:
                rychlost = random.random() * 3 + 3
                for i in range(random.randint(1,3)):
                    obrazek = random.choice(obrazky_aut)
                    if smer == -1:
                        obrazek = pygame.transform.flip(obrazek, True, False)
        
                    if smer == 1:
                        pruh["autaci"].append({
                            "rect": pygame.Rect(-auticko_x - i*random.randint(auticko_x*1.25, auticko_x*1.5)*(-1 if rychlost < 0 else 1), pruh["rect"].y+10, auticko_x, auticko_y),
                            "obrazek": obrazek,
                            "rychlost": rychlost
                        })

                    elif smer == -1:
                        pruh["autaci"].append({
                            "rect": pygame.Rect(auticko_x + silnice_x - i*random.randint(auticko_x*1.25, auticko_x*1.5)*(1 if rychlost < 0 else -1), pruh["rect"].y+10, auticko_x, auticko_y),
                            "obrazek": obrazek,
                            "rychlost": -rychlost
                        })
                    obrazek = random.choice(obrazky_aut)
                    if smer == -1:
                        obrazek = pygame.transform.flip(obrazek, True, False)

            for auto in pruh["autaci"]:
                if auto["rect"].colliderect(hrac):
                    hrac = pygame.Rect(rozliseni_x/2 - hrac_x/2,rozliseni_y-1.5*hrac_y, hrac_x, hrac_y)
                    zivoty -= 1
                    if zivoty == 0:
                        prohra = True

            zobrazovacka.blit(silnice, pruh["rect"])  
            zobrazovacka.blit(chodnik, (0, -80))
            zobrazovacka.blit(chodnik,(1024,-80))
            zobrazovacka.blit(chodnik,(0,1010))
            zobrazovacka.blit(chodnik,(1024,1010))
            
            temp_autaci = pruh["autaci"].copy()
            for tacoauto in pruh["autaci"]:
                tacoauto["rect"].x += tacoauto["rychlost"]
                zobrazovacka.blit(tacoauto["obrazek"], tacoauto["rect"])


                if tacoauto["rychlost"] > 0:
                    if tacoauto["rect"].x > rozliseni_x:
                        temp_autaci.remove(tacoauto)
                        
                if tacoauto["rychlost"] < 0:
                    if tacoauto["rect"].x < - auticko_x:
                        temp_autaci.remove(tacoauto)
            
            pruh['autaci'] = temp_autaci.copy()
                        
                
        pygame.draw.rect(zobrazovacka, hrac_barva,hrac)
        
        zivoty_text = font.render(f"Životy: {zivoty}", True, (255, 0, 0))
        zobrazovacka.blit(zivoty_text, (10, 10))
        
        if prohra == True:
            zobrazovacka.fill("blue")
            pygame.display.set_caption("NO ŽIVOT")
        
        pygame.display.update()
        hodiny.tick(60)
    # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"

if __name__ == "__main__":
    masterFunc(novyProgram(main))
