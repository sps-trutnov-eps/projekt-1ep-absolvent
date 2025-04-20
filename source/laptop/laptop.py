import sys
from pathlib import Path
import pygame
import json
import os
import datetime

# Přidání rodičovského adresáře pro importy
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

# Import hlavních funkcí
from master import main as masterFunc
from master import convertFuncToStr as novyProgram

# Inicializace Pygame
pygame.init()

# Získání rozlišení obrazovky
screen_info = pygame.display.Info()
rozliseni_sirka, rozliseni_vyska = screen_info.current_w, screen_info.current_h



# Uložení, že hra běží
stav = {"running": True, "player_name": "", "battery": rozliseni_vyska / 1.08}
if os.path.exists("stav.json"):
    with open("stav.json", "r") as f:
        stav = json.load(f)
stav["running"] = True
with open("stav.json", "w") as f:
    json.dump(stav, f)

# Fullscreen okno
screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska), pygame.FULLSCREEN)

# Načtení obrázků
try:
    background_image = pygame.image.load('laptop.png').convert()
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

jmeno = pygame.image.load('pixil-frame-0.png').convert()
jmeno = pygame.transform.scale(jmeno, (rozliseni_sirka / 1.6, rozliseni_vyska / 3))

controler_icon = pygame.image.load('ChatGPT Image 13. 4. 2025 18_38_36.png').convert()
controler_icon = pygame.transform.scale(controler_icon, (80, 80))

krizek = pygame.image.load('pixilart-drawing.png').convert()
krizek = pygame.transform.scale(krizek, (rozliseni_sirka / 80, rozliseni_sirka / 80))

# Písmo
pygame.font.init()
font = pygame.font.Font(None, rozliseni_sirka // 70)
font_text = pygame.font.Font(None, rozliseni_sirka // 10)
font_placeholder = pygame.font.Font(None, rozliseni_sirka // 11)
font_varovani = pygame.font.Font(None, rozliseni_sirka // 80)
pygame.display.set_caption("Textový vstup v Pygame")

# Herní proměnné
input_text = stav.get("player_name", "")
placeholder = input_text == ""
jmeno_pole_visible = input_text == ""

battery = stav.get("battery", rozliseni_vyska / 1.08)
battery_minus = rozliseni_sirka / 170
posledni_akce = pygame.time.get_ticks()
clock = pygame.time.Clock()

okno_her_zapnuto = False

icon_x = rozliseni_sirka / 5
icon_y = rozliseni_vyska / 8
icon_x1 = rozliseni_sirka / 1.34
icon_y1 = rozliseni_vyska / 5.8

controler_rect = pygame.Rect(icon_x, icon_y, 80, 80)
krizek_rect = pygame.Rect(icon_x1, icon_y1, rozliseni_sirka / 80, rozliseni_sirka / 80)


def main(global_data):
    # Inicializace proměnných
    input_text = stav.get("player_name", "")  # nebo "" pokud není definováno
    jmeno_pole_visible = input_text == ""  # Skrytí/přítomnost jména
    placeholder = input_text == ""
    battery = stav.get("battery", rozliseni_vyska / 1.08)
    battery_minus = rozliseni_sirka / 170
    posledni_akce = pygame.time.get_ticks()
    
    # Zbytek kódu pokračuje...
    while True:
        screen.blit(background_image, (0, 0))
        screen.blit(controler_icon, (icon_x, icon_y))

        if jmeno_pole_visible:
            screen.blit(jmeno, (rozliseni_sirka / 5.25, rozliseni_vyska / 4))

        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                stav["running"] = False
                stav["player_name"] = input_text
                stav["battery"] = battery
                with open("stav.json", "w") as f:
                    json.dump(stav, f)
                pygame.quit()
                sys.exit()

            if udalost.type == pygame.KEYDOWN:
                if udalost.key == pygame.K_RETURN and len(input_text) > 2:
                    print(f"Uložený text: {input_text}")
                    jmeno_pole_visible = False
                    placeholder = False
                    stav["player_name"] = input_text
                    with open("stav.json", "w") as f:
                        json.dump(stav, f)

                elif udalost.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                    placeholder = False

                elif len(input_text) < 8:
                    input_text += udalost.unicode
                    placeholder = False

            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if controler_rect.collidepoint(udalost.pos):
                    okno_her_zapnuto = True

                if krizek_rect.collidepoint(udalost.pos):
                    okno_her_zapnuto = False

        if input_text == "" and jmeno_pole_visible:
            placeholder = True

        if placeholder:
            text_surface_placeholder = font_placeholder.render('Zadej své jméno', True, (200, 200, 200))
            screen.blit(text_surface_placeholder, (rozliseni_sirka // 4.1, rozliseni_vyska // 3.1))

        if jmeno_pole_visible:
            text_surface_varovani = font_varovani.render('min 3 a max 8 znaku', True, (0, 0, 0))
            screen.blit(text_surface_varovani, (rozliseni_sirka // 2.13, rozliseni_vyska // 3.7))

            text_surface_name = font_text.render(input_text, True, (0, 0, 0))
            screen.blit(text_surface_name, (rozliseni_sirka // 4.1, rozliseni_vyska // 3.1))

        # Snížení baterie každých 10 sekund
        battery_time = pygame.time.get_ticks()
        if battery_time - posledni_akce >= 10000:
            battery -= battery_minus
            battery = max(battery, 0)
            posledni_akce = battery_time

        # Naše hry
        if okno_her_zapnuto:
            pygame.draw.rect(screen, (127, 127, 127), (rozliseni_sirka / 4.2, rozliseni_vyska / 6, rozliseni_sirka / 1.9, rozliseni_vyska / 2))
            screen.blit(krizek, (icon_x1, icon_y1))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 2.65, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 2.65, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 2.65, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 2.1, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 2.1, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 2.1, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 1.75, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 1.75, rozliseni_sirka / 7, rozliseni_vyska / 15))

            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 1.75, rozliseni_sirka / 7, rozliseni_vyska / 15))

        # Baterie
        pygame.draw.rect(screen, (100, 100, 100), (rozliseni_sirka / 1.2, rozliseni_vyska / 15, rozliseni_sirka / 12, rozliseni_vyska / 15))
        pygame.draw.rect(screen, (255, 255, 0), (rozliseni_sirka / 1.2, rozliseni_vyska / 15, battery, rozliseni_vyska / 15))

        pygame.display.update()
        clock.tick(60)



if __name__ == "__main__":
    masterFunc(novyProgram(main))