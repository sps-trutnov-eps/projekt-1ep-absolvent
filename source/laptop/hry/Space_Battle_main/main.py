import pygame as pg
import sys
import random
import subprocess
import os



def main(global_data):
    pg.font.init()

    rozliseni_x = 900
    rozliseni_y = 700
    # okinko
    
    
    cesta = os.path.join("..", "laptop", "laptop.py")
    
    obrazek_v_okinku = pg.transform.scale(pg.image.load("hry\\Space_Battle_main\\Nature.jpg"),
                                          (rozliseni_x, rozliseni_y))

    okinko = pg.display.set_mode((rozliseni_x, rozliseni_y))
    # vypsání výhry a prohry
    font = pg.font.Font(pg.font.get_default_font(), 50)

    vyherni_text = font.render("YOU WIN!", True, "green")
    vyherni_text_rect = vyherni_text.get_rect()
    vyherni_text_rect.center = (rozliseni_x/2, rozliseni_y/2)

    proherni_text = font.render("YOU LOSE!", True, "red")
    proherni_text_rect = proherni_text.get_rect()
    proherni_text_rect.center = (rozliseni_x/2, rozliseni_y/2)

    # hráč
    # parametry kanonu
    k_rychlost = 5
    kx = 25
    ky = 50 
    kanon = pg.Rect(rozliseni_x/2 - kx/2, rozliseni_y - ky, kx, ky)
    kanon_barva = (255, 255, 255)

    # střely hráče
    textura_strely = pg.image.load("hry\\Space_Battle_main\\strela.png")
    strely = []
    strely_rychlost = 10

    # nemesis
    nemesis_x = 25
    nemesis_y = 15
    nemesis_barva = "black"
    nemesis_rychlost = 8
    nemesis_skok = 40
    nemesis = []
    nemesis_smer = "prava"

    # střely nepřítele
    sp_width  = 5
    sp_height = 10
    strelyp = []
    strelyp_barva = "blue"
    strelyp_rychlost = 5

    for x in range(10):
        for y in range(6):
            nemesis.append(
                pg.Rect(20 + x * (nemesis_x + 20),
                20 + y * (nemesis_y + 20),
                        nemesis_x, nemesis_y))

    prohra = False

    #fps
    hodiny = pg.time.Clock()

    while True:
        
        # input #
        
        for udalost in pg.event.get():
            # vypnuti krizkem nebo ALT+F4
            if udalost.type == pg.QUIT:
                subprocess.run(["python", cesta])
                sys.exit()
                
            # vypnuti klavesou Escape
            if udalost.type == pg.KEYDOWN:
                if udalost.key == pg.K_ESCAPE:
                    subprocess.run(["python", cesta])
                    sys.exit()
                    
                    
                if udalost.key == pg.K_SPACE:
                    nova_strela = textura_strely.get_rect()
                    nova_strela.midtop = (kanon.centerx, kanon.top)
                    
                    strely.append(nova_strela)
                    
        stisknute_klavesy = pg.key.get_pressed()
                                    
        if stisknute_klavesy[pg.K_LEFT]:  
            kanon.left -= k_rychlost
            if kanon.left <= 0:
                kanon.left = 0
        if stisknute_klavesy[pg.K_RIGHT]:
            kanon.right += k_rychlost
            if kanon.right >= rozliseni_x:
                kanon.right = rozliseni_x
                
        # update #
        # odmazani strely hrace po tom co je moc dlouha  #
        for strela in strely:
            strela.y -= strely_rychlost
            if strela.bottom <= 0:
                strely.remove(strela)
        for strela in strelyp:
            strela.y += strelyp_rychlost
            if strela.top >= rozliseni_y:
                strelyp.remove(strela)
        # odstraneni enemy #
        for strela in strely:
            for nem in nemesis:
                if strela.colliderect(nem):
                    strely.remove(strela)
                    nemesis.remove(nem)
                    
        # zmena smeru #
        for nepritel in nemesis:
            if nemesis_smer == "leva":
                nepritel.x -= nemesis_rychlost
            else:
                nepritel.x += nemesis_rychlost
                
            if random.randint(0, 500) == 0:
                nova_strela = pg.Rect(0, 0, sp_width, sp_height)
                nova_strela.midbottom = (nepritel.centerx, nepritel.bottom)
                
                strelyp.append(nova_strela)
        for strela in strelyp:
            if strela.colliderect(kanon):
                strelyp.remove(strela)
                prohra = True
        prev_smer = nemesis_smer
        
        for nepritel in nemesis:
            if nepritel.right >= rozliseni_x:
                nemesis_smer = "leva"
            elif nepritel.left <= 0:
                nemesis_smer = "prava"
                
        if nemesis_smer != prev_smer:
            for nepritel in nemesis:
                nepritel.y += nemesis_skok
                
                if nepritel.bottom > kanon.top:
                    prohra = True
            
        # draw #
        
        okinko.blit(obrazek_v_okinku, (0,0))  
        
        for trouba in nemesis:
            pg.draw.rect(okinko, nemesis_barva, trouba)
        for strela in strely:
            okinko.blit(textura_strely, strela)
            
        for strela in strelyp:
            pg.draw.rect(okinko, strelyp_barva, strela)
            
        pg.draw.rect(okinko, kanon_barva, kanon)
        
        if len(nemesis) == 0:
            okinko.blit(vyherni_text, vyherni_text_rect)
            
        if prohra:
            okinko.fill("black")
            okinko.blit(proherni_text, proherni_text_rect)
        
        pg.display.update()
        hodiny.tick(60)
     
