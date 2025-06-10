import os

import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

from laptop.hry.Space_Battle_main.main import main as Space_Battle





# sem piste importy
import pygame
import sys
import datetime
import json
import os

import win32gui
import win32con

import time


def open_file(address):
    os.startfile(address)
    time.sleep(1)

    file_title = os.path.basename(address)  # <-- fix here: just the file name

    def find_notepad_window(title_part):
        def callback(hwnd, result):
            window_text = win32gui.GetWindowText(hwnd)
            if title_part.lower() in window_text.lower():
                result.append(hwnd)
            return True

        hwnds = []
        win32gui.EnumWindows(callback, hwnds)
        return hwnds[0] if hwnds else None

    hwnd = find_notepad_window(file_title)
    if hwnd:
        win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # Restore if minimized
        win32gui.MoveWindow(hwnd, 500, 300, 1300, 500, True)  # x, y, width, height, repaint
    else:
        print("Window not found.")

def main(global_data):
    new_dir = "laptop"
    os.chdir(new_dir)
    # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"
    # sem piste svuj program
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
    
    calculator_icon = pygame.image.load('calculator.png').convert()
    calculator_icon = pygame.transform.scale(calculator_icon, (40, 60))
    
    kalkulacka = pygame.image.load('kalkulacka.png').convert()
    kalkulacka = pygame.transform.scale(kalkulacka, (rozliseni_sirka / 6, rozliseni_vyska / 2.5))
    
    
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
    battery_minus = rozliseni_sirka / 100
    posledni_akce = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    
    
    

        
    
    
    okno_her_zapnuto = False

    icon_x = rozliseni_sirka / 5
    icon_y = rozliseni_vyska / 8
    icon_x1 = rozliseni_sirka / 1.34
    icon_y1 = rozliseni_vyska / 5.8
    icon_x2 = rozliseni_sirka / 4.75
    icon_y2 = rozliseni_vyska / 4.4
    icon_x3 = rozliseni_sirka / 4.75
    icon_y3 = rozliseni_vyska / 4.4
    icon_x4 = rozliseni_sirka / 2.4
    icon_y4 = rozliseni_vyska / 4.2
    icon_x5 = rozliseni_sirka / 1.7555
    icon_y5 = rozliseni_vyska / 4.2
    

    controler_rect = pygame.Rect(icon_x, icon_y, 80, 80)
    calculator_rect = pygame.Rect(icon_x2, icon_y2, 50, 80)
    
    
    
    font1 = pygame.font.SysFont("Arial", 48)
    font2 = pygame.font.SysFont("Arial", 40)
    
    
    text1 = font1.render("Space Battle", True, (255, 255, 255))
    text2 = font1.render("Tank Game", True, (255, 255, 255))
    text3 = font1.render("Plane Game", True, (255, 255, 255))
    text4 = font2.render("Platformer Game", True, (255, 255, 255))
    text5 = font1.render("Jump Game", True, (255, 255, 255))
    text6 = font2.render("Catze VS mouze", True, (255, 255, 255))
    text7 = font2.render("The jumping man", True, (255, 255, 255))
    
    
    
    

    rect1 = pygame.Rect(rozliseni_sirka / 4, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15)
    rect2 = pygame.Rect(rozliseni_sirka / 2.35, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15)
    rect3 = pygame.Rect(rozliseni_sirka / 1.67, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15)
    rect4 = pygame.Rect(rozliseni_sirka / 4, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15)
    rect5 = pygame.Rect(rozliseni_sirka / 2.35, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15)
    rect6 = pygame.Rect(rozliseni_sirka / 1.67, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15)
    rect7 = pygame.Rect(rozliseni_sirka / 4, rozliseni_vyska / 2.65, rozliseni_sirka / 7, rozliseni_vyska / 15)
    
    
    kalkulacka_zapnuta = False
    
    krizek_rect = pygame.Rect(icon_x1, icon_y1, rozliseni_sirka / 80, rozliseni_sirka / 80)
    krizek_rect2 = pygame.Rect(icon_x5, icon_y5, rozliseni_sirka / 80, rozliseni_sirka / 80)

    for i, lore in enumerate(global_data["lory"]):
        if lore:
            cesta = f"lore\\lore{i+1}.txt"
            open_file(cesta)

    # Hlavní smyčka
    while True:
        screen.blit(background_image, (0, 0))
        screen.blit(controler_icon, (icon_x, icon_y))
        screen.blit(calculator_icon, (icon_x2, icon_y2))
        
        

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
        
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if calculator_rect.collidepoint(udalost.pos):
                    kalkulacka_zapnuta = True
                    
        
        
        if kalkulacka_zapnuta == True:
            screen.blit(kalkulacka, (icon_x4, icon_y4))
            screen.blit(krizek, (icon_x5, icon_y5))
        
        if udalost.type == pygame.MOUSEBUTTONDOWN:
            if krizek_rect2.collidepoint(udalost.pos):
                kalkulacka_zapnuta = False
        
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

       
       
       
       
       # Nase hry
        if okno_her_zapnuto:
            pygame.draw.rect(screen, (127, 127, 127), (rozliseni_sirka / 4.2, rozliseni_vyska / 6, rozliseni_sirka / 1.9, rozliseni_vyska / 2))
            screen.blit(krizek, (icon_x1, icon_y1))
            
            
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15))
            screen.blit(text1, (rozliseni_sirka / 3.8, rozliseni_vyska / 4.9))
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if rect1.collidepoint(udalost.pos):
                    print("space battle")
                    
                    
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15))
            screen.blit(text2, (rozliseni_sirka / 2.25, rozliseni_vyska / 4.9))
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if rect2.collidepoint(udalost.pos):
                    print("tank game")
            
            
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 5.1, rozliseni_sirka / 7, rozliseni_vyska / 15))
            screen.blit(text3, (rozliseni_sirka / 1.63, rozliseni_vyska / 4.9))
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if rect3.collidepoint(udalost.pos):
                    print("plane game")
           
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15))
            screen.blit(text4, (rozliseni_sirka / 3.9, rozliseni_vyska / 3.4))
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if rect4.collidepoint(udalost.pos):
                    print("platformer game")
                    
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15))
            screen.blit(text5, (rozliseni_sirka / 2.28, rozliseni_vyska / 3.4))
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if rect5.collidepoint(udalost.pos):
                    print("jump game")
                    
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 3.5, rozliseni_sirka / 7, rozliseni_vyska / 15))
            screen.blit(text6, (rozliseni_sirka / 1.66, rozliseni_vyska / 3.37))
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if rect6.collidepoint(udalost.pos):
                    print("Catze_VS_mouze")
        
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 2.65, rozliseni_sirka / 7, rozliseni_vyska / 15))
            screen.blit(text7, (rozliseni_sirka / 3.9, rozliseni_vyska / 2.57))
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                if rect7.collidepoint(udalost.pos):
                    print("the_jumping_man")
                    
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 2.65, rozliseni_sirka / 7, rozliseni_vyska / 15))
            
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 2.65, rozliseni_sirka / 7, rozliseni_vyska / 15))


            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 2.1, rozliseni_sirka / 7, rozliseni_vyska / 15))
            
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 2.1, rozliseni_sirka / 7, rozliseni_vyska / 15))
            
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 2.1, rozliseni_sirka / 7, rozliseni_vyska / 15))


            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 4, rozliseni_vyska / 1.75, rozliseni_sirka / 7, rozliseni_vyska / 15))
            
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 2.35, rozliseni_vyska / 1.75, rozliseni_sirka / 7, rozliseni_vyska / 15))
            
            pygame.draw.rect(screen, (170, 170, 170), (rozliseni_sirka / 1.67, rozliseni_vyska / 1.75, rozliseni_sirka / 7, rozliseni_vyska / 15))

        # Baterie
        pygame.draw.rect(screen, (0, 0, 255), (rozliseni_sirka / 1.12, rozliseni_vyska / 19, rozliseni_sirka / 12, rozliseni_vyska / 1.08), 2)
        pygame.draw.rect(screen, (0, 0, 255), (rozliseni_sirka / 1.12, rozliseni_vyska / 19 + (rozliseni_vyska / 1.08 - battery), rozliseni_sirka / 12, battery))

        # Aktuální datum
        dnes = datetime.datetime.today().strftime("%d.%m.%Y")
        text_surface = font.render(dnes, True, (0, 0, 0))
        screen.blit(text_surface, (rozliseni_sirka / 1.3, rozliseni_vyska / 1.339))

        pygame.display.update()
        clock.tick(60)
    
if __name__ == "__main__":
    masterFunc(novyProgram(main))