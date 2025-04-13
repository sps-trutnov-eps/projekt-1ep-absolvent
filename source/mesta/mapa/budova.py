import pygame as pg

class Budova:
    def __init__(self, okno, vlevo_x, nahore_y, sirka, vyska, textura, barva_hitboxu = (0, 0, 255)):
        self.okno = okno

        self.obdelnik = pg.Rect(vlevo_x, nahore_y, sirka, vyska)
        self.textura = textura
        self.barva = barva_hitboxu

    def hitbox(self, objekt):
        '''
        udela hitboxi s objektem
        '''

        objekt.x += objekt.rychlost_x

        zed_ctverec  = pg.Rect(self.obdelnik.x, self.obdelnik.y, self.obdelnik.width, self.obdelnik.height)
        objekt_ctverec = pg.Rect(objekt.x, objekt.y, objekt.sirka, objekt.vyska)

        if zed_ctverec.colliderect(objekt_ctverec):

            if objekt_ctverec.left <= zed_ctverec.right <= objekt_ctverec.right:
                objekt.rychlost_x = 0
                objekt.x = zed_ctverec.right

            if objekt_ctverec.left <= zed_ctverec.left <= objekt_ctverec.right:
                objekt.rychlost_x = 0
                objekt.x = zed_ctverec.left - objekt.sirka

        objekt.x -= objekt.rychlost_x
        objekt.y += objekt.rychlost_y

        zed_ctverec  = pg.Rect(self.obdelnik.x, self.obdelnik.y, self.obdelnik.width, self.obdelnik.height)
        objekt_ctverec = pg.Rect(objekt.x, objekt.y, objekt.sirka, objekt.vyska)

        if zed_ctverec.colliderect(objekt_ctverec):

            if objekt_ctverec.top <= zed_ctverec.top <= objekt_ctverec.bottom:
                objekt.rychlost_y = 0
                objekt.nazemi = True
                objekt.y = zed_ctverec.top - objekt.vyska

            elif objekt_ctverec.top <= zed_ctverec.bottom <= objekt_ctverec.bottom:
                objekt.rychlost_y = 0
                objekt.y = zed_ctverec.bottom

        objekt.y -= objekt.rychlost_y

    def nakresli(self, okno, offset = [0, 0]):
        okno.blit(self.textura, (self.obdelnik.x + offset[0], self.obdelnik.y + offset[1]))

    def nakresliHitbox(self, okno, offset = [0, 0]):
        pg.draw.rect(okno, self.barva, (self.obdelnik.x + offset[0], self.obdelnik.y + offset[1], self.obdelnik.width, self.obdelnik.height))
