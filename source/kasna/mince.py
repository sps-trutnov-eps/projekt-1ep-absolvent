import pygame
import random
import math

class Mince:
    def __init__(self, x, y, typ=None):
        self.x = x
        self.y = y
        self.type = typ if typ else self._vyber_typ()

        if self.type == "1":
            self.radius = 8
            self.hodnota = 1
            self.textura=pygame.image.load("kasna\\1.png").convert_alpha()
        elif self.type == "2":
            self.radius = 10
            self.hodnota = 2
            self.textura=pygame.image.load("kasna\\2.png").convert_alpha()
        elif self.type == "5":
            self.radius = 12
            self.hodnota = 5
            self.textura=pygame.image.load("kasna\\5.png").convert_alpha()
        elif self.type == "10":
            self.radius = 17
            self.hodnota = 10
            self.textura=pygame.image.load("kasna\\10.png").convert_alpha()
        elif self.type == "20":
            self.radius = 20
            self.hodnota = 20
            self.textura=pygame.image.load("kasna\\20.png").convert_alpha()
        elif self.type == "50":
            self.radius = 25
            self.hodnota = 50
            self.textura=pygame.image.load("kasna\\50.png").convert_alpha()
        elif self.type == "sputnik":
            self.radius = 50
            self.hodnota = 10000
            self.textura=pygame.image.load("kasna\\sputnik.png").convert_alpha()
    
    def _vyber_typ(self):
        typy = ["1", "2", "5", "10", "20", "50","sputnik"]
        return random.choices(typy, weights=SANCE_MINCI.values(), k=1)[0]
            
    def vykresli_se(self, screen):
        screen.blit(self.textura,(self.x-self.radius/2,self.y-self.radius/2))

    def get_info(self):
        return f"Typ: {self.type}, Hodnota: {self.hodnota}"
        
    def je_kliknuto(self, mouse_x, mouse_y):
        distance = math.sqrt((mouse_x - self.x)**2 + (mouse_y - self.y)**2)
        return distance <= self.radius


SANCE_MINCI = {
    "1": 50,   
    "2": 30,  
    "5": 12,  
    "10": 5,  
    "20": 2.5,  
    "50": 0.5,
    "sputnik":0.001  
}

def nastav_sance(nove_sance):

    global SANCE_MINCI
    SANCE_MINCI.update(nove_sance)
    for typ in ["1", "2", "5", "10", "20", "50","sputnik"]:
        if typ not in SANCE_MINCI or SANCE_MINCI[typ] < 0:
            SANCE_MINCI[typ] = 0.5 
def ziskej_sance():
    return SANCE_MINCI

def spawn(pocet_minci):
    list_mince = []
    # Hodnoty kruhu s vodou
    ellipse_center_x = 800/2
    ellipse_center_y = 500/2
    ellipse_sirka = 650
    ellipse_vyska = 350
    a = ellipse_sirka / 2
    b = ellipse_vyska / 2
    # Spawnování mincí v kruhu s vodou
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