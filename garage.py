import random
from datetime import datetime
class Auto:
    def __init__(self, znacka:str, model:str,rok:int,stkrok:int,palivo:100):
        self.znacka = znacka 
        self.model = model 
        self.rok = rok 
        self.stkrok = stkrok
        self.palivo = palivo 
        pass 

    
    def __str__(self): #metoda, která se volá jako základní pro výpis vlastností

        return f"{self.znacka} {self.model} {self.rok} - palivo {self.palivo} %"
    
    def move(self):
        spotreba = random.randint(5,20)
        if self.palivo >= spotreba:
            #self.palivo = self.palivo - spotreba
            self.palivo -= spotreba
            return f"auto {self.znacka} model {self.model} spotřeboval {spotreba} % paliva a zbývá mu {self.palivo} %"
        else:
            return f"auto {self.znacka} model {self.model} nemá palivo."
        
    def natankuj(self):
        naplneno = 100 - self.palivo
        self.palivo = 100
        return f"{self.znacka} {self.model} natankovala {naplneno} % paliva"
    
    def STK(self):
        if self.stkrok < datetime.now().year:
            return f"{self.znacka} {self.model} musí na technickou - technická skončila v roce {self.stkrok}"
        else:
            return f"{self.znacka} {self.model} má technickou v pořádku. Na technickou bude muet za následující počet let: {self.stkrok - datetime.now().year}"
        

class Garaz:
    def __init__(self, jmeno):
        self.jmeno = jmeno
        self.auta = []
        pass

    def pridejauta(self, car:Auto):
        self.auta.append(car)
        return f"Do garáže {self.jmeno} bylo přidáno auto: {car.znacka} {car.model}"
    


car1 = Auto("Škoda", "Octavia 3", 2016, 2026, 85)
car2 = Auto("Volkswagen", "Golf 7",2018, 2022, 10)
car3 = Auto("Nissan","Skyline",1999,2014,30)
car4 = Auto ("Toyota", "Hilux", 2014, 2028, 3)

print(car1)
print(car2)
print(car3)
print(car4)

print(car1.move())
print(car2.natankuj())


print(car1.STK())

oblibenagaraz = Garaz("podzemni garaz")

print(Garaz.pridejauta(car1))