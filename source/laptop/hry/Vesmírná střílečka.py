import sys
import pygame
import math
import random
pygame.init()

#Vlastnosti okna
pygame.display.set_caption("Vesmírná střílečka")
okno_aplikace = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
sirka_okna, vyska_okna = okno_aplikace.get_size()
fps_casovac = pygame.time.Clock()

#Peníze
penize = 0
odmena_za_enship = 15
odmena_za_bosse = 600

#Vlastnosti ovladatelné lodě
rychlost = 12
max_hp = 10
hp = max_hp
max_naboje = 2
naboje = max_naboje
reload_cas = 60
reload_tick = 0
ship = pygame.image.load("vesmirna_lod.png")
ship_rect = ship.get_rect()
centrum_sirky_okna = (sirka_okna - ship_rect.width) // 2
poloha_x = centrum_sirky_okna
poloha_y = vyska_okna - ship_rect.height - 10
min_rychlost_strel = -15
vychozi_rychlost_strel = -7

#Ceny vylepšení
cena_hp = 70
cena_naboje = 50

#Obchod
v_obchode = False
obchod_font = pygame.font.SysFont(None, 48)
volba_font = pygame.font.SysFont(None, 36)

#Text
def vykresli_text(plocha, text, font, barva, pozice):
    text_obj = font.render(text, True, barva)
    plocha.blit(text_obj, pozice)

#Text statů    
def vykresli_staty():
    stats_font = pygame.font.SysFont(None, 36)
    vykresli_text(okno_aplikace, f"HP: {hp}/{max_hp}", stats_font, (255, 0, 0), (15, 20))
    vykresli_text(okno_aplikace, f"Náboje: {naboje}/{max_naboje}", stats_font, (255, 255, 0), (15, 60))
    if reload_tick > 0:
        vykresli_text(okno_aplikace, f"Nabíjení... {(reload_cas - reload_tick) // 60 + 1}s", stats_font, (255, 165, 0), (15, 100))
    vykresli_text(okno_aplikace, f"Úroveň: {aktualni_uroven}/{max_uroven}", stats_font, (0, 255, 255), (15, 140))
    vykresli_text(okno_aplikace, f"Peníze: ${penize}", stats_font, (50, 205, 50), (15, 180))
    
    if aktualni_uroven % 5 == 0 and boss_active and not hra_skoncila:
        vykresli_text(okno_aplikace, f"Boss HP: {bhp}/{Max_bhp}", stats_font, (210, 255, 150), (sirka_okna - 200, 20))
                   
