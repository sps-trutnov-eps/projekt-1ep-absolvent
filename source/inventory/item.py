class Item:
    def __init__(self, x, y, textura, nazev_itemu, lore: str = ""):
        self.x = x
        self.y = y

        self.nazev = nazev_itemu
        self.lore = lore

        self.textura = textura

    def nakresli(self, okno):
        okno.blit(self.textura, [self.x, self.y])
