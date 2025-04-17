import pygame 
def main(global_data):
    pygame.init()
    poloha_x =800
    notove = [[4, 27], [2, 32], [5, 37], [4, 43], [3, 49], [1, 53], [2, 58], [2, 64], [3, 112], [3, 119], [5, 161], [3, 167], [3, 172], [4, 178], [5, 184], [5, 190], [1, 195], [1, 200], [3, 206], [5, 211], [3, 217], [1, 223], [3, 228], [2, 233], [4, 238], [3, 243], [3, 249], [5, 254], [4, 260], [4, 265], [1, 271], [4, 282], [3, 287], [3, 292], [2, 350], [5, 361], [2, 373], [3, 382], [1, 384], [3, 390], [2, 393], [2, 402], [1, 407], [1, 412], [1, 416], [3, 421], [3, 426], [4, 430], [2, 436], [2, 439], [2, 444], [1, 448], [5, 455], [3, 459], [1, 464], [3, 469], [2, 474], [1, 479], [3, 483], [5, 488], [1, 491], [5, 494], [5, 498], [3, 505], [1, 509], [1, 514], [2, 518], [4, 525], [3, 530], [1, 535], [3, 539], [5, 545], [4, 549], [2, 554], [3, 570], [1, 581], [3, 586], [4, 590], [2, 597], [5, 602], [3, 607], [4, 613], [4, 618], [5, 623], [5, 629], [1, 635], [5, 640], [3, 646], [3, 651], [3, 656], [5, 662], [3, 667], [4, 685], [5, 692], [4, 698], [2, 704], [1, 709], [5, 714], [2, 718], [3, 724], [1, 729], [1, 734], [2, 740], [4, 745], [5, 761], [5, 777], [5, 782], [4, 793], [2, 799], [2, 805], [4, 810], [1, 815], [5, 821], [1, 826], [3, 832], [5, 837], [1, 843], [1, 847], [5, 853], [2, 858], [3, 863], [5, 869], [4, 874], [3, 878], [5, 885], [3, 891], [3, 896], [1, 901], [3, 906], [1, 912], [2, 917], [4, 922], [2, 928], [4, 934], [5, 938], [3, 945], [3, 950], [1, 956], [2, 960], [2, 971], [5, 976], [2, 982], [2, 987], [4, 992], [3, 998], [4, 1003], [1, 1008], [1, 1013], [2, 1019], [2, 1024], [3, 1036], [4, 1040], [3, 1083], [1, 1088], [4, 1104], [5, 1136], [4, 1146], [1, 1162], [4, 1362], [3, 1374], [2, 1379], [4, 1385], [5, 1391], [3, 1396], [2, 1402], [4, 1407], [5, 1442], [4, 1454], [5, 1466], [4, 1486], [5, 1493], [5, 1498], [1, 1505], [2, 1509], [4, 1513], [2, 1519], [2, 1523], [3, 1529], [4, 1532], [2, 1537], [3, 1548], [4, 1552], [3, 1558], [2, 1562], [1, 1568], [5, 1572], [2, 1578], [2, 1583], [2, 1589], [5, 1594], [3, 1600], [4, 1606], [5, 1611]]
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
    modry = pygame.image.load("D:\\kraken\\projekt-1ep-absolvent\\source\\Martin_hudba_minihra\\bitmapa.png")
    cerveny = pygame.image.load("D:\\kraken\\projekt-1ep-absolvent\\source\\Martin_hudba_minihra\\bitmapa2.png")

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
                    for n in aktivni_noty:
                        nota_rect=n[0]  
                        if modry_rect.colliderect(nota_rect) or cerveny_rect.colliderect(nota_rect):
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
          

        for _ in range(aktivni):
                
                poloha_y = notove[ktera_nota][0]*100
                ktera_nota += 1
                nota=pygame.Rect(poloha_x,poloha_y,20,40)
                aktivni_noty.append([nota,aktivni])
                aktivni = 0

        screen.fill(barva_pozadi)

        for o in aktivni_noty:
            rect_nota = o[0]
            rect_nota.x -= 5 
            
            pygame.draw.rect(screen, (0, 200, 0), rect_nota)
            if rect_nota.x < 0:
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
