import random
class Postava:
    def __init__(self, jmeno:str, zdravi:int):
        self.jmeno = jmeno
        self.zdravi = zdravi
        pass
    def predstav_se(self):
        return f"Jmenuju se {self.jmeno}, a mám {self.zdravi} HP"
    
    def utok(self):
        return 0 
    
class Rytir(Postava):
    def __init__(self, jmeno: str,brneni:int, zdravi: int):
        super().__init__(jmeno, zdravi)
        self.brneni = brneni
    
    def utok(self):
        return print(random.randint(10,20), "seknutí mečem")
    
    def zablokuj(self):
        return ("Zablokoval jsem útok")


class Mag(Postava):
    def __init__(self, jmeno: str,mana:int,zdravi: int):
        super().__init__(jmeno, zdravi)
        self.mana = mana 
    
    def utok(self):
        if self.mana >= 10:
            self.mana = self.mana - 10
            poskozeni = random.randint(25,40)
            return f"{self.jmeno}dává poškození {poskozeni}, zbývá  {self.mana}"
        else: 
            print("Musím utocit slabe holí, poškození 5")
    

class Lukostrelec(Postava):
    def __init__(self, jmeno: str, zdravi: int, pocet_sipu = 20):
        super().__init__(jmeno, zdravi)
        self.pocet_sipu = pocet_sipu
    
    def palba(self,):
        self.pocet_sipu = 50
        spotreba_sipu = int(input("Zadej kolik mám spotřebovat šípů:"))
        konecny_pocet_sipu = self.pocet_sipu - spotreba_sipu
        return f"Zbylo ti {konecny_pocet_sipu} šípů."
    

druzina = []


valecnik = Mag("Jáchym", 10, 150)
mistr_luku = Lukostrelec("Vašek", 100, 30)

print(mistr_luku.palba())
print(mistr_luku.predstav_se())
print(valecnik.predstav_se())





