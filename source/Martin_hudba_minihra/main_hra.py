import pygame 
def main(global_data):
    pygame.init()
    poloha_x =800
    notove = [[4, 8], [2, 37], [4, 48], [5, 60], [2, 70], [5, 78], [4, 86], [2, 93], [5, 101], [2, 110], [1, 118], [3, 126], [5, 133], [5, 141], [3, 149], [1, 157], [3, 166], [2, 234], [2, 255], [5, 277], [1, 296], [1, 378], [5, 383], [5, 387], [3, 393], [1, 398], [1, 403], [1, 408], [2, 414], [4, 420], [3, 425], [3, 430], [2, 437], [1, 441], [3, 447], [2, 452], [3, 458], [1, 463], [4, 468], [1, 473], [1, 479], [5, 484], [2, 490], [5, 495], [2, 501], [1, 506], [3, 512], [4, 517], [3, 523], [2, 540], [4, 544], [1, 564], [4, 574], [4, 583], [4, 597], [5, 620], [2, 630], [2, 636], [4, 641], [3, 647], [4, 653], [2, 659], [4, 665], [3, 671], [3, 676], [5, 682], [4, 688], [3, 693], [3, 698], [3, 704], [4, 709], [1, 715], [4, 721], [5, 726], [4, 732], [3, 738], [5, 749], [2, 755], [1, 759], [2, 766], [5, 770], [1, 776], [5, 782], [1, 787], [1, 793], [2, 799], [3, 804], [1, 810], [1, 816], [2, 823], [3, 829], [2, 833], [4, 839], [4, 844], [5, 849], [2, 854], [4, 860], [5, 866], [5, 870], [4, 876], [4, 881], [1, 886], [2, 892], [5, 897], [1, 903], [2, 909], [5, 915], [4, 919], [1, 925], [2, 931], [1, 936], [4, 942], [4, 948], [4, 953], [2, 960], [4, 964], [1, 969], [5, 975], [1, 980], [3, 984], [4, 990], [1, 995], [1, 1006], [4, 1011], [2, 1017], [1, 1023], [4, 1028], [1, 1033], [1, 1045], [1, 1050], [1, 1056], [3, 1061], [4, 1066], [3, 1072], [2, 1084], [3, 1089], [1, 1100]]
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
    modry = pygame.image.load("Martin_hudba_minihra\\bitmapa.png")
    cerveny = pygame.image.load("Martin_hudba_minihra\\bitmapa2.png")

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
