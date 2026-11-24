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
    
    
class Armada:
    def __init__(self, nazev:str):
        self.nazev = nazev 
        self.vojaci = []
        pass

    def naberVojaka(self, vojak: Vojak):
        self.vojaci.append(vojak)
        print(f"Zaražen do jednotky: {vojak.hodnost}, {vojak.jmeno}")

    def vypisArmadu(self):
        if len(self.vojaci) == 0:
            print(f"Jednotka {self.nazev} je prázdná.")
        else:
            print(f"-----Sestava jednotky {self.nazev}---")
            for v in self.vojaci:
                print("-->", v)
    
    def odstranPadle(self):
        prezivsi = []
        for v in self.vojaci:
            if v.zdravi > 0:
                prezivsi.append(v)
            else:
                print(f"Padl v boji: {v.hodnost}, {v.jmeno}")
        self.vojaci = prezivsi
    
    def hromadnaAkce(self):
        if len(self.vojaci) == 0:
            print("Nemáme žádné vojáky pro bitvu!")
            return
        print(f"Jednotka {self.nazev} vyráží do boje")
        for v in self.vojaci:
            print(v.bitva())

##testovaciVojak = Vojak("Karl von Bahnhof", "Vojín")
armada = Armada("Armada Leonida")
while True:
    print("="*30)
    print("=== HLAVNÍ MEU VELITELE ===")
    print("="* 30)
    print("1. Nabrav Vojáky")
    print("2. Výpis armády")
    print("3 Trénink vojáků")
    print("4 Hromadná bitva")
    print("5 Konec programu")

    volba = input("Zadej číslo akce (1-5)")

    match volba:
        case "1":
            jmeno = input("Zadej jmeno vojáka.")
            armada.naberVojaka(Vojak(jmeno,"vojín"))
        case "2":
            armada.vypisArmadu()
        case "3":
            if len(armada.vojaci) == 0:
                print("Jednotka je prázdná, nikdo netrénuje.")
            else:
                print("Hromadný trénink")
                for v in armada.vojaci:
                    print(v.trenuj())
        case "4":
            armada.hromadnaAkce()
        case "5":
            print("Velitel opouští základnu. Hra ukončena")
            break 
        case _:
            print("neplatná volba. Zkus to znovu")
#armada.naberVojaka(testovaciVojak)
#armada.hromadnaAkce()
#armada.odstranPadle()
#print(testovaciVojak)
#armada.vypisArmadu()
#print(testovaciVojak.trenuj())
#print(testovaciVojak.bitva())