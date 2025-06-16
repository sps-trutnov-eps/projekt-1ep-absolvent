def newStats(nazev):
    if nazev == "temp":
        return {
            "temp": None
        }

def newItem(x, y, textura, nazev):
    return {
        "x": x,
        "y": y,
        "textura": textura,
        "nazev": nazev,
        "staty": newStats(nazev)
    }
