# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:13:12 2019

@author: AsteriskAmpersand
"""

monsterGuildcardList = [
     #"Great_Jagras"
     #"Kulu_Ya_Ku"
     #"Pukei_Pukei"
     #"Barroth"
     #"Jyuratodus"
     #"Tobi_Kadachi"
     #"Anjanath"
     #"Rathian"
     #"Tzitzi_Ya_Ku"
     #"Paolumu"
     #"Great_Girros"
     #"Radobaan"
     #"Legiana"
     #"Odogaron"
     #"Rathalos"
     #"Diablos"
     #"Kirin"
     #"Zorah_Magdaros"
     #"Dodogama"
     #"Pink_Rathian"
     #"Bazelgeuse"
     #"Lavasioth"
     #"Uragaan"
     #"Azure_Rathalos"
     #"Black_Diablos"
     #"Nergigante"
     #"Teostra"
     #"Kushala_Daora"
     #"Vaal_Hazak"
     #"Xenojiiva"
     #"Deviljho"
     #"Kulve_Taroth"
     #"Lunastra"
     #"Behemoth"
     #"Leshen"
     #"Ancient_Leshen"
     ]

class guildcardMonster():
    def __init__(self,index):
        self.monsterData = (monsterGuildcardList[-1] 
                            if index > len(monsterGuildcardList) 
                            else monsterGuildcardList[index])
    def getSize(self, indexVal):
        return indexVal
        
class guildcardMonsterData():
    def __init__(self, cardIndex, monsterStats):
        self.monster = guildcardMonster(cardIndex)
        self.captureCount = monsterStats.captured
        self.smallest = self.monster.getSize(monsterStats.smallest)
        self.largest = self.monster.getSize(monsterStats.largest)
        self.researchLevel = monsterStats.researchLevel

class GuildcardTab():
    def __init__(self, hunter,shared):
        self.hunter = hunter
        self.shared = shared
        