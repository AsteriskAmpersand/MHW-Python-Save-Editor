# -*- coding: utf-8 -*-
"""
Created on Wed Jan  8 20:28:54 2020

@author: AsteriskAmpersand
"""

from ..GameStructs.GameItems import GameItem

class ItemSlot():
    def __init__(self,item,quantity):
        self.itemData = item
        self.quantity = quantity

class ShortCutSlot():
    def __init__(self,shortcut):
        self.name = shortcut.shortcutname
        self.items = shortcut.items

class LoadoutSlot():
    def __init__(self,loadout,sortIx):
        self.name = loadout.loadoutName
        self.loadoutData = loadout.loadoutData
        self.shortcuts = loadout.shortcuts
        self.sortIndex = sortIx

class ItemContainer():
    @staticmethod
    def createItemSlots(container):
        slots = []
        for item in container:
            slots.append(ItemSlot(GameItem(item.itemID),item.itemQty))
        return slots

class PouchTab(ItemContainer):
    def __init__(self,pouch):
        self.items = self.createItemSlots(pouch.items)
        self.ammo = self.createItemSlots(pouch.ammo)
        self.materials = self.createItemSlots(pouch.unkn)
        self.decorations = self.createItemSlots(pouch.special)
    
class BoxTab(ItemContainer):
    def __init__(self,box):
        self.items = self.createItemSlots(box.items)
        self.ammo = self.createItemSlots(box.ammo)
        self.materials = self.createItemSlots(box.materials)
        self.decorations = self.createItemSlots(box.decorations)
        
class LoadoutTab():
    def __init__(self,loadouts):
        self.loadouts = self.createLoadoutSlots(loadouts.iloadout,loadouts.itemLoadoutSort)
    @staticmethod
    def createLoadoutSlots(loadouts,ordering):
        slots = []
        for loadout,ix in zip(loadouts,ordering):
            slots.append(LoadoutSlot(loadout,ix))
        return slots
            
class ItemTab():
    def __init__(self,pouch,box,loadouts):
        self.pouch = PouchTab(pouch)
        self.itembox = BoxTab(box)
        self.loadouts = LoadoutTab(loadouts)