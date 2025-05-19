
import pygame
class Shop:
    def __init__(self,main_buttony,image):
        
        self.main_buttony = main_buttony
        self.image=image
        self.option1 = self.main_buttony["option1/3button"]
        self.option2 = self.main_buttony["option1/2button"]
        self.option3 = self.main_buttony["option1/1button"]
        self.chosen_letadlo=0
        self.chosen_raketa=0
        self.letadlo = 0
        self.zmena =0
        self.moznost = 0
        self.shop = True
        self.lobby = False
        self.rakety = 0
        self.obrazky_option1 =[self.main_buttony["preview1/1"],self.main_buttony["preview1/2"],self.main_buttony["preview1/3"]]
        self.obrazky_option2 = [self.main_buttony["preview2/1"],self.main_buttony["preview2/2"],self.main_buttony["preview2/3"]]
        self.value_zmenena=False
        self.peníze = 0
        self.letadlo_owned =0
        self.raketa_owned =0
        
        
    def draw_shop(self,screen):
        
        screen.blit(self.image,(0,0))
        screen.blit(self.main_buttony["option_1"],self.main_buttony["pozice_option_1"])
        screen.blit(self.main_buttony["option_2"],self.main_buttony["pozice_option_2"])
        
        
        
    def choose(self,event,screen):
        if self.moznost == 1:
            screen.blit(self.obrazky_option1[self.chosen_letadlo],(100,100))
        if self.moznost == 2:
            screen.blit(self.obrazky_option2[self.chosen_raketa],(100,100))
        self.value_zmenena = False
#_________________________________________________________________________________________________________________________________________________________________________                         
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            if self.main_buttony["pozice_option_1"].collidepoint(event.pos):
                self.option1 = self.main_buttony["option1/3button"]
                self.option2 = self.main_buttony["option1/2button"]
                self.option3 = self.main_buttony["option1/1button"]
                self.moznost = 1
# co se děje v option1 a jaké vlastnosti dostane každá možnost___________________________________________________________________________________________________________                
            if self.moznost == 1:
                
                if self.main_buttony["pozice_buttonu1"].collidepoint(event.pos):
                    
                    if  self.letadlo_owned >= 2:
                        
                        self.chosen_letadlo = 2
                        #zde napište co chcete aby se změnilo
                    elif self.peníze >= 2000:#cena
                        self.peníze-=2000
                        self.chosen_letadlo = 2
#_________________________________________________________________________________________________________________________________________________________________________                    
                elif self.main_buttony["pozice_buttonu2"].collidepoint(event.pos)  :
                    
                    if self.letadlo_owned >= 1:
                        
                        self.chosen_letadlo = 1
                        #zde napište co chcete aby se změnilo
                    elif self.peníze >= 1000:
                        self.peníze-=1000
                        self.chosen_letadlo = 1
#_________________________________________________________________________________________________________________________________________________________________________                        
                elif  self.main_buttony["pozice_buttonu3"].collidepoint(event.pos) :
                    
                    self.chosen_letadlo = 0
                    #zde napište co chcete aby se změnilo
            if self.letadlo_owned < self.chosen_letadlo: # funkce pro vlastnění letadlo čím nižší číslo tím více toho vlastním
                self.letadlo_owned = self.chosen_letadlo
               
               
#_________________________________________________________________________________________________________________________________________________________________________                    
            if self.main_buttony["pozice_option_2"].collidepoint(event.pos):
                self.option1 = self.main_buttony["option2/3button"]
                self.option2 = self.main_buttony["option2/2button"]
                self.option3 = self.main_buttony["option2/1button"]
                self.moznost = 2
#_________________________________________________________________________________________________________________________________________________________________________                
            if self.moznost == 2:
                
                if self.main_buttony["pozice_buttonu1"].collidepoint(event.pos) :                
                    if self.raketa_owned >= 2:
                        self.chosen_raketa = 2
                        self.presnost=8
                        
                    elif self.peníze >= 2000:
                        self.peníze-=2000
                        self.chosen_raketa = 2
                    
                    
                    
#_________________________________________________________________________________________________________________________________________________________________________                        
                elif self.main_buttony["pozice_buttonu2"].collidepoint(event.pos):
                    
                    if self.raketa_owned >= 1:
                        self.chosen_raketa = 1
                        self.presnost=6
                        
                    elif self.peníze >= 1000:
                        self.peníze-=1000
                        self.chosen_raketa = 1
                    
#_________________________________________________________________________________________________________________________________________________________________________                        
                elif  self.main_buttony["pozice_buttonu3"].collidepoint(event.pos) :
                    self.chosen_raketa = 0
                    self.presnost=5
#_________________________________________________________________________________________________________________________________________________________________________                        
                if self.raketa_owned < self.chosen_raketa: # funkce pro vlastnění letadlo čím nižší číslo tím více toho vlastním
                    self.raketa_owned = self.chosen_raketa
                    print(self.raketa_owned)
                
                    
                
               
            
         
                
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
            return  self.list_animací[self.chosen_raketa][self.animace1]
        
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
            
                
        
            
                    
      
