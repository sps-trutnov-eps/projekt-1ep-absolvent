import pygame
import random
import math

class Mince:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.type = random.choice(["1","2","5","10","20","50"])  
        self.color = "yellow" 

        # Nastavení velikosti na základě typu
        if self.type == "1":
            self.radius = 8
            self.hodnota=1
        elif self.type == "2":
            self.radius = 10
            self.hodnota=2
        elif self.type == "5":
            self.radius = 12
            self.hodnota=5
        elif self.type == "10":
            self.radius = 17
            self.hodnota=10
        elif self.type == "20":
            self.radius = 20
            self.hodnota=20
        elif self.type == "50":
            self.radius = 25
            self.hodnota=50
    def vykresli_se(self, screen):

            pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def get_info(self):
        return f"Typ: {self.type}, Hodnota: {self.hodnota}"
    def je_kliknuto(self,mouse_x,mouse_y):
        distance = math.sqrt((mouse_x - self.x)**2 + (mouse_y - self.y)**2)
        return distance <= self.radius
def spawn(pocet_minci):
    list_mince = []
    #hodnoty kruhu s vodou
    ellipse_center_x = 800/2
    ellipse_center_y = 500/2
    ellipse_sirka = 600
    ellipse_vyska = 400
    a = ellipse_sirka / 2
    b = ellipse_vyska / 2
    #spawnování mincí v kruhu s vodou
    for _ in range(pocet_minci):
        while True:
            angle = random.uniform(0, 2 * math.pi)
            distance = math.sqrt(random.random())
            x = ellipse_center_x + a * distance * math.cos(angle)
            y = ellipse_center_y + b * distance * math.sin(angle)
            mince = Mince(x, y)
            if ((x - ellipse_center_x) / a) ** 2 + ((y - ellipse_center_y) / b) ** 2 <= (1 - mince.radius / min(a, b)) ** 2:
                list_mince.append(mince)
                break

    return list_mince


