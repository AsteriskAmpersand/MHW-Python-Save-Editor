# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 18:08:54 2019

@author: AsteriskAmpersand
"""
try:
    from .SaveStats import StatsTab
    from .SaveAppearance import AppearanceTab
    from .SaveGuildcard import GuildcardTab
    from .SaveItem import ItemTab
    from .SaveEquipment import EquipmentTab
    from .SaveInvestigations import InvestigationsTab
    from .SaveDlc import DlcTab
except:
    from SaveStats import StatsTab
    from SaveAppearance import AppearanceTab
    from SaveGuildcard import GuildcardTab
    from SaveItem import ItemTab
    from SaveEquipment import EquipmentTab
    from SaveInvestigations import InvestigationsTab
    from SaveDlc import DlcTab
    
class SaveSlot():
    def __init__(self,slot):
        if slot.slotactive:
            self.stats = StatsTab(slot)
            self.appearance = AppearanceTab(slot.hunterAppearance,slot.palicoAppearance)
            self.guildcards = GuildcardTab(slot.hunterGC, slot.sharedGC)
            self.item = ItemTab(slot.itempouch,slot.itembox,slot.itemLoadouts)
            self.equipment = EquipmentTab(slot.equipslots,slot.equiploadout)
            self.investigations = InvestigationsTab(slot.investigations)
            self.dlc = DlcTab(slot.DLCClaimed)
            self.data=slot
    def clone(self):
        return SaveSlot(self.data.struct.parse(self.serialize()))
    def serialize(self):
        pass

class SaveSlots():
    def __init__(self,binSaveSlots):
        self.slots = [SaveSlot(slot) for slot in binSaveSlots]
