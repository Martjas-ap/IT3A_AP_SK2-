class Motorka:
    def __init__(self, znacka:str, kategorie:str, stav_nadrze:int, stav_stojanku:str = "Výchozí hodnota"):
        self.znacka = znacka 
        self.kategorie = kategorie
        self.stav_nadrze = stav_nadrze
        self.stav_stojanku = stav_stojanku
        pass

    def zatoc_plyn(self):
        return "VRMM VRMM"
    
    def stav_stojanku_vypis(self):
        return f"Práve je stojánek {self.stav_stojanku}"
    
    def popis_moto(self):
        return f"Jsem {self.znacka}, {self.kategorie}. A mám {self.stav_nadrze} litrů nádrže a můj stav stojánku je {self.stav_stojanku}."
    
    def zmen_stojanek(self, novystavstojanku:str):
        self.stav_stojanku = novystavstojanku
        return f"Stojánek je {novystavstojanku}"

    def popojed20(self, pp20:int):
        self.stav_nadrze = self.stav_nadrze - pp20
        return f"stav nádrže je {self.stav_nadrze}"
    
    def vypis_palivo(self,):
        return f"Stav nádrže je: {self.stav_nadrze} l"
    
    def natankuj_mnozstvi(self, mnozstvi:int):
        self.stav_nadrze = self.stav_nadrze + mnozstvi 
        return f"Finální množství paliva je {self.stav_nadrze}"


Chopper = Motorka("Chopper", "Hustá_Motorka", 30, "Nahoře")

print(Chopper.popis_moto())
print(Chopper.stav_stojanku)
print(Chopper.zmen_stojanek("Dole"))
print(Chopper.popojed20(20))
print(Chopper.vypis_palivo())
print(Chopper.natankuj_mnozstvi(50))