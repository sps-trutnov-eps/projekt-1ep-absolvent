import sys
from pathlib import Path

parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))

from master import main as masterFunc
from master import convertFuncToStr as novyProgram

import pygame
import subprocess
import sys

def spustit_minihru():
    subprocess.Popen(["python", "Hack_minihra.py"])
    pygame.quit()
    sys.exit()

def main(global_data):
    # Inicializace Pygame
    pygame.font.init()
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Bankomat")

    # Načtení pozadí a obrázku šroubu
    background = pygame.image.load("okraj_obrazovky.png")
    background = pygame.transform.scale(background, (screen_width, screen_height))

    sroub_img = pygame.image.load("sroub.png")
    sroub_img = pygame.transform.scale(sroub_img, (50, 50))

    # Barvy a fonty
    WHITE = (255, 255, 255)
    GRAY = (100, 100, 100)
    BLACK = (0, 0, 0)
    font = pygame.font.SysFont(None, 60)
    message_font = pygame.font.SysFont(None, 48)

    # Hlavní tlačítko
    main_button_width, main_button_height = 300, 80
    main_button_rect = pygame.Rect(
        (screen_width // 2 - main_button_width // 2, screen_height // 2 - main_button_height // 2),
        (main_button_width, main_button_height)
    )

    # Tlačítka (šrouby) v rozích
    sroub_buttons = {
        "top_left": pygame.Rect(10, 10, 50, 50),
        "top_right": pygame.Rect(screen_width - 60, 10, 50, 50),
        "bottom_left": pygame.Rect(10, screen_height - 60, 50, 50),
        "bottom_right": pygame.Rect(screen_width - 60, screen_height - 60, 50, 50)
    }

    # Sleduj kliknutí na každý šroub
    clicked_srouby = {key: False for key in sroub_buttons.keys()}

    # Proměnné pro hlášku
    show_message = False
    message_start_time = 0
    message_duration = 5000  # 5 sekund

    # Funkce pro spuštění minihry

    # Hlavní smyčka7
    running = True
    while running:
        screen.blit(background, (0, 0))

        # Vykresli hlavní tlačítko
        pygame.draw.rect(screen, GRAY, main_button_rect)
        text = font.render("    Vybrat", True, WHITE)
        screen.blit(text, (main_button_rect.x + 30, main_button_rect.y + 15))

        # Vykresli šrouby (před kliknutím) nebo kolečka (po kliknutí)
        for key, rect in sroub_buttons.items():
            if clicked_srouby[key]:
                # Po kliknutí vykreslíme černé kolečko
                pygame.draw.circle(screen, BLACK, rect.center, 25)
            else:
                # Před kliknutím vykreslíme šroub
                screen.blit(sroub_img, rect.topleft)

        # Zobrazení hlášky
        current_time = pygame.time.get_ticks()
        if show_message and current_time - message_start_time <= message_duration:
            msg = message_font.render("Není platební karta", True, WHITE)
            screen.blit(msg, (screen_width // 2 - msg.get_width() // 2, 100))
        elif show_message and current_time - message_start_time > message_duration:
            show_message = False

        # Události
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                # Kliknutí na hlavní tlačítko
                if main_button_rect.collidepoint(mouse_pos):
                    show_message = True
                    message_start_time = pygame.time.get_ticks()

                # Kliknutí na šrouby (změna na kolečko po kliknutí)
                for key, rect in sroub_buttons.items():
                    if rect.collidepoint(mouse_pos) and not clicked_srouby[key]:
                        clicked_srouby[key] = True

                # Zkontroluj, jestli už jsou všechny šrouby kliknuté
                if all(clicked_srouby.values()):
                    spustit_minihru()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

    # pro otevreni okna "global_data['otevrena_okna'].append(novyProgram(funkce))"

if __name__ == "__main__":
    masterFunc(novyProgram(main))
