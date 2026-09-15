class Hero:
    def __init__(self, jmeno:str, lvl:int, lokace:str = "vychozi hodnota"):
        self.jmeno = jmeno
        self.lvl = lvl
        self.lokace = lokace
        pass
    
    def pokrik(self):
        return "???"
    
    def predstav_se(self):
        return f"Jsem {self.jmeno} a mám level {self.lvl}"
    
    def kde_jsi(self):
        return f"Nacházím se {self.lokace}"
    
    def presun_se(self, novaLokace:str):
        self.lokace = novaLokace
        return f"Šel jsem na {novaLokace}"

    

hrdina = Hero("King", 20,"Zeme")
print(hrdina.jmeno)
print(hrdina.lvl)
print(hrdina.predstav_se())
print(hrdina.kde_jsi())
print(hrdina.presun_se("Mars"))
