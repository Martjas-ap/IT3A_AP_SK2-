import random
class Zvire:
    def __init__(self, jmeno:str, vek:int, misto:str = "bouda"):
        self.jmeno = jmeno
        self.vek = vek
        self.misto = misto
        pass
    
    def zvuk(self):
        return "vrr"
    
    
    
    def predstav_se(self):
        return f"Jsem {self.jmeno} a je mi {self.vek}"
    
    def kde_jsi(self):
        return f"Nacházím se {self.misto}"
    
    def jdi_na(self, nMisto:str):
        self.misto = nMisto
        return f"Šel jsem na {nMisto}"




class Pes(Zvire):
    def __init__(self, jmeno: str, vek: int, plemeno:str, misto: str = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.plemeno = plemeno  
    def vycesat(self):
        if(random.randint(0,1) > 0):
            return f"{self.jmeno} utekl"
        else:
            return f"{self.jmeno} se nechal učesat"
    
    def udelej_aport(self):
        return f"{self.jmeno} už k tobě běží"
    
    def predstav_se(self):
        return f"{super().predstav_se()} a jsem {self.plemeno}"


class Kocka(Zvire):
    def __init__(self, jmeno: str, vek: int,barva:str, misto: str = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.barva = barva 
    
    def zvuk(self):
        return("mnau")
    def utok(self):
        return f"{self.jmeno} tě škrábl/a."
    
    def pohladit(self):
        if(random.randint(0,1) > 0):
            return self.utok()
        else:
            return f"{self.jmeno} nechala se pohladit a vrní."

class Had(Zvire):
    def __init__(self, jmeno: str, vek: int, delka:int,jedovaty,misto: str = "bouda"):
        super().__init__(jmeno, vek, misto)
        self.delka = delka 
        self.jedovaty = jedovaty
    def zvuk(self):
        return "ssss"     
    
    def predstav_se(self):
        if self.jedovaty:
            typ = "jedovaty"
        else:
            typ = "škrtič"
        return f"SSssss.... já jsem {self.jmeno}, měřím {self.delka} a jsem {typ}"



Zmije = Had("Kaňour", 2, 15,False,"zoo")

print(Zmije.jmeno,Zmije.delka, Zmije.jedovaty, Zmije.misto)
print(Zmije.zvuk())
print(Zmije.predstav_se())

    

Čokl = Pes("Čoklik", 5, "Mops", "gauč")
Mája = Kocka("Mája", 6, "Šedá", "Škrabadlo" )

"""print(Mája.utok())
print(Mája.zvuk())
print(Mája.pohladit())
"""
    
"""print(Čokl.jmeno, Čokl.plemeno)

print(Čokl.kde_jsi())
print("-" * 20)
print(Čokl.zvuk())
print(Čokl.udelej_aport())
print(Čokl.vycesat())
print(Čokl.predstav_se())

zvire = Zvire("Šoral", 50)
"""
""" print(zvire.jmeno)
print(zvire.vek)
print(zvire.misto)

print(zvire.zvuk())
print(zvire.predstav_se())
print(zvire.kde_jsi())
print(zvire.jdi_na("Kadeřnictví"))
print(zvire.kde_jsi())

zvire2 = Zvire("Wolfram", 32, "PentHouse")

print(zvire2.jmeno)
print(zvire2.vek)
print(zvire2.misto)

print(zvire2.zvuk())
print(zvire2.predstav_se())
print(zvire2.kde_jsi())
print(zvire2.jdi_na("Klokánek"))
print(zvire2.kde_jsi())
"""

zoo = {Čokl, Mája, Zmije}
for obyvatel in zoo: 
    print(obyvatel.predstav_se())
    print(obyvatel.zvuk())
    print("-" * 20)