#Zobrazení obchodu
def zobraz_obchod():
    global v_obchode, penize, max_hp, max_naboje, hp, naboje
    
    okno_aplikace.blit(pozadi1, (0, 0))
    
    vykresli_text(okno_aplikace, "OBCHOD", obchod_font, (255, 255, 255), (sirka_okna // 2 - 100, 100))
    vykresli_text(okno_aplikace, f"Peníze: ${penize}", obchod_font, (50, 205, 50), (sirka_okna // 2 - 100, 160))
    
#Tlačítka
    hp_btn = pygame.Rect(sirka_okna // 2 - 200, 250, 400, 80)
    naboje_btn = pygame.Rect(sirka_okna // 2 - 200, 350, 400, 80)
    pokracovat_btn = pygame.Rect(sirka_okna // 2 - 150, 500, 300, 80)
    
    pygame.draw.rect(okno_aplikace, (100, 100, 100), hp_btn)
    pygame.draw.rect(okno_aplikace, (100, 100, 100), naboje_btn)
    pygame.draw.rect(okno_aplikace, (50, 150, 50), pokracovat_btn)
    
    # Text tlačítek
    vykresli_text(okno_aplikace, f"Vylepšit HP (+1): ${cena_hp}", volba_font, (255, 255, 255), (hp_btn.x + 20, hp_btn.y + 25))
    vykresli_text(okno_aplikace, f"Vylepšit náboje (+1): ${cena_naboje}", volba_font, (255, 255, 255), (naboje_btn.x + 20, naboje_btn.y + 25))
    vykresli_text(okno_aplikace, "Pokračovat ve hře", volba_font, (255, 255, 255), (pokracovat_btn.x + 40, pokracovat_btn.y + 25))
    
    # Aktuální staty
    vykresli_text(okno_aplikace, f"Aktuální HP: {max_hp}", volba_font, (255, 0, 0), (sirka_okna // 2 + 220, 250 + 25))
    vykresli_text(okno_aplikace, f"Aktuální náboje: {max_naboje}", volba_font, (255, 255, 0), (sirka_okna // 2 + 220, 350 + 25))
    
    pygame.display.update()
    
    while v_obchode:
        for udalost in pygame.event.get():
            if udalost.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if udalost.type == pygame.KEYDOWN:
                if udalost.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if udalost.type == pygame.MOUSEBUTTONDOWN:
                mys_x, mys_y = pygame.mouse.get_pos()
                # Koupení HP
                if hp_btn.collidepoint(mys_x, mys_y) and penize >= cena_hp:
                    penize -= cena_hp
                    max_hp += 1
                    hp = max_hp  # Obnovit HP na maximum
                    
                    okno_aplikace.blit(pozadi1, (0, 0))
                    zobraz_obchod()
                # Koupení nábojů
                elif naboje_btn.collidepoint(mys_x, mys_y) and penize >= cena_naboje:
                    penize -= cena_naboje
                    max_naboje += 1
                    naboje = max_naboje  # Obnovit náboje na maximum
                    
                    okno_aplikace.blit(pozadi1, (0, 0))
                    zobraz_obchod()
                # Pokračovat ve hře
                elif pokracovat_btn.collidepoint(mys_x, mys_y):
                    v_obchode = False
        
        fps_casovac.tick(60)
    
def znic_lod():
    global hra_skoncila, vyhra, hp
    hp -= 1
    if hp <= 0:
        hra_skoncila = True
        vyhra = False
        
#Vlastnosti bosse
Max_bhp = 25
bhp = Max_bhp
bship = pygame.image.load("Boss.png")
bship_rect = bship.get_rect()
bship_rect.inflate_ip(0, -200)
boss_active = False
boss_laser_timer = 0
boss_laser_interval = 100  # 3 sekundy mezi lasery
boss_strela_timer = 0
boss_strela_interval = 60

class BossLaser:
    def __init__(self, x, y):
        self.image = pygame.image.load("Boss_laser.png")
        self.rect = self.image.get_rect()
        self.rect.midtop = (x, y + 200)
        self.zivotnost = 30
    def update(self):
        self.zivotnost -= 1
        return self.zivotnost <= 0
boss_lasery = []

class BossStrela:
    def __init__(self, x, y):
        self.image = pygame.image.load("Boss_strela.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y + 175)
        self.rect.inflate_ip(0, -50)
        self.rychlost = 15
        self.damage = 2
        
    def update(self):
        self.rect.y += self.rychlost
        
boss_strely = []
        
class PowerUp:
    def __init__(self, x, y, typ):
        self.typ = typ
        if typ == "reload":
            self.image = pygame.image.load("Power_up-reload.png")
        elif typ == "rychlost":
            self.image = pygame.image.load("Power_up-rychlost_strela.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rychlost = 3
    def update(self):
        self.rect.y += self.rychlost
power_ups = []
        
#Střela
class Strela:
    rychlost = -7
    def __init__(self, x, y):
        self.image = pygame.image.load("strela.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rychlost = vychozi_rychlost_strel
        
    def update(self):
        self.rect.y += self.rychlost
        
strely = []

#Nepřátelská střela
class Enstrela:
    def  __init__(self, x, y):
        self.image = pygame.image.load("nepratelska_strela.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.rect.inflate_ip(0, -40)
        self.rychlost = 10
        
    def update(self):
        self.rect.y += self.rychlost
        
enemy_strely = []

#Nepřátelská loď
class enemy:
    def __init__(self, x, y):
        self.image = pygame.image.load("nepratelska_lod.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rychlost = random.choice([4, 5, 6])
        self.smer = 1
        self.hp = 1
        
    def update(self):
        self.rect.x += self.rychlost * self.smer
        if self.rect.right >= sirka_okna or self.rect.left <= 0:
            self.smer *= -1
        if random.randint(1,400) == 1:
            nova_enstrela = Enstrela(self.rect.centerx, self.rect.bottom)
            enemy_strely.append(nova_enstrela)
            
enemies = []

class EasterEgg:
    def __init__(self, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.direction = random.choice([-1, 1])
        if self.direction == 1:
            self.rect.right = sirka_okna
        else:
            self.rect.left = sirka_okna
        self.rect.y = random.randint(50, vyska_okna - 350)
        self.speed = random.randint(10, 25) * self.direction
        
    def update(self):
        self.rect.x += self.speed
        if self.direction == 1 and self.rect.left > sirka_okna:
            return True
        elif self.direction == -1 and self.rect.right < 0:
            return True
        return False
    
easter_egg_active = False
easter_egg_obj = None
easter_egg_chance = 0.0003

#Úrovně
aktualni_uroven = 1
max_uroven = 20
pocet_zabitych_bossu = 0

def uroven(uroven):
    global enemies, boss_active, bhp
    enemies = []
    Strela.rychlost = vychozi_rychlost_strel
    
    if uroven  % 5 == 0:
        boss_active = True
        bhp = Max_bhp
        bship_rect.centerx = sirka_okna // 2
        bship_rect.top = 50
        if uroven >= 6:
            bhp = Max_bhp + 50
            if uroven > 16:
                bhp = Max_bhp + 125
    else:
        boss_active = False
        pocet_rad = 2
        if uroven > 5:
            pocet_rad = 3
        if uroven > 10:
            pocet_rad = 4
        if uroven > 15:
            pocet_rad = 5
            
        enemy_hp = 1
        if uroven >= 6:
            enemy_hp = 2
        if uroven >= 11:
            enemy_hp = 3
        if uroven >= 16:
            enemy_hp = 4

            
        for radek in range(pocet_rad):
            for sloupec in range(7):
                nepritel = enemy(sloupec * 150, 50 + radek * 100)
                nepritel.hp = enemy_hp
                enemies.append(nepritel)

#Pozadí
pozadi1 = pygame.image.load("pozadi-1.jpg")
pozadi1 = pygame.transform.scale(pozadi1, (sirka_okna, vyska_okna))
font = pygame.font.SysFont(None, 74)
text_timer = 0
text_zprava = ""
zobrazit_text = False 

hra_skoncila = False
vyhra = False 

def zobraz_boss_upozorneni():
    okno_aplikace.blit(pozadi1, (0, 0))
    vykresli_text(okno_aplikace, "POZOR! Blíží se BOSS!", font, (255, 0, 0), (sirka_okna // 2 - 250, vyska_okna // 2 - 50))
    pygame.display.update()
    pygame.time.wait(3000)
    
uroven(aktualni_uroven)
pozadi1 = pygame.transform.scale(pozadi1, (sirka_okna, vyska_okna))
    
#Celá smyčka hry
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if udalost.key == pygame.K_SPACE and naboje > 0 and reload_tick == 0:
                nova_strela = Strela(poloha_x + ship_rect.width // 2, poloha_y)
                strely.append(nova_strela)
                naboje -= 1
                if naboje == 0:
                    reload_tick = reload_cas
                    
    #Update reloadu 
    if reload_tick > 0:
        reload_tick -= 1
        if reload_tick == 0:
            naboje = max_naboje
        
    if not hra_skoncila and not v_obchode:      
        #Kontrola lodě, aby neutekla z obrazovky
        if poloha_x < 0:
            poloha_x = 0
        if poloha_x > sirka_okna - ship_rect.width:
            poloha_x = sirka_okna - ship_rect.width
        if poloha_y < vyska_okna // 2:
            poloha_y = vyska_okna // 2
        if poloha_y > vyska_okna - ship_rect.width:
            poloha_y = vyska_okna- ship_rect.width
    
        #Stisknuté klávesy
        stisknute_klavesy = pygame.key.get_pressed()
        if stisknute_klavesy[pygame.K_a]:
            poloha_x -= rychlost
        if stisknute_klavesy[pygame.K_d]:
            poloha_x += rychlost
        if stisknute_klavesy[pygame.K_s]:
            poloha_y += rychlost
        if stisknute_klavesy[pygame.K_w]:
            poloha_y -= rychlost
            
        # Boss logika
        if boss_active:
            # Střílení laseru
            boss_laser_timer += 1
            if boss_laser_timer >= boss_laser_interval:
                boss_laser_timer = 0
                # Varování před laserem
                vykresli_text(okno_aplikace, "!!! LASER !!!", font, (255, 0, 0), (sirka_okna // 2 - 150, vyska_okna // 2))
                pygame.display.update()
                pygame.time.wait(350)  # Krátké upozornění
                # Vystřelení laseru
                novy_laser = BossLaser(bship_rect.centerx, bship_rect.bottom)
                boss_lasery.append(novy_laser)
            
            # Střílení bočních střel
            boss_strela_timer += 1
            if boss_strela_timer >= boss_strela_interval:
                boss_strela_timer = 0
                # Levá střela
                leva_strela = BossStrela(bship_rect.left + 80, bship_rect.bottom)
                boss_strely.append(leva_strela)
                # Pravá střela
                prava_strela = BossStrela(bship_rect.right - 80, bship_rect.bottom)
                boss_strely.append(prava_strela)
        
        # Aktualizace laserů
        for laser in boss_lasery[:]:
            if laser.update():
                boss_lasery.remove(laser)
    
            #Detekce zníčení lodě
        def zpracuj_kolize():
            global penize, bhp, boss_active, vyhra, hra_skoncila, hp, pocet_zabitych_bossu, reload_cas
            # Kontrola kolize laserů s lodí
            for laser in boss_lasery:
                if laser.rect.colliderect(ship_rect):
                    znic_lod()
            
            # Kontrola střel hráče
            for strela in strely[:]:
                if strela.rect.top < 0:
                    strely.remove(strela)
                
                # Kolize s nepřáteli
                for enship in enemies[:]:
                    if strela.rect.colliderect(enship.rect):
                        enship.hp -= 1
                        if enship.hp <= 0:
                            if enship in enemies:
                                enemies.remove(enship)
                                penize += odmena_za_enship
                            
                            if random.randint(1, 100) <= 5:
                                typ = random.choice(["reload", "rychlost"])
                                novy_powerup = PowerUp(enship.rect.centerx, enship.rect.centery, typ)
                                power_ups.append(novy_powerup)
                                
                        if strela in strely:
                            strely.remove(strela)
                            break
                
                # Kolize s bossem
                if boss_active and strela.rect.colliderect(bship_rect):
                    bhp -= 1
                    if strela in strely:
                        strely.remove(strela)
                    if bhp <= 0:
                        boss_active = False
                        penize += odmena_za_bosse
                        pocet_zabitych_bossu += 1
                    if pocet_zabitych_bossu >= 4:
                        vyhra = True
                        hra_skoncila = True
                        
            # Kontrola nepřátelských střel
            for enstrela in enemy_strely[:]:
                if enstrela.rect.bottom > vyska_okna:
                    enemy_strely.remove(enstrela)
                if enstrela.rect.colliderect(ship_rect):
                    if enstrela in enemy_strely:
                        enemy_strely.remove(enstrela)
                        znic_lod()
                        
            # Kontrola boss střel
            for bstrela in boss_strely[:]:
                if bstrela.rect.bottom > vyska_okna:
                    boss_strely.remove(bstrela)
                if bstrela.rect.colliderect(ship_rect):
                    if bstrela in boss_strely:
                        boss_strely.remove(bstrela)
                        #Větší poškození než běžná střela
                        hp -= bstrela.damage
                        if hp <= 0:
                            hra_skoncila = True
                            vyhra = False
                            
            # Update power-upů
            for powerup in power_ups[:]:
                powerup.update()
                # Odstranit power-up, pokud vypadne z obrazovky
                if powerup.rect.top > vyska_okna:
                    power_ups.remove(powerup)
                # Kolize s lodí hráče
                elif powerup.rect.colliderect(ship_rect):
                    global reload_cas, text_timer, text_zprava, zobrazit_text
                    if powerup.typ == "reload":
                        # Efekt: rychlejší reload (snížení reload_cas o 20%, minimum 15)
                        reload_cas = max(15, int(reload_cas * 0.8))
                        text_zprava = "Rychlejší reload!"
                        pygame.display.update()
                    elif powerup.typ == "rychlost":
                        # Efekt: rychlejší střely pro všechny budoucí střely
                        Strela.rychlost -= 2  # Střely jsou rychlejší (menší záporné číslo = rychlejší pohyb nahoru)
                        text_zprava = "Rychlejší střely!"
                        
                    zobrazit_text = True
                    text_timer = 60
                    power_ups.remove(powerup)
                    
            #Update hitboxu  
            ship_rect.topleft = (poloha_x, poloha_y)
    
        #Update
        for strela in strely:
            strela.update()
        for enship in enemies:
            enship.update()
        for enstrela in enemy_strely:
            enstrela.update()
        for bstrela in boss_strely:
            bstrela.update()
            
        zpracuj_kolize()
                
        # Kontrola, zda jsou všichni nepřátelé zničeni
        if not enemies and not boss_active and not hra_skoncila:
            if aktualni_uroven < max_uroven:
                nasledujici_uroven = aktualni_uroven + 1
                bude_boss = nasledujici_uroven % 5 == 0
                
                vykresli_text(okno_aplikace, f"Úroveň {aktualni_uroven + 1}!", font, (22, 249, 255), (sirka_okna // 2 - 250, vyska_okna // 2 - 50))
                pygame.display.update()
                pygame.time.wait(2000)
                
                #Otevření obchodu
                v_obchode = True
                zobraz_obchod()
                
                if bude_boss:
                    zobraz_boss_upozorneni()
                
                #Přechod na další úroveň
                aktualni_uroven += 1
                uroven(aktualni_uroven)
                #Dopnění životů
                hp = max_hp
            else:
                vyhra = True
                hra_skoncila = True
                
    if zobrazit_text:
        text_timer -= 1
        if text_timer <= 0:
            zobrazit_text = False
    # Easter egg logika
    if not easter_egg_active and not hra_skoncila and not v_obchode:
        if random.random() < easter_egg_chance:
            easter_egg_active = True
            easter_egg_obj = EasterEgg("Easter_egg.png")
    
    # Aktualizace easter eggu pokud je aktivní
    if easter_egg_active and easter_egg_obj:
        if easter_egg_obj.update():
            easter_egg_active = False
            easter_egg_obj = None
            
    #Vykreslení 
    okno_aplikace.blit(pozadi1, (0, 0))
    if not hra_skoncila and not v_obchode:
        if boss_active:
            okno_aplikace.blit(bship, bship_rect.topleft)
        for laser in boss_lasery:
            okno_aplikace.blit(laser.image, laser.rect.topleft)
        okno_aplikace.blit(ship, (poloha_x, poloha_y))
        for strela in strely:
            okno_aplikace.blit(strela.image, strela.rect.topleft)    
        for enstrela in enemy_strely:
            okno_aplikace.blit(enstrela.image, enstrela.rect.topleft)
        for bstrela in boss_strely:
            okno_aplikace.blit(bstrela.image, bstrela.rect.topleft)
        for enship in enemies:
            okno_aplikace.blit(enship.image, enship.rect.topleft)
        vykresli_staty()
        for powerup in power_ups:
            okno_aplikace.blit(powerup.image, powerup.rect.topleft)
        if zobrazit_text:
            vykresli_text(okno_aplikace, text_zprava, volba_font, (255, 255, 0), (poloha_x, poloha_y - 30))
        if easter_egg_active and easter_egg_obj:
            okno_aplikace.blit(easter_egg_obj.image, easter_egg_obj.rect)
    else:
        if vyhra:
            vykresli_text(okno_aplikace, "Jsi vítěz :3 Dokončil jsi všechny úrovně!", font, (22, 249, 255), (sirka_okna // 2 - 500, vyska_okna // 2 - 50))
            vykresli_text(okno_aplikace, f"Peníze:${penize}", font, (50, 205, 50), (sirka_okna // 2 - 250, vyska_okna // 2 + 50))
        else:
            vykresli_text(okno_aplikace, "Tvoje loď byla zničena (-_-) Prohrál jsi!", font, (22, 249, 255), (sirka_okna // 2 - 500, vyska_okna // 2 - 50))
    if not v_obchode:    
        pygame.display.update()
        fps_casovac.tick(60)
