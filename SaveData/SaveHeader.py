# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:45:17 2019

@author: AsteriskAmpersand
"""

class SaveHeader():
    def __init__(self,header):
        self.unkn0 = header.unkn0
        self.unkn1 = header.unkn1
        self.steamID = header.steamID
        #check bounds when writing steamID