import pygame 
def main(global_data):
    pygame.init()
    poloha_x =800
    notove = [[4, 88, 2], [5, 100, 1], [5, 110, 1], [5, 119, 3], [3, 129, 3], [2, 150, 2], [5, 165, 1], [4, 176, 2], [2, 186, 3], [2, 197, 2], [2, 208, 2], [4, 231, 1], [3, 240, 2], [4, 250, 1], [3, 258, 3], [4, 266, 2], [3, 275, 2], [3, 282, 1], [5, 305, 2], [2, 313, 2], [2, 327, 2], [2, 335, 1], [2, 343, 1], [5, 351, 3], [1, 359, 1], [1, 374, 2], [3, 382, 1], [5, 389, 1], [5, 397, 3], [3, 405, 1], [2, 415, 2], [5, 423, 2], [3, 433, 1], [4, 441, 1], [1, 450, 3], [1, 459, 3], [4, 507, 2], [2, 516, 3], [3, 526, 3], [2, 535, 2], [4, 544, 1], [3, 552, 2], [1, 559, 3], [1, 566, 3], [4, 571, 1], [5, 578, 3], [2, 621, 2], [2, 627, 1], [1, 638, 1], [2, 647, 3], [1, 655, 2], [2, 667, 2], [3, 670, 2], [5, 682, 2], [2, 686, 1], [5, 689, 1], [5, 694, 1], [5, 702, 1], [1, 723, 1], [5, 729, 1], [3, 735, 2], [2, 738, 1], [4, 744, 2], [2, 747, 1], [1, 752, 3], [2, 760, 2], [4, 765, 3], [4, 770, 2], [4, 775, 2], [4, 780, 2], [1, 786, 2], [5, 788, 2], [3, 792, 1], [1, 797, 2], [3, 806, 1], [3, 814, 2], [1, 890, 2], [1, 924, 1], [3, 997, 2], [3, 1006, 3], [3, 1021, 3], [4, 1097, 3], [4, 1102, 3], [3, 1109, 1], [5, 1112, 1], [2, 1114, 2], [3, 1121, 3], [5, 1125, 3], [5, 1131, 1], [1, 1137, 3], [5, 1141, 1], [4, 1147, 3], [5, 1158, 1], [4, 1167, 3], [1, 1178, 3], [4, 1182, 3], [5, 1188, 2], [1, 1194, 2], [5, 1200, 3], [2, 1205, 1], [2, 1211, 1], [3, 1216, 1], [5, 1221, 3], [4, 1227, 2], [5, 1232, 1], [2, 1237, 1], [1, 1244, 2], [1, 1249, 3], [3, 1255, 3], [2, 1289, 1], [1, 1304, 2], [5, 1310, 2], [2, 1315, 1], [4, 1321, 1], [1, 1323, 2], [4, 1330, 2], [4, 1339, 2], [4, 1350, 3], [4, 1360, 1], [1, 1365, 3], [4, 1371, 3], [5, 1377, 2], [2, 1383, 3], [4, 1391, 1], [1, 1407, 1], [1, 1414, 3], [1, 1418, 3], [2, 1425, 3], [5, 1430, 3], [4, 1436, 2], [3, 1441, 2], [3, 1447, 2], [4, 1455, 1], [1, 1460, 3], [5, 1474, 3], [4, 1488, 3], [5, 1503, 2], [2, 1553, 1], [3, 1561, 2], [2, 1571, 3], [3, 1607, 1], [1, 1614, 1], [1, 1624, 1], [1, 1632, 2], [4, 1640, 1], [2, 1648, 1], [1, 1659, 3], [3, 1667, 3], [2, 1676, 3], [1, 1682, 1], [2, 1712, 1], [4, 1736, 3], [5, 1753, 3], [3, 1763, 3], [1, 1775, 1], [1, 1792, 3], [4, 1807, 3], [4, 1817, 1], [5, 1824, 2], [3, 1839, 3], [5, 1846, 3], [5, 1855, 2], [2, 1862, 2], [5, 1872, 2], [2, 1881, 2], [1, 1890, 2], [3, 1898, 3], [2, 1907, 2], [2, 1917, 1], [5, 1924, 1], [3, 1932, 1], [4, 1940, 3], [2, 1950, 2], [1, 1958, 1], [4, 1968, 3], [3, 1977, 1], [3, 1986, 3], [3, 1997, 1], [3, 2008, 3], [1, 2014, 1], [2, 2035, 3], [4, 2046, 1], [5, 2058, 2], [3, 2068, 2], [5, 2077, 3], [2, 2085, 3], [2, 2098, 2], [5, 2111, 1], [2, 2121, 1], [5, 2130, 2], [2, 2141, 1], [2, 2155, 3], [1, 2167, 3], [5, 2182, 1], [1, 2192, 3], [3, 2201, 1], [1, 2207, 2], [4, 2219, 3], [5, 2228, 2], [2, 2244, 1], [4, 2253, 3], [4, 2271, 2], [1, 2284, 1], [2, 2295, 3], [1, 2302, 3], [5, 2313, 2], [5, 2321, 3], [3, 2328, 3], [1, 2351, 1], [5, 2361, 3], [1, 2372, 2], [5, 2379, 3], [4, 2395, 1], [1, 2405, 2], [5, 2412, 1], [4, 2418, 2], [5, 2429, 2], [2, 2444, 3], [5, 2466, 1], [5, 2486, 2], [2, 2505, 3], [1, 2520, 2], [2, 2533, 2], [5, 2546, 1], [5, 2562, 1], [5, 2578, 2], [1, 2597, 3], [4, 2612, 3], [4, 2626, 3], [4, 2640, 1], [3, 2654, 3], [4, 2681, 3], [1, 2697, 3], [3, 2712, 3], [1, 2724, 1], [1, 2733, 2], [5, 2747, 1], [3, 2757, 2], [4, 2769, 3], [4, 2778, 3], [4, 2803, 2], [2, 2812, 3], [5, 2821, 1], [3, 2832, 3], [5, 2841, 1], [5, 2850, 1], [2, 2862, 3], [1, 2872, 1], [3, 2892, 2], [4, 2904, 3], [4, 2912, 3], [1, 2923, 1], [5, 2933, 3], [4, 2943, 1], [1, 2954, 3], [2, 2965, 3], [3, 2975, 1], [5, 2988, 1], [5, 3000, 1], [4, 3010, 1], [5, 3028, 3], [3, 3039, 3], [1, 3057, 1]]
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
                            if n[2] <=2: 
                                aktivni_noty.remove(n)
                                skore+=1
                        if modry_rect.colliderect(nota_rect) and cerveny_rect.colliderect(nota_rect):
                            if n[2] ==3: 
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
                aktivni_noty.append([nota,aktivni,barvan])
                aktivni = 0

        screen.fill(barva_pozadi)

        for o in aktivni_noty.copy():
            rect_nota = o[0]
            rect_nota.x -= 5 
            
            if 3 == o[2]:
                barva =(255,0,255)
            if 2 == o[2]:
                barva =(0,0,255)
            if 1 == o[2]:
                barva =(255,0,0)
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
