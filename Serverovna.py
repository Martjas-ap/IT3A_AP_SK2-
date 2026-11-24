import random
from datetime import datetime


class Server:
    def __init__(self, hostname: str, os: str, deployYear: int, warrantyYear: int = 0, storageFree: int = 100):
        self.hostname = hostname
        self.os = os
        self.deployYear = deployYear
        self.warrantyYear = warrantyYear
        self.storageFree = storageFree

    def __str__(self):
        return f"{self.hostname} ({self.os}, {self.deployYear}) - volné místo: {self.storageFree}%"

    def saveData(self):
        pozadavek = random.randint(5, 20)

        if self.storageFree >= pozadavek:
            self.storageFree -= pozadavek
            return f"Na server {self.hostname} se uložila data (zabráno {pozadavek}%). Zbývá {self.storageFree}% volného místa."
        else:
            return f"Chyba: Na serveru {self.hostname} není místo! Potřeba {pozadavek}%, ale k dispozici je jen {self.storageFree}%."

    def cleanDisk(self):
        uvolneno = 100 - self.storageFree
        self.storageFree = 100
        return f"Disky na serveru {self.hostname} byly pročištěny. Uvolnilo se {uvolneno}% místa."

    def warrantyCheck(self):
        if self.warrantyYear < datetime.now().year:
            return f"Záruka serveru {self.hostname} skončila v roce {self.warrantyYear}."
        else:
            return f"Server {self.hostname} je v záruce ještě {self.warrantyYear - datetime.now().year} let."


class ServerRoom:
    def __init__(self, name):
        self.name = name
        self.servers = []

    def addServer(self, server):
        self.servers.append(server)
        print(f"Do serverovny {self.name} byl přidán server {server.hostname}.")

    def showServers(self):
        if len(self.servers) == 0:
            print("Serverovna je prázdná.")
        else:
            for server in self.servers:
                print(f"{server}")

    def oldestServer(self):
        if len(self.servers) == 0:
            return "Není zde žádný server."

        nejstarsi = self.servers[0]

        for server in self.servers:
            if server.deployYear < nejstarsi.deployYear:
                nejstarsi = server

        return nejstarsi

    def avgStorage(self):
        if len(self.servers) == 0:
            return 0

        celkem = 0

        for server in self.servers:
            celkem += server.storageFree

        return celkem / len(self.servers)

    def fullServers(self, limit=30):
        vysledek = []

        for server in self.servers:
            if server.storageFree < limit:
                vysledek.append(server)

        return vysledek

    def serversForReplacement(self):
        vysledek = []

        for server in self.servers:
            if server.warrantyYear < datetime.now().year:
                vysledek.append(server)

        return vysledek

    def countOS(self, targetOS):
        pocet = 0

        for server in self.servers:
            if server.os == targetOS:
                pocet = pocet + 1

        return pocet


serverovna = ServerRoom("SOUEPL Datacentrum")

server1 = Server("Web-Main", "Ubuntu Linux", 2018, 2028, 80)
server2 = Server("Database-01", "Windows Server", 2015, 0, 20)
server3 = Server("Backup-01", "Ubuntu Linux", 2021, 2027, 45)

serverovna.addServer(server1)
serverovna.addServer(server2)
serverovna.addServer(server3)

print("Obsah serverovny:")
serverovna.showServers()

print("Ukládání dat:")
for server in serverovna.servers:
    print(server.saveData())

print("Servery po uložení dat:")
serverovna.showServers()

print(f"Průměrné volné místo: {serverovna.avgStorage():}%")

print(f"Nejstarší hardware: {serverovna.oldestServer()}")

print("Kontrola záruky:")
for server in serverovna.servers:
    print(server.warrantyCheck())

print("Servery, které potřebují pročistit disk:")
serveryNaProcisteni = serverovna.fullServers(50)
for server in serveryNaProcisteni:
    print(f"{server}")

print("Servery po záruce:")
serveryPoZaruce = serverovna.serversForReplacement()
for server in serveryPoZaruce:
    print(f"{server}")

print(f"Počet serverů s Ubuntu Linux: {serverovna.countOS('Ubuntu Linux')}")
