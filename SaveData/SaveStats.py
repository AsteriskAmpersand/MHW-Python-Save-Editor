# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 11:07:25 2019

@author: aguevara
"""

class StatsTab():
    def __init__(self,slot):
        self.name = slot.hunterName
        self.rank = slot.hunterRank
        self.money = slot.zenni
        self.research = slot.researchPoints
        self.xp = slot.hunterXP
        self.playtime = slot.playTime_S
        