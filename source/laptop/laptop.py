import pygame
import sys
import datetime
import time

pygame.init()


placeholder = True

# Získání nativního rozlišení obrazovky
screen_info = pygame.display.Info()
rozliseni_sirka, rozliseni_vyska = screen_info.current_w, screen_info.current_h

# Nastavení fullscreen okna
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
font = pygame.font.Font(None, rozliseni_sirka // 70)  # Zvýšení velikosti písma pro lepší viditelnost

font_text = pygame.font.Font(None, rozliseni_sirka // 10) 

font_placeholder = pygame.font.Font(None, rozliseni_sirka // 11)

font_varovani = pygame.font.Font(None, rozliseni_sirka // 80) 

pygame.display.set_caption("Textový vstup v Pygame")



print(rozliseni_vyska)


input_text = ""    #JMENO HRACE





jmeno_pole_visible = True

battery = rozliseni_vyska / 1.08
battery_minus = 5  # o kolik se má zmenšit každých 10 sekund
posledni_akce = pygame.time.get_ticks()

clock = pygame.time.Clock()

while True:
    screen.blit(background_image, (0, 0))  
    if jmeno_pole_visible == True:
        screen.blit(jmeno, (rozliseni_sirka / 5.25, rozliseni_vyska / 4))  
    
   
    
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    

        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_RETURN and len(input_text) > 2:
                print(f"Uložený text: {input_text}")
                input_text = ""  # Vymazání vstupu po potvrzení
                jmeno_pole_visible = False
                placeholder = False
            elif udalost.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
                placeholder = False 
            elif len(input_text) < 8:
                input_text += udalost.unicode  # Přidání znaku do vstupu
                placeholder = False
   
    if input_text == "" and jmeno_pole_visible == True:
        placeholder = True
   
    
    placeholder_text = 'Zadej své jméno'
    varovani_text = 'min 3 a max 8 znaku'
    
    if placeholder == True:
        text_surface_placeholder = font_placeholder.render(placeholder_text, True, (200, 200, 200)) 
        screen.blit(text_surface_placeholder, (rozliseni_sirka // 4.1 , rozliseni_vyska // 3.1))
    
    if jmeno_pole_visible == True:
        text_surface_varovani = font_varovani.render(varovani_text, True, (0, 0, 0)) 
        screen.blit(text_surface_varovani, (rozliseni_sirka // 2.13 , rozliseni_vyska // 3.7))
        

    
    # Vykreslení textu na obrazovku
    text_surface_name = font_text.render(input_text, True, (0, 0, 0))  
    screen.blit(text_surface_name, (rozliseni_sirka // 4.1 , rozliseni_vyska // 3.1))  
    
    battery_time = pygame.time.get_ticks()

    # Každých 10 sekund zmenši baterii
    if battery_time - posledni_akce >= 10000:
        battery -= battery_minus
        if battery < 0:
            battery = 0  # zabrání záporné výšce
        posledni_akce = battery_time
    
    
    
    
    pygame.draw.rect(screen, (0, 0, 255), (rozliseni_sirka / 1.12, rozliseni_vyska / 19, rozliseni_sirka / 12, rozliseni_vyska / 1.08), 2)

    # Výplň baterie
    pygame.draw.rect(screen, (0, 0, 255), (rozliseni_sirka / 1.12, rozliseni_vyska / 19 + (rozliseni_vyska / 1.08 - battery), rozliseni_sirka / 12, battery))

    # Zobrazení data
    dnes = datetime.datetime.today().strftime("%d.%m.%Y")
    text_surface = font.render(dnes, True, (0, 0, 0))  # Černá barva
    screen.blit(text_surface, (rozliseni_sirka / 1.3, rozliseni_vyska / 1.339))
    
    
    
    pygame.display.update()
    clock.tick(60)
