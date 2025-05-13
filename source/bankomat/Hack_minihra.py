import pygame
import random
import sys
import time

# Inicializace Pygame
pygame.init()

# Konstanty
WIDTH, HEIGHT = 800, 500
COLUMN_WIDTH = 70
COLUMN_COUNT = 4
SYMBOL_HEIGHT = 50
MARGIN = 50 #prostor mezi sloupci a okraji obrazovky
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0) 
BLACK = (0, 0, 0)
FPS = 60
SYMBOL_CHANGE_RATE = 2  # Počet změn za sekundu
LETTER_PROBABILITY = 0.2 

# Písmena pro jednotlivé sloupce
LETTERS = ['P', 'A', 'S', 'S']

# Vytvoření obrazovky
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ATM Hacking Minigame")
clock = pygame.time.Clock()

# Načtení obrázku pozadí
try:
    background_image = pygame.image.load("bankomat/okraj_obrazovky.png").convert_alpha()
    # Změna velikosti obrázku na rozměry okna
    background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
except pygame.error as e:
    print(f"Nepodařilo se načíst obrázek pozadí: {e}")
    background_image = None

font = pygame.font.SysFont('consolas', 28)
big_font = pygame.font.SysFont('consolas', 40)  # Větší font pro zvýraznění aktivního sloupce

class Symbol:
    def __init__(self, letter, is_special=False):
        self.current_symbol = "0" if random.random() < 0.5 else "1"
        self.is_special = is_special
        self.letter = letter
        self.change_timer = 0
        self.change_interval = 1.0 / SYMBOL_CHANGE_RATE
        
    def update(self, dt):
        self.change_timer += dt
        if self.change_timer >= self.change_interval:
            self.change_timer = 0
            
            # Když je speciální a není aktuálně písmenem, větší šance na objevení písmene
            if self.is_special and self.current_symbol != self.letter and random.random() < LETTER_PROBABILITY:
                self.current_symbol = self.letter
            else:
                self.current_symbol = "0" if random.random() < 0.5 else "1"
                
    def get_symbol(self):
        return self.current_symbol

class Column:
    def __init__(self, x, letter, visible_positions):
        self.x = x
        self.letter = letter
        self.stopped = False
        self.target_zone_index = len(visible_positions) // 2  
        self.zone_size = 1  
        self.win = False
        self.visible_positions = visible_positions
        self.active = False  
        
        # Vytvoření symbolů na pevných pozicích
        self.symbols = []
        for i in range(len(visible_positions)):
            
            is_special = (i == self.target_zone_index)
            self.symbols.append(Symbol(letter, is_special))
                
    def update(self, dt):
        if not self.stopped:
            for symbol in self.symbols:
                symbol.update(dt)
                
    def draw(self):
        # Vykreslení cílové zóny 
        target_y = self.visible_positions[self.target_zone_index]
        zone_color = (80, 80, 80) if self.active else (50, 50, 50)  
        
        pygame.draw.rect(screen, zone_color, 
                        (self.x - COLUMN_WIDTH//2, target_y - SYMBOL_HEIGHT//2, 
                         COLUMN_WIDTH, SYMBOL_HEIGHT))
        
        # Vykreslení trojúhelníku nad aktivním sloupcem
        if self.active:
            triangle_points = [
                (self.x, MARGIN - 20),
                (self.x - 15, MARGIN - 35),
                (self.x + 15, MARGIN - 35)
            ]
            pygame.draw.polygon(screen, WHITE, triangle_points)
        
        # Vykreslení symbolů na pevných pozicích
        for i, symbol in enumerate(self.symbols):
            y = self.visible_positions[i]
            
            
            current_symbol = symbol.get_symbol()
            if current_symbol == self.letter:
                color = RED  
                
                if i == self.target_zone_index and self.stopped:
                    self.win = True
            else:
                color = GREEN if not self.stopped else WHITE
                
            text = font.render(current_symbol, True, color)
            screen.blit(text, (self.x - text.get_width()//2, y - text.get_height()//2))
                
    def stop(self):
        if not self.stopped:
            self.stopped = True
            
          
            target_symbol = self.symbols[self.target_zone_index].get_symbol()
            if target_symbol == self.letter:
                self.win = True
                return True
            return False

def main():
    # Vytvoření sloupců
    columns = []
    column_spacing = WIDTH // (COLUMN_COUNT + 1)
    
    
    visible_area_height = HEIGHT - (2 * MARGIN)
    symbol_positions_count = visible_area_height // SYMBOL_HEIGHT
    visible_positions = []
    
    for i in range(symbol_positions_count):
        y = MARGIN + (i * SYMBOL_HEIGHT) + (SYMBOL_HEIGHT // 2)
        visible_positions.append(y)
    
    for i in range(COLUMN_COUNT):
        x = (i + 1) * column_spacing
        columns.append(Column(x, LETTERS[i], visible_positions))
    
    
    active_column_index = 0
    columns[active_column_index].active = True
    
    # Hlavní herní smyčka
    running = True
    all_stopped = False
    win_count = 0
    
    last_time = time.time()
    
    while running:
        current_time = time.time()
        dt = current_time - last_time
        last_time = current_time
        
        screen.fill(BLACK)
        
        # Vykreslení pozadí
        if background_image:
            screen.blit(background_image, (0, 0))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                # Ovládání šipkami (vlevo, vpravo)
                if event.key == pygame.K_LEFT:
                    columns[active_column_index].active = False
                    active_column_index = (active_column_index - 1) % COLUMN_COUNT
                    columns[active_column_index].active = True
                elif event.key == pygame.K_RIGHT:
                    columns[active_column_index].active = False
                    active_column_index = (active_column_index + 1) % COLUMN_COUNT
                    columns[active_column_index].active = True
                # Zastavení sloupce mezerníkem
                elif event.key == pygame.K_SPACE:
                    if not columns[active_column_index].stopped:
                        if columns[active_column_index].stop():
                            win_count += 1
                        
                        found_next = False
                        if not all(col.stopped for col in columns):
                            original_index = active_column_index
                            while True:
                                active_column_index = (active_column_index + 1) % COLUMN_COUNT
                                if not columns[active_column_index].stopped:
                                    found_next = True
                                    break
                                if active_column_index == original_index:
                                    break
                            
                            if found_next:
                                for i, col in enumerate(columns):
                                    col.active = (i == active_column_index)
        
        
        for column in columns:
            column.update(dt)
            column.draw()
        
        # Kontrola, zda jsou všechny sloupce zastaveny
        all_stopped = all(column.stopped for column in columns)
        
        
        if all_stopped:
            if win_count == COLUMN_COUNT:
                result_text = font.render("HACK ÚSPĚŠNÝ!", True, GREEN)
            else:
                result_text = font.render(f"HACK SELHAL! Správně: {win_count}/{COLUMN_COUNT}", True, (255, 0, 0))
            screen.blit(result_text, (WIDTH//2 - result_text.get_width()//2, HEIGHT - 100))
            
            # Zobrazení možnosti restartovat hru
            restart_text = font.render("Stiskněte R pro restart", True, WHITE)
            screen.blit(restart_text, (WIDTH//2 - restart_text.get_width()//2, HEIGHT - 50))
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                # Restart hry
                columns = []
                for i in range(COLUMN_COUNT):
                    x = (i + 1) * column_spacing
                    columns.append(Column(x, LETTERS[i], visible_positions))
                active_column_index = 0
                columns[active_column_index].active = True
                all_stopped = False
                win_count = 0
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()