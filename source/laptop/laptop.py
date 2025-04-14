import pygame
import sys
import datetime
import json
import os

pygame.init()


# Získání rozlišení obrazovky
screen_info = pygame.display.Info()
rozliseni_sirka, rozliseni_vyska = screen_info.current_w, screen_info.current_h

# Uložení, že hra běží
stav = {"running": True, "player_name": "", "battery": rozliseni_vyska / 1.08}  # Přidáme baterii do stavového slovníku
if os.path.exists("stav.json"):
    with open("stav.json", "r") as f:
        stav = json.load(f)
stav["running"] = True
with open("stav.json", "w") as f:
    json.dump(stav, f)

# Získání rozlišení obrazovky
screen_info = pygame.display.Info()
rozliseni_sirka, rozliseni_vyska = screen_info.current_w, screen_info.current_h

# Fullscreen okno
screen = pygame.display.set_mode((rozliseni_sirka, rozliseni_vyska), pygame.FULLSCREEN)

try:
    background_image = pygame.image.load('laptop.png').convert()
    background_image = pygame.transform.scale(background_image, (rozliseni_sirka, rozliseni_vyska))
except pygame.error as e:
    print(f"Chyba při načítání obrázku: {e}")
    pygame.quit()
    sys.exit()

jmeno = pygame.image.load('pixil-frame-0.png').convert()
jmeno = pygame.transform.scale(jmeno, (rozliseni_sirka / 1.6, rozliseni_vyska / 3))

pygame.font.init()
font = pygame.font.Font(None, rozliseni_sirka // 70)
font_text = pygame.font.Font(None, rozliseni_sirka // 10)
font_placeholder = pygame.font.Font(None, rozliseni_sirka // 11)
font_varovani = pygame.font.Font(None, rozliseni_sirka // 80)
pygame.display.set_caption("Textový vstup v Pygame")

# --- HERNÍ PROMĚNNÉ ---
input_text = stav.get("player_name", "")
placeholder = input_text == ""
jmeno_pole_visible = input_text == ""

battery = stav.get("battery", rozliseni_vyska / 1.08)  # Načteme hodnotu baterie z uloženého stavu
battery_minus = rozliseni_sirka / 170
posledni_akce = pygame.time.get_ticks()
clock = pygame.time.Clock()


controler_icon = pygame.image.load('ChatGPT Image 13. 4. 2025 18_38_36.png').convert()
controler_icon = pygame.transform.scale(controler_icon, (80, 80))




icon_x = 350
icon_y = 130

controler_rect = controler_icon.get_rect(topleft=(icon_x, icon_y))

# --- HLAVNÍ SMYČKA ---
while True:
    screen.blit(background_image, (0, 0))
    screen.blit(controler_icon, (icon_x, icon_y))

    if jmeno_pole_visible:
        screen.blit(jmeno, (rozliseni_sirka / 5.25, rozliseni_vyska / 4))

    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            stav["running"] = False
            stav["player_name"] = input_text
            stav["battery"] = battery  # Uložíme aktuální stav baterie
            with open("stav.json", "w") as f:
                json.dump(stav, f)
            pygame.quit()
            sys.exit()

        if udalost.type == pygame.KEYDOWN:
            # Reset uloženého stavu pomocí R
            if udalost.key == pygame.K_r:
                if os.path.exists("stav.json"):
                    os.remove("stav.json")
                    input_text = ""
                    placeholder = True
                    jmeno_pole_visible = True
                    stav["player_name"] = ""
                    stav["battery"] = rozliseni_vyska / 1.08  # Reset baterie na původní hodnotu
                    print("Postup resetován.")

            # Vstup jména
            elif udalost.key == pygame.K_RETURN and len(input_text) > 2:
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

    if input_text == "" and jmeno_pole_visible:
        placeholder = True

    if placeholder:
        text_surface_placeholder = font_placeholder.render('Zadej své jméno', True, (200, 200, 200))
        screen.blit(text_surface_placeholder, (rozliseni_sirka // 4.1, rozliseni_vyska // 3.1))

    if jmeno_pole_visible:
        text_surface_varovani = font_varovani.render('min 3 a max 8 znaku', True, (0, 0, 0))
        screen.blit(text_surface_varovani, (rozliseni_sirka // 2.13, rozliseni_vyska // 3.7))
    
    if jmeno_pole_visible:
        text_surface_name = font_text.render(input_text, True, (0, 0, 0))
        screen.blit(text_surface_name, (rozliseni_sirka // 4.1, rozliseni_vyska // 3.1))

    # Snížení baterie
    battery_time = pygame.time.get_ticks()
    if battery_time - posledni_akce >= 10000:
        battery -= battery_minus
        battery = max(battery, 0)
        posledni_akce = battery_time
    
    
    

    if udalost.type == pygame.MOUSEBUTTONDOWN:
        if controler_rect.collidepoint(udalost.pos):
            print("Klikl jsi na herní ovladač!")

    
    
    # Zobrazení baterie
    pygame.draw.rect(screen, (0, 0, 255), (rozliseni_sirka / 1.12, rozliseni_vyska / 19, rozliseni_sirka / 12, rozliseni_vyska / 1.08), 2)
    pygame.draw.rect(screen, (0, 0, 255), (rozliseni_sirka / 1.12, rozliseni_vyska / 19 + (rozliseni_vyska / 1.08 - battery), rozliseni_sirka / 12, battery))

    # Zobrazení aktuálního data
    dnes = datetime.datetime.today().strftime("%d.%m.%Y")
    text_surface = font.render(dnes, True, (0, 0, 0))
    screen.blit(text_surface, (rozliseni_sirka / 1.3, rozliseni_vyska / 1.339))

    pygame.display.update()
    clock.tick(60)
