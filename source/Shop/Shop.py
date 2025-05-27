
import pygame
class Shop:
    def __init__(self,main_buttony,image):
        
        self.main_buttony = main_buttony
        self.image=image
        self.option1 = self.main_buttony["option1_3button"]
        self.option2 = self.main_buttony["option1_2button"]
        self.option3 = self.main_buttony["option1_1button"]
        self.chosen_letadlo=0
        self.chosen_raketa=0
        self.letadlo = 0
        self.zmena =0
        self.moznost = 0
        self.shop = True
        self.lobby = False
        self.rakety = 0
        self.obrazky_option1 =[self.main_buttony["preview1_1"],self.main_buttony["preview1_2"],self.main_buttony["preview1_3"]]
        self.obrazky_option2 = [self.main_buttony["preview2_1"],self.main_buttony["preview2_2"],self.main_buttony["preview2_3"]]
        self.value_zmenena=False
        self.peníze = 99999990
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
                self.option1 = self.main_buttony["option1_1button"]
                self.option2 = self.main_buttony["option1_2button"]
                self.option3 = self.main_buttony["option1_3button"]
                self.moznost = 1
            # Zpracování výběru možností
            if self.moznost == 1:
                ceny = [0, 1000, 2000]  # cena za letadlo 0, 1, 2
                for i in range(3):
                    if self.main_buttony[f"pozice_buttonu{i+1}"].collidepoint(event.pos):
                        print(self.chosen_letadlo)
                        if self.letadlo_owned >= 2 - i:
                            self.chosen_letadlo = 2 - i
                            
                            # zde napište co chcete aby se změnilo
                        elif self.peníze >= ceny[2 - i]:
                            self.peníze -= ceny[2 - i]
                            self.chosen_letadlo = 2 - i
                            

            # Kontrola vlastnictví letadla (čím nižší číslo, tím více toho vlastním)
            if self.letadlo_owned < self.chosen_letadlo:
                self.letadlo_owned = self.chosen_letadlo
            
        #_________________________________________________________________________________________________________________________________________________________________________
            if self.main_buttony["pozice_option_2"].collidepoint(event.pos):
                
                self.option1 = self.main_buttony["option2_1button"]
                self.option2 = self.main_buttony["option2_2button"]
                self.option3 = self.main_buttony["option2_3button"]
                self.moznost = 2
            # Zpracování výběru možností
            if self.moznost == 2:
                ceny = [0, 1000, 2000]  # cena za letadlo 0, 1, 2
                
                for i in range(3):
                    if self.main_buttony[f"pozice_buttonu{i+1}"].collidepoint(event.pos):
                        
                        if self.letadlo_owned >= 2 - i:
                            self.chosen_letadlo = 2 - i
                            # zde napište co chcete aby se změnilo
                        elif self.peníze >= ceny[2 - i]:
                            self.peníze -= ceny[2 - i]
                            self.chosen_letadlo = 2 - i
                            
                            break  # jakmile jeden button odpovídá, dál nehledáme
                print(self.chosen_letadlo)
            # Kontrola vlastnictví letadla (čím nižší číslo, tím více toho vlastním)
            if self.letadlo_owned < self.chosen_letadlo:
                self.letadlo_owned = self.chosen_letadlo
                
        screen.blit(self.option1,(500,500))
        screen.blit(self.option2,(500,400))
        screen.blit(self.option3,(500,300))
        
        
                
                    
                

                
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
            
                
        
            
                    
      
