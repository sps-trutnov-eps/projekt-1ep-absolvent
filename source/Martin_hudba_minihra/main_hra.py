import pygame 
def main(global_data):
    pygame.init()
    poloha_x =800
    notove = [[5, 187, (0, 0, 255)], [1, 193, (255, 0, 0)], [1, 200, (255, 0, 0)], [1, 205, (255, 0, 0)], [3, 207, (255, 0, 250)], [5, 214, (0, 0, 255)], [5, 218, (0, 0, 255)], [2, 222, (255, 0, 0)], [2, 226, (255, 0, 0)], [1, 231, (255, 0, 0)], [5, 244, (0, 0, 255)], [4, 249, (0, 0, 255)], [3, 253, (255, 0, 250)], [1, 258, (255, 0, 0)], [2, 263, (255, 0, 0)], [1, 266, (255, 0, 0)], [1, 271, (255, 0, 0)], [2, 291, (255, 0, 0)], [1, 296, (255, 0, 0)], [2, 301, (255, 0, 0)], [5, 305, (0, 0, 255)], [1, 311, (255, 0, 0)], [4, 314, (0, 0, 255)], [5, 321, (0, 0, 255)], [2, 325, (255, 0, 0)], [1, 330, (255, 0, 0)], [2, 336, (255, 0, 0)], [5, 339, (0, 0, 255)], [5, 341, (0, 0, 255)], [2, 346, (255, 0, 0)], [1, 351, (255, 0, 0)], [3, 355, (255, 0, 250)], [3, 359, (255, 0, 250)], [4, 364, (0, 0, 255)], [3, 369, (255, 0, 250)], [2, 373, (255, 0, 0)], [2, 380, (255, 0, 0)], [3, 390, (255, 0, 250)], [1, 400, (255, 0, 0)], [4, 405, (0, 0, 255)], [5, 410, (0, 0, 255)], [1, 415, (255, 0, 0)], [5, 419, (0, 0, 255)], [1, 426, (255, 0, 0)], [2, 436, (255, 0, 0)], [5, 442, (0, 0, 255)], [1, 459, (255, 0, 0)], [1, 464, (255, 0, 0)], [3, 470, (255, 0, 250)], [2, 476, (255, 0, 0)], [5, 481, (0, 0, 255)], [2, 487, (255, 0, 0)], [4, 492, (0, 0, 255)], [1, 498, (255, 0, 0)], [2, 503, (255, 0, 0)], [1, 508, (255, 0, 0)], [1, 514, (255, 0, 0)], [5, 525, (0, 0, 255)], [3, 530, (255, 0, 250)], [1, 536, (255, 0, 0)], [3, 541, (255, 0, 250)], [3, 547, (255, 0, 250)], [5, 553, (0, 0, 255)], [1, 568, (255, 0, 0)], [5, 574, (0, 0, 255)], [2, 579, (255, 0, 0)], [2, 584, (255, 0, 0)], [1, 590, (255, 0, 0)], [1, 595, (255, 0, 0)], [2, 601, (255, 0, 0)], [5, 607, (0, 0, 255)], [2, 612, (255, 0, 0)], [3, 618, (255, 0, 250)], [3, 624, (255, 0, 250)], [5, 630, (0, 0, 255)], [3, 635, (255, 0, 250)], [2, 640, (255, 0, 0)], [5, 646, (0, 0, 255)], [1, 652, (255, 0, 0)], [1, 657, (255, 0, 0)], [5, 662, (0, 0, 255)], [4, 668, (0, 0, 255)], [5, 673, (0, 0, 255)], [1, 678, (255, 0, 0)], [3, 684, (255, 0, 250)], [5, 691, (0, 0, 255)], [5, 695, (0, 0, 255)], [5, 700, (0, 0, 255)], [4, 707, (0, 0, 255)], [1, 712, (255, 0, 0)], [4, 716, (0, 0, 255)], [4, 728, (0, 0, 255)], [2, 733, (255, 0, 0)], [5, 739, (0, 0, 255)], [1, 744, (255, 0, 0)], [1, 750, (255, 0, 0)], [4, 756, (0, 0, 255)], [1, 761, (255, 0, 0)], [2, 767, (255, 0, 0)], [5, 773, (0, 0, 255)], [2, 779, (255, 0, 0)], [3, 789, (255, 0, 250)], [2, 795, (255, 0, 0)], [2, 800, (255, 0, 0)], [4, 807, (0, 0, 255)], [2, 812, (255, 0, 0)], [4, 818, (0, 0, 255)], [4, 824, (0, 0, 255)], [4, 830, (0, 0, 255)], [5, 836, (0, 0, 255)], [2, 841, (255, 0, 0)], [1, 847, (255, 0, 0)], [4, 853, (0, 0, 255)], [1, 859, (255, 0, 0)], [2, 870, (255, 0, 0)], [4, 876, (0, 0, 255)], [5, 890, (0, 0, 255)], [4, 908, (0, 0, 255)], [3, 913, (255, 0, 250)], [3, 920, (255, 0, 250)], [2, 926, (255, 0, 0)], [5, 931, (0, 0, 255)], [3, 937, (255, 0, 250)], [3, 943, (255, 0, 250)], [1, 948, (255, 0, 0)], [1, 954, (255, 0, 0)], [2, 960, (255, 0, 0)], [4, 966, (0, 0, 255)], [1, 972, (255, 0, 0)], [5, 977, (0, 0, 255)], [4, 983, (0, 0, 255)], [1, 989, (255, 0, 0)], [5, 995, (0, 0, 255)], [5, 1000, (0, 0, 255)], [2, 1005, (255, 0, 0)], [2, 1011, (255, 0, 0)], [3, 1017, (255, 0, 250)], [4, 1023, (0, 0, 255)], [3, 1029, (255, 0, 250)], [2, 1034, (255, 0, 0)], [5, 1041, (0, 0, 255)], [4, 1047, (0, 0, 255)], [1, 1052, (255, 0, 0)], [4, 1059, (0, 0, 255)], [3, 1064, (255, 0, 250)], [1, 1069, (255, 0, 0)], [1, 1075, (255, 0, 0)], [5, 1080, (0, 0, 255)], [2, 1086, (255, 0, 0)], [1, 1091, (255, 0, 0)], [4, 1097, (0, 0, 255)], [1, 1102, (255, 0, 0)], [1, 1107, (255, 0, 0)], [5, 1113, (0, 0, 255)], [3, 1118, (255, 0, 250)], [3, 329899999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999, (255, 0, 250)]]


    ktera_nota = 1
    aktivni = 0
    aktivni_noty = []
    kdy = 0
    # Nastavení velikosti okna
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pohyb obdélníků nad a pod středem")

  

    # Barvy
    b=255
    # Načtení obrázků
    modry = pygame.image.load("bitmapa.png")
    cerveny = pygame.image.load("bitmapa2.png")

    # Získání rectů
    modry_rect = modry.get_rect()
    cerveny_rect = cerveny.get_rect()

    # Nastavení počátečních pozic
    modry_rect.topleft = (10, (screen.get_height() // 2) - modry_rect.height)
    cerveny_rect.topleft = (10, (screen.get_height() // 2))
    skore=0
    noooooooooooooooooooooooooobe=0    # Rychlost pohybu
    move_speed = 5
    barva_pozadi = (255, 255, 255)
    # Hlavní smyčka hry
    running = True
    clock = pygame.time.Clock()
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    for n in aktivni_noty.copy():
                        nota_rect=n[0]  
                        if modry_rect.colliderect(nota_rect) or cerveny_rect.colliderect(nota_rect):
                            if n[2] !=(255,0,250): 
                                aktivni_noty.remove(n)
                                skore+=1
                        if modry_rect.colliderect(nota_rect) and cerveny_rect.colliderect(nota_rect):
                            if n[2] ==(255,0,250): 
                                aktivni_noty.remove(n)
                                skore+=1
                    b=150
        barva_pozadi = (b,b,b)
        if b<255:
            b+=3
        # Získání stavu klávesnice
        keys = pygame.key.get_pressed()

        # Pohyb modrého
        
        if keys[pygame.K_UP]:
            modry_rect.y -= move_speed
        if keys[pygame.K_DOWN]:
            modry_rect.y += move_speed

        # Pohyb červeného
        if keys[pygame.K_w]:
            cerveny_rect.y -= move_speed
        if keys[pygame.K_s]:
            cerveny_rect.y += move_speed

        kdy +=5

        if notove[ktera_nota][1]==kdy/5:
                aktivni = 1
          

        for i in range(aktivni):
                
                poloha_y = notove[ktera_nota][0]*100
                barva  = notove[ktera_nota][2]
                ktera_nota += 1
                nota=pygame.Rect(poloha_x,poloha_y,20,40)
                aktivni_noty.append([nota,aktivni,barva])
                aktivni = 0

        screen.fill(barva_pozadi)

        for o in aktivni_noty.copy():
            rect_nota = o[0]
            barva = o[2]
            rect_nota.x -= 5 
            
            pygame.draw.rect(screen, barva, rect_nota)
            if rect_nota.x+20 < 0:
                aktivni_noty.remove(o)
                noooooooooooooooooooooooooobe+=1  # Volitelně odstraníš notu mimo obrazovku

        # Omez pohyb na okno
        modry_rect.y = max(0, min(modry_rect.y, screen.get_height() - modry_rect.height))
        cerveny_rect.y = max(0, min(cerveny_rect.y, screen.get_height() - cerveny_rect.height))
        print(noooooooooooooooooooooooooobe)
        print(skore)
        print()
        # Vyplnění obrazovky

        # Vykreslení obrázků pomocí blit
        screen.blit(modry, modry_rect.topleft)
        screen.blit(cerveny, cerveny_rect.topleft)

       
        # Aktualizace obrazovky
        pygame.display.flip()
        clock.tick(60)
