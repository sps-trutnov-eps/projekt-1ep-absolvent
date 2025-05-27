import pygame
import math

class Strela:
    
    def __init__ (self, strela_x, strela_y, angle_kanon, zasazeni):
        self.strela_x = strela_x
        self.strela_y = strela_y
        self.angle_kanon = angle_kanon
        self.zasazeni = zasazeni
        self.spawn = 20  # Přidání atributu spawn jako atribut instance
        
        
        
    def move(self, pohyb_země):
        if self.strela_y > 1080 - 20:  # 20 ke velikost výbuchu
            self.strela_y = 1080
            self.spawn -= 1  # Použití atributu instance
            self.strela_x -= pohyb_země
            
        elif self.zasazeni == True:
            self.spawn -= 1  # Použití atributu instance
            self.strela_x -= pohyb_země
            
        else:
            self.strela_x -= 20 * math.sin(math.radians(self.angle_kanon - 90)) 
            self.strela_y -= 20 * math.cos(math.radians(self.angle_kanon - 90))
            self.spawn = 20  # Použití atributu instance
            
            
    
    def draw(self, surface, image_strela, image_vybuch, vybuch):
        if self.spawn > 0:  # Použití atributu instance
            if self.strela_y > 1080 - 20:
                surface.blit(image_vybuch, (self.strela_x, self.strela_y - 40))
                
            if self.zasazeni == True:
                surface.blit(vybuch, (self.strela_x, self.strela_y))
                
            else:
                surface.blit(image_strela, (self.strela_x, self.strela_y))
                
                
                
    def zasah(self, nepritel):
        if nepritel.poloha_x < self.strela_x < nepritel.poloha_x + 150 and \
           nepritel.poloha_y < self.strela_y < nepritel.poloha_y + 200:  # hitbox
            
            nepritel.zivoty_self -= 1
            self.zasazeni = True
            
            

class Raketa:
    def __init__ (self, raketa_x, raketa_y, zasazeni):
        self.raketa_x = raketa_x
        self.raketa_y = raketa_y
        self.zasazeni = zasazeni
        self.délka_navádění = 100
        self.angle = 0
        self.spawn = 20
    
    def move(self, pohyb_země,nepritel,výška,presnost):
        if self.raketa_y > 1080 - 20:  # 20 ke velikost výbuchu
            self.raketa_y = 1080
            self.spawn -= 1  # Použití atributu instance
            self.raketa_x -= pohyb_země
            
        elif self.zasazeni == True:
            self.spawn -= 1  # Použití atributu instance
            self.raketa_x -= pohyb_země
            
        else:
            if self.délka_navádění > 0:
                self.délka_navádění -= 1
            else:
                dy = výška + 100
            
            # Výpočet rozdílu v pozicích
            dx = nepritel.poloha_x - self.raketa_x
            dy = nepritel.poloha_y - self.raketa_y
            
            # Výpočet úhlu k cíli
            target_angle = math.atan2(dy, dx)
        
            self.angle = (1 - 0.05) * self.angle + 0.05 * target_angle
            
            # Výpočet nové pozice rakety pomocí sin a cos s konstantní rychlostí
            self.raketa_x += math.cos(self.angle) * 6
            self.raketa_y += math.sin(self.angle) * presnost
            self.raketa_x-= pohyb_země
            self.raketa_x+=7 # aby raketa necouvala a to + 7  je něco jako šance  kterou má raketa trefit cíl

    def navádění(self, nepritel, screen, raketa, výška, pohyb_země,presnost):
        self.move(pohyb_země,nepritel,výška,presnost)
        
                
    def draw(self, surface, image_strela, image_vybuch, vybuch,pohyb_země):
        if self.spawn > 0:  # Použití atributu instance
            if self.raketa_y > 1080 - 20:
                surface.blit(image_vybuch, (self.raketa_x, self.raketa_y - 40))
                
            if self.zasazeni == True:
                surface.blit(vybuch, (self.raketa_x, self.raketa_y))
                
            else:
                surface.blit(image_strela, (self.raketa_x , self.raketa_y))
            
                  
    def zasah(self, nepritel,rozmer_y,rozmer_x):
        if nepritel.poloha_x < self.raketa_x < nepritel.poloha_x + rozmer_x and \
           nepritel.poloha_y < self.raketa_y < nepritel.poloha_y + rozmer_y:  # hitbox
            nepritel.zivoty_self -= 10
            self.zasazeni = True
