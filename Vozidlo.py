import random 
class Vozidlo:
    def __init__(self, znacka:str, rok_vyroby:int, stav_nadrze:100):
        self.znacka = znacka 
        self.rok_vyroby = rok_vyroby
        self.stav_nadrze = stav_nadrze
        pass
    
    def zvuk_motoru(self):
        return "????"
    
    def info(self):
        return f"jsem {self.znacka}, jsem vyroben v roce {self.rok_vyroby}, mám natankováno {self.stav_nadrze}"
    
    def startuj(self):
        if self.stav_nadrze > 0:
            return f"{self.zvuk_motoru()} Nastartoval"
        else: 
            return "Nemám dost štávy"
    

class Auto(Vozidlo):
    def __init__(self, znacka: str, rok_vyroby: int,typ_prevodovky:str, stav_nadrze: 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.typ_prevodovky = typ_prevodovky 

    def zvuk_motoru(self):
        return "Vrrrm Vrmm!"
    
    def Klakson(self):
        return "Píp píp"


class Moped(Vozidlo):
    def __init__(self, znacka: str, rok_vyroby: int,ma_slapadla:bool,stav_nadrze: 100):
        super().__init__(znacka, rok_vyroby, stav_nadrze)
        self.ma_slapadla = ma_slapadla

    def zvuk_motoru(self):
        return "Trrrrrr!"

    def slapej(self):
        if self.ma_slapadla == True:
            print("Šlapu!")
        else: 
            print("Nemám šlapadla, nemůžu šlapat")


garaz = []

faro = Auto("Škoda", 2014, "Manuální", 70)
muj_mopedak = Moped("Babeta", 1960, True, 0)

garaz.append(faro)
garaz.append(muj_mopedak)

for vozidlo in garaz:
    print(vozidlo.info())
    print("-" * 2)
    print(vozidlo.startuj())

    
    

        
        
    

