import pygame
class Shop:
    def __init__(self,main_buttony,image):
        
        self.main_buttony = main_buttony
        self.image=image
        self.option1 = self.main_buttony["f_button"]
        self.option2 = self.main_buttony["myg_button"]
        self.option3 = self.main_buttony["fockerfox_button"]
        self.chosen_letadlo=0
        self.chosen_raketa=0
        self.letadlo = 0
        self.zmena =0
        self.moznost = 0
        self.shop = True
        self.lobby = False
        self.rakety = 0
        self.obrazky_letadel =[self.main_buttony["fockerfox"],self.main_buttony["myg25"],self.main_buttony["F23"]]
        self.obrazky_raket = [self.main_buttony["raketa1"],self.main_buttony["raketa2"],self.main_buttony["raketa3"]]
        self.value_zmenena=False
        self.obratnost = 2.5
        self.presnost=6
        self.peníze = 0
        self.letadlo_owned =0
        self.raketa_owned =0
        
        
        self.firerate = 20
        self.zivoty = 5
        
        
    def draw_shop(self,screen):
        
        screen.blit(self.image,(0,0))
        screen.blit(self.main_buttony["letadla"],self.main_buttony["pozice_letadla"])
        screen.blit(self.main_buttony["rakety"],self.main_buttony["pozice_rakety"])
        screen.blit(self.main_buttony["upgrady"],self.main_buttony["pozice_upgrady"])
        
        
    def choose(self,event,screen):
        if self.moznost == 1:
            screen.blit(self.obrazky_letadel[self.chosen_letadlo],(100,100))
        if self.moznost == 2:
            screen.blit(self.obrazky_raket[self.chosen_raketa],(100,100))
        self.value_zmenena = False
                     
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.main_buttony["pozice_letadla"].collidepoint(event.pos):
                self.option1 = self.main_buttony["f_button"]
                self.option2 = self.main_buttony["myg_button"]
                self.option3 = self.main_buttony["fockerfox_button"]
                self.moznost = 1
                
            if self.moznost == 1:
                
                if self.main_buttony["pozice_buttonu1"].collidepoint(event.pos):
                    
                    if  self.letadlo_owned >= 2:
                        
                        self.chosen_letadlo = 2
                        self.obratnost = 4
                        self.firerate = 10
                        self.zivoty = 7
                        
                    elif self.peníze >= 2000:
                        self.peníze-=2000
                        self.chosen_letadlo = 2
                    
                elif self.main_buttony["pozice_buttonu2"].collidepoint(event.pos)  :
                    
                    if self.letadlo_owned >= 1:
                        
                        self.chosen_letadlo = 1
                        
                        self.obratnost = 3
                        self.firerate = 16
                        self.zivoty = 6
                        
                    elif self.peníze >= 1000:
                        self.peníze-=1000
                        self.chosen_letadlo = 1
                    
                elif  self.main_buttony["pozice_buttonu3"].collidepoint(event.pos) :
                    
                    self.chosen_letadlo = 0
                    
                    self.obratnost = 2.5
                    self.firerate = 20
                    self.zivoty = 5
                    
            if self.letadlo_owned < self.chosen_letadlo: # funkce pro vlastnění letadlo čím nižší číslo tím více toho vlastním
                self.letadlo_owned = self.chosen_letadlo
               
               
                
            if self.main_buttony["pozice_rakety"].collidepoint(event.pos):
                self.option1 = self.main_buttony["r_b_3"]
                self.option2 = self.main_buttony["r_b_2"]
                self.option3 = self.main_buttony["r_b_1"]
                self.moznost = 2
            
            if self.moznost == 2:
                
                if self.main_buttony["pozice_buttonu1"].collidepoint(event.pos) :                
                    if self.raketa_owned >= 2:
                        self.chosen_raketa = 2
                        self.presnost=10
                        
                    elif self.peníze >= 2000:
                        self.peníze-=2000
                        self.chosen_raketa = 2
                    
                    
                    
                    
                elif self.main_buttony["pozice_buttonu2"].collidepoint(event.pos):
                    
                    if self.raketa_owned >= 1:
                        self.chosen_raketa = 1
                        self.presnost=7
                        
                    elif self.peníze >= 1000:
                        self.peníze-=1000
                        self.chosen_raketa = 1
                    
                    
                elif  self.main_buttony["pozice_buttonu3"].collidepoint(event.pos) :
                    self.chosen_raketa = 0
                    self.presnost=6
                    
                if self.raketa_owned < self.chosen_raketa: # funkce pro vlastnění letadlo čím nižší číslo tím více toho vlastním
                    self.raketa_owned = self.chosen_raketa
                    print(self.raketa_owned)
                
                    
                
               
            if self.main_buttony["pozice_upgrady"].collidepoint(event.pos):
                self.option1 = self.main_buttony["f_button"]
                self.option2 = self.main_buttony["myg_button"]
                self.option3 = self.main_buttony["fockerfox_button"]
                self.moznost = 3
                
            if self.moznost == 3:
                
                if self.main_buttony["pozice_buttonu1"].collidepoint(event.pos) :                
                    self.chosen_letadlo = 2
                    
                elif self.main_buttony["pozice_buttonu2"].collidepoint(event.pos):
                    self.chosen_letadlo = 1            
                    
                elif  self.main_buttony["pozice_buttonu3"].collidepoint(event.pos) :
                    self.chosen_letadlo = 0
         
                
        screen.blit(self.option1,self.main_buttony["pozice_buttonu1"])
        screen.blit(self.option2,self.main_buttony["pozice_buttonu2"])
        screen.blit(self.option3,self.main_buttony["pozice_buttonu3"])
                
    def animace(self,fockerfox,f,myg,wanted):
        
        self.list_animací = [fockerfox,myg,f]
        
        
         
            
        if wanted == 1:
            self.zmena -=3
        
            if self.zmena>10:
                self.animace1=0
            else:
                self.animace1=1
            if self.zmena <0:
                self.zmena =20
                
            return  self.list_animací[self.chosen_letadlo][self.animace1]
        
        if wanted == 2:   
            return  self.list_animací[self.chosen_raketa]
        
    def opustit_shop(self,screen,back_button,event):
        
        self.pozice_back = back_button.get_rect(topleft=(1000, 1000))
        screen.blit(back_button,self.pozice_back)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.pozice_back.collidepoint(event.pos):
                self.shop=False
                self.lobby=True
                
            else:
                self.shop = True
                self.lobby = False
            
                
        
            
                    
      
