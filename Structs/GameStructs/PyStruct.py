# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:52:29 2019

@author: AsteriskAmpersand
"""

class PyStruct():
    def __init__(self, filePath):
        with open(filePath,"rb") as file:
            binData = file.read()
        self.structData = self.struct.parse(binData)