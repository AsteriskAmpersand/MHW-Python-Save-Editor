# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 17:45:17 2019

@author: AsteriskAmpersand
"""

class SaveHeader():
    def __init__(self,header):
        self.data = header
        self.steamID = header.steamID
        self.dataHash = header.dataHash
        #check bounds when writing steamID