import pygame 
def main(global_data):
    pygame.init()
    poloha_x =800
    notove = [[3, 13], [4, 39], [5, 65], [3, 69], [5, 76], [5, 81], [5, 87], [2, 93], [1, 98], [5, 104], [5, 110], [5, 116]]
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

    # Rychlost pohybu
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
                    for n in notove:  
                        if modry_rect.colliderect(n) or cerveny_rect.colliderect(n):
                            notove.remove(n)
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

        if notove[ktera_nota][1]==kdy/100:
                aktivni = 1
                print(kdy)        

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
            print(rect_nota.x)
            print(rect_nota.y)
            print()
            pygame.draw.rect(screen, (0, 200, 0), rect_nota)
            if rect_nota.x < 0:
                aktivni_noty.remove(o)  # Volitelně odstraníš notu mimo obrazovku

        # Omez pohyb na okno
        modry_rect.y = max(0, min(modry_rect.y, screen.get_height() - modry_rect.height))
        cerveny_rect.y = max(0, min(cerveny_rect.y, screen.get_height() - cerveny_rect.height))

        # Vyplnění obrazovky
        

        # Vykreslení obrázků pomocí blit
        screen.blit(modry, modry_rect.topleft)
        screen.blit(cerveny, cerveny_rect.topleft)

       
        # Aktualizace obrazovky
        pygame.display.flip()
        clock.tick(60)
