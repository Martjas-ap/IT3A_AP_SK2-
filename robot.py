class Robot:
    def __init__(self, oznaceni:str, baterie:int, ukol:str = "Vychozi hodnota"):
        self.oznaceni = oznaceni
        self.baterie = baterie 
        self.ukol = ukol 
        pass

    def udelej_zvuk(self):
        return "Píp"
    
    def diagnostika(self):
        return f"Jsem {self.oznaceni} a mám {self.baterie} %"
    
    def aktualni_ukol(self):
        return f"Právě  {self.ukol}"
    
    def zadej_ukol(self, novyUkol:str):
        self.aktualni_ukol = novyUkol
        return f"Právě dělám {novyUkol}"
    
Robutek = Robot("Robutek", 64, "Sedím")

print(Robutek.oznaceni)
print(Robutek.aktualni_ukol())
print(Robutek.oznaceni, Robutek.baterie)
print(Robutek.diagnostika())
print(Robutek.udelej_zvuk())
print(Robutek.zadej_ukol("Zvedám činky"))