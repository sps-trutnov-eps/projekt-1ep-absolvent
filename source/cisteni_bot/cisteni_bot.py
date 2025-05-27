import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

# sem piste importy
import pygame
import random
from cisteni_bot.kruhy import Kruh

def main(global_data):
    # Rozlišení okna
    rozliseni_x = 800
    rozliseni_y = 600

    textura_pozadi = pygame.image.load("cisteni_bot/podlazi.png")
    bota = pygame.image.load("cisteni_bot/bota.png")
    scaled_bota = pygame.transform.scale(bota, (800, 600))
    kroksa = pygame.image.load("cisteni_bot/kroksa.png")
    scaled_kroksa = pygame.transform.scale(kroksa, (800, 600))
    sandal = pygame.image.load("cisteni_bot/sandal.png")
    scaled_sandal = pygame.transform.scale(sandal, (800, 600))
    vyber_boty = random.choice([scaled_bota,scaled_kroksa,scaled_sandal])
    vlajky = pygame.NOFRAME

    # Vytvoření okna
    obrazovka = pygame.display.set_mode((rozliseni_x, rozliseni_y), vlajky)


    # Barvy
    barva_pozadi = (255, 0, 0)  # červená
    barva_kurzoru = (0, 0, 0)   # černá
    barva_kruhu = (139, 69, 19) # hnědá (saddle brown)

    pygame.font.init()
    font = pygame.font.SysFont("Arial", 30)
    barva_textu = (255, 255, 255) 


    # Seznam kruhů
    kruhy = []

    pygame.mouse.set_visible(False)

    # Časovač pro generování nových kruhů
    spawn_timer = 0
    spawn_delay = 100  # v milisekundách

    zbirka = 0

    casovac = 1800

    # Hodiny
    hodiny = pygame.time.Clock()
    # Hlavní smyčka



    hlavni_smyska = True
    while hlavni_smyska:
        dt = hodiny.tick(60)  # limit na 60 FPS
        casovac -= 1
        spawn_timer += dt
        odpocet = int(casovac/60)

        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT or (udalost.type == pygame.KEYDOWN and udalost.key == pygame.K_ESCAPE):
                hlavni_smyska = False

        # Generování nového kruhu (max. 5 na obrazovce)
        if len(kruhy) < 5 and spawn_timer > spawn_delay:
            kruhy.append(Kruh(rozliseni_x, rozliseni_y))
            spawn_timer = 0

        # Pozice kurzoru
        pozice_mysi = pygame.mouse.get_pos()

        # Vyplnění pozadí
        obrazovka.blit(textura_pozadi, (0, 0))
        
        obrazovka.blit(vyber_boty,(0,0))

        # Kontrola kolize kurzoru s kruhy
        novy_seznam = []

        # Pro každý kruh v seznamu kruhů
        for k in kruhy:
            # Pokud není kurzor nad tímto kruhem, přidej ho do nového seznamu
            if not k.is_hovered(pozice_mysi):
                novy_seznam.append(k)

        zbirka += (len(kruhy) - len(novy_seznam)) / 10
        zbirka = round(zbirka, 1)
        
        # Přiřaď nový seznam zpět do původního seznamu
        kruhy = novy_seznam

        # Vykreslení kruhů
        for k in kruhy:
            k.draw(obrazovka, barva_kruhu)

        

        if casovac == 0:
            hlavni_smyska = False
            zbirka = round(zbirka)
            print(zbirka)
            global_data['penize'] += zbirka

        text = font.render(f"Konto: {zbirka}   Čas: {odpocet}s", True, barva_textu)
        obrazovka.blit(text, (10, 10))   # levý horní roh

        # Kruh sledující kurzor
        pygame.draw.circle(obrazovka, barva_kurzoru, pozice_mysi, 20)

        # Aktualizace obrazovky
        pygame.display.update()

    # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"
    # sem piste svuj program
    global_data["penize"] += zbirka
if __name__ == "__main__":
    masterFunc(novyProgram(main))
    pygame.quit()