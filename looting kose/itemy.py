import pygame
pygame.init()
class Itemy:
        def __init__(self, okno, textura_bobku, textura_ohryzku, textura_kebabu, textura_novin, textura_lahve, textura_krabicaku, textura_hodinek, textura_tuzemaku, textura_energetaku, textura_derava_cepice, textura_derave_tricko
                        , textura_derave_kalhoty, textura_pizzy, textura_burger):
        
                self.okno = okno

                self.textura_bobku = textura_bobku
                self.textura_ohryzku = textura_ohryzku
                self.textura_kebabu = textura_kebabu        
                self.textura_novin = textura_novin
                self.textura_lahve = textura_lahve
                self.textura_krabicaku = textura_krabicaku
                self.textura_hodinek = textura_hodinek
                self.textura_tuzemaku = textura_tuzemaku
                self.textura_energetaku = textura_energetaku
                self.textura_derava_cepice = textura_derava_cepice
                self.textura_derave_tricko = textura_derave_tricko
                self.textura_derave_kalhoty = textura_derave_kalhoty
                self.textura_pizzy = textura_pizzy
                self.textura_burger = textura_burger

        def bobek(self, x, y):
                self.okno.blit(self.textura_bobku, x, y)
                self.time_debuffu = 1500

        def ohryzek(self, x, y):
                self.okno.blit(self.textura_ohryzku, x, y)
                
                #kdyz uzito:
                self.food_stat = 12

        def kebab(self, x, y):
                self.okno.blit(self.textura_kebabu, x, y)
                
                #kdyz uzito:
                self.food_stat = 20

        def noviny(self, x, y):
                self.okno.blit(self.textura_novin, x, y)

                #kdyz uzito:
                self.burn_time = 1500

        def lahev(self, x, y):
                self.okno.blit(self.textura_lahve, x, y)

                #kdyz uzito:
                self.cena = 1

        def krabicak(self, x, y):
                self.okno.blit(self.textura_krabicaku, x, y)
                
                #kdyz uzito:
                self.alko_teplo = 10

        def hodinky(self, x, y):
                self.okno.blit(self.textura_hodinek, x, y)

                #kdyz uzito:
                self.cena = 25

        def tuzemak(self, x, y):
                self.okno.blit(self.textura_tuzemaku, x, y)

                #kdyz uzito
                self.alko_teplo = 20

        def energetak(self, x, y):
                self.okno.blit(self.textura_energetaku, x, y)

                #kdyz uzito:
                self.speed_boost = 5

        def cepice(self, x, y):
                self.okno.blit(self.textura_derava_cepice, x, y)

        def tricko(self, x, y):
                self.okno.blit(self.textura_derave_tricko, x, y)

        def kalhoty(self, x, y):
                self.okno.blit(self.textura_derave_kalhoty, x, y)

        def pizza(self, x, y):
                self.okno.blit(self.textura_pizzy, x, y)

                #kdyz uzito:
                self.food_stat = 21

        def burger(self, x, y):
                self.okno.blit(self.textura_burger, x, y)

                #kdyz uzito:
                self.food_stat = 25