import random 

class Vojak:
    def __init__(self, jmeno:str,hodnost:str,zdravi:int=100, energie:int=100):
        self.jmeno = jmeno
        self.hodnost = hodnost 
        self.zdravi = zdravi
        self.energie = energie 
        pass

    def __str__(self):
        return f"{self.hodnost} {self.jmeno} (zdraví: {self.zdravi} a energie: {self.energie}%)"
    
    def trenuj(self):
        vydej = random.randint(15,30)
        if self.energie >= vydej:
            self.energie -= vydej
            return f"{self.hodnost}, {self.jmeno} absolvoval trenink. Ztratil {vydej} % energie."
        else:
            return f"{self.hodnost}, {self.jmeno} je mimo doporučenou fyzickou kondici."

    def bitva(self):
        zraneni = random.randint(10,70)
        self.zdravi = self.zdravi - zraneni 
        if self.zdravi < 0:
            self.zdravi = 0
        return f"{self.hodnost} {self.jmeno} v bitvě utržil zranení {zraneni}%. zbývá {self.zdravi} % zdraví."
    
        





testovaciVojak = Vojak("Karl von Bahnhof", "Vojín")
print(testovaciVojak)
print(testovaciVojak.trenuj())
print(testovaciVojak.bitva())