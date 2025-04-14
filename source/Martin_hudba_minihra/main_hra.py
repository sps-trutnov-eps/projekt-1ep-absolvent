import pygame
from Martin_hudba_minihra.noty import nota 
def main(global_data):
    pygame.init()

    notove = []

    # Nastavení velikosti okna
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Pohyb obdélníků nad a pod středem")

    # Barvy
    WHITE = (255, 255, 255)

    # Načtení obrázků
    modry = pygame.image.load("Martin_hudba_minihra\\bitmapa.png")
    cerveny = pygame.image.load("Martin_hudba_minihra\\bitmapa2.png")

    # Získání rectů
    modry_rect = modry.get_rect()
    cerveny_rect = cerveny.get_rect()

    # Nastavení počátečních pozic
    modry_rect.topleft = (10, (screen.get_height() // 2) - modry_rect.height)
    cerveny_rect.topleft = (10, (screen.get_height() // 2))

    # Rychlost pohybu
    move_speed = 5

    # Hlavní smyčka hry
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

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

        # Kolize se seznamem not (pokud nějaké máš)
        if keys[pygame.K_SPACE]:
            for n in notove[:]:  # použij kopii seznamu při mazání
                if modry_rect.colliderect(n) or cerveny_rect.colliderect(n):
                    notove.remove(n)

        # Omez pohyb na okno
        modry_rect.y = max(0, min(modry_rect.y, screen.get_height() - modry_rect.height))
        cerveny_rect.y = max(0, min(cerveny_rect.y, screen.get_height() - cerveny_rect.height))

        # Vyplnění obrazovky
        screen.fill(WHITE)

        # Vykreslení obrázků pomocí blit
        screen.blit(modry, modry_rect.topleft)
        screen.blit(cerveny, cerveny_rect.topleft)

        # Vykresli noty, pokud nějaké máš
        for nota in notove:
            pygame.draw.rect(screen, (0, 255, 0), nota)  # jen příklad, zelená nota

        # Aktualizace obrazovky
        pygame.display.flip()
        clock.tick(60)
