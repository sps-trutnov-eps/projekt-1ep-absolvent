import pygame
pygame.init()
class Itemy:
        def __init__(self, okno):
                self.okno = okno

                self.textura_bobku = pygame.image.load("source//textury//bobek.png")
                self.textura_ohryzku = pygame.image.load("source//textury//ohryzek.png")
                self.textura_kebabu = pygame.image.load("source//textury//kebab.png")
                self.textura_novin = pygame.image.load("source//textury//noviny.png")
                self.textura_lahve = pygame.image.load("source//textury//lahev.png")
                self.textura_krabicaku = pygame.image.load("source//textury//krabicak.png")
                self.textura_hodinek = pygame.image.load("source//textury//hodinky.png")
                self.textura_tuzemaku = pygame.image.load("source//textury//tuzemak.png")
                self.textura_energetaku = pygame.image.load("source//textury//energetak.png")
                self.textura_derave_cepice = pygame.image.load("source//textury//cepice.png")
                self.textura_derave_tricko = pygame.image.load("source//textury//tricko.png")
                self.textura_derave_kalhoty = pygame.image.load("source//textury//kalhoty.png")
                self.textura_pizza = pygame.image.load("source//textury//pizza.png")
                self.textura_burger = pygame.image.load("source//textury//burger.png")
        
        def bobek(self, x, y):
                self.okno.blit(self.textura_bobku, (x, y))
                self.time_debuffu = 1500

        def ohryzek(self, x, y):
                self.okno.blit(self.textura_ohryzku, (x, y))
                
                #kdyz uzito:
                self.food_stat = 12

        def kebab(self, x, y):
                self.okno.blit(self.textura_kebabu, (x, y))
                
                #kdyz uzito:
                self.food_stat = 20

        def noviny(self, x, y):
                self.okno.blit(self.textura_novin, (x, y))

                #kdyz uzito:
                self.burn_time = 1500

        def lahev(self, x, y):
                self.okno.blit(self.textura_lahve, (x, y))

                #kdyz uzito:
                self.cena = 10

        def krabicak(self, x, y):
                self.okno.blit(self.textura_krabicaku, (x, y))
                
                #kdyz uzito:
                self.alko_teplo = 10

        def hodinky(self, x, y):
                self.okno.blit(self.textura_hodinek, (x, y))

                #kdyz uzito:
                self.cena = 50

        def tuzemak(self, x, y):
                self.okno.blit(self.textura_tuzemaku, (x, y))

                #kdyz uzito
                self.alko_teplo = 20

        def energetak(self, x, y):
                self.okno.blit(self.textura_energetaku, (x, y))

                #kdyz uzito:
                self.speed_boost = 5

        def cepice(self, x, y):
                self.okno.blit(self.textura_derave_cepice, (x, y))

        def tricko(self, x, y):
                self.okno.blit(self.textura_derave_tricko, (x, y))

        def kalhoty(self, x, y):
                self.okno.blit(self.textura_derave_kalhoty, (x, y))

        def pizza(self, x, y):
                self.okno.blit(self.textura_pizza, (x, y))

                #kdyz uzito:
                self.food_stat = 15

        def burger(self, x, y):
                self.okno.blit(self.textura_burger, (x, y))

                #kdyz uzito:
                self.food_stat = 25