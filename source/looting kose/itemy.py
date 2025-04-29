import pygame

textury = {
    "bobek": pygame.image.load("source//textury//bobek.png"),
    "ohryzek": pygame.image.load("source//textury//ohryzek.png"),
    "kebab": pygame.image.load("source//textury//kebab.png"),
    "noviny": pygame.image.load("source//textury//noviny.png"),
    "lahev": pygame.image.load("source//textury//lahev.png"),
    "krabicak": pygame.image.load("source//textury//krabicak.png"),
    "hodinky": pygame.image.load("source//textury//hodinky.png"),
    "tuzemak": pygame.image.load("source//textury//tuzemak.png"),
    "energetak": pygame.image.load("source//textury//energetak.png"),
    "derava_cepice": pygame.image.load("source//textury//cepice.png"),
    "derave_tricko": pygame.image.load("source//textury//tricko.png"),
    "derave_kalhoty": pygame.image.load("source//textury//kalhoty.png"),
    "pizza": pygame.image.load("source//textury//pizza.png"),
    "burger": pygame.image.load("source//textury//burger.png")
}

class Item:
    def __init__(self, textura, pozice, nazev):
        self.textura = textura
        self.nazev = nazev

        self.pozice = pozice

    def vykresli(self, okno):
        okno.blit(self.textura, self.pozice)