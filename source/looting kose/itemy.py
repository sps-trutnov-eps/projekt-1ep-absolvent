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
    "derava_cepice": pygame.image.load("source//textury//derava_cepice.png"),
    "derave_tricko": pygame.image.load("source//textury//derave_tricko.png"),
    "derave_kalhoty": pygame.image.load("source//textury//derave_kalhoty.png"),
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

def newItem(item_name, x, y):
    return {
        "x": x,
        "y": y,
        "textura": f"source//textury//{item_name}.png",
        "nazev": item_name,
        "staty": newStats(item_name)
    }

def newStats(nazev):
    if nazev == "energy_drink":
        return {
            "energie": 2,
            "speed_boost": 20
        }
    
    if nazev == "ohryzek":
        return {
            "potrava": 2
        }
    
    if nazev == "kebab":
        return {
            "potrava": 15
        }
    
    if nazev == "noviny":
        return {
            "fire_stage": 1 / 2
        }
    
    if nazev == "lahev":
        return {
            "cena": 3
        }
    
    if nazev == "krabicak":
        return {
            "potrava": 1
        }
    
    if nazev == "hodinky":
        return {
            "cena": 25
        }
    
    if nazev == "tuzemak":
        return {
            "potrava": 1
        }
    
    if nazev == "derava_cepice":
        return {
            "izolace": 3
        }
    
    if nazev == "derave_tricko":
        return {
            "izolace": 4
        }
    
    if nazev == "derave_kalhoty":
        return {
            "izolace": 5
        }
    
    if nazev == "pizza":
        return {
            "potrava": 12
        }
    
    if nazev == "burger":
        return {
            "potrava": 13
        }