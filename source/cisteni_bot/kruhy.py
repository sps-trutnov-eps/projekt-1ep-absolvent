import random
import pygame
class Kruh:
    def __init__(self, rozliseni_x, rozliseni_y):
        self.radius = random.randint(20, 50)

        # Zajištění, že kruh zůstane uvnitř okna i při malém rozlišení
        max_x = max(self.radius, rozliseni_x - self.radius)
        max_y = max(self.radius, rozliseni_y - self.radius)
        min_x = max(self.radius, 200)
        
        self.x = random.randint(min_x, max_x)
        self.y = random.randint(self.radius, max_y)
    
    def draw(self, screen,barva_kruhu):
        pygame.draw.circle(screen, barva_kruhu, (self.x, self.y), self.radius)
    
    def is_hovered(self, pos):
        dx = self.x - pos[0]
        dy = self.y - pos[1]
        return (dx**2 + dy**2) <= self.radius**2
