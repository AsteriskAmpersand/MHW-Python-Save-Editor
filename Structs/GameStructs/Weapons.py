# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 16:54:28 2019

@author: aguevara
"""


try:
    from .DatHeader import DatFile
    from ..constructBoilerplate import *
except:
    from DatHeader import DatFile
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *
    
WpDatEntry = Struct(
	"id" / UInt32,
	"unknown1" / Byte,
	"unknown2" / Byte,
	"base_model_id" / UInt16,
	"part1_id" / UInt16,
	"part2_id" / UInt16,
	"color" / UByte,
	"tree_id" / UByte,
	"is_fixed_upgrade" / UByte,
	"crafting_cost" / UInt32,
	"rarity" / UByte,
	"kire_id" / UByte,
	"handicraft" / UByte,
	"raw_damage" / UInt16,
	"defense" / UInt16,
	"affinity" / Byte,
	"element_id" / UByte,
	"element_damage" / UInt16,
	"hidden_element_id" / UByte,
	"hidden_element_damage" / UInt16,
	"elderseal" / UByte,
	"num_gem_slots" / UByte,
	"gem_slot1_lvl" / UByte,
	"gem_slot2_lvl" / UByte,
	"gem_slot3_lvl" / UByte,
	"wep1_id" / UInt16,
	"wep2_id" / UInt16,
	"unknown3" / UInt32,
	"unknown4" / UInt32,
	"unknown5" / UInt32,
	"tree_position" / UByte,
	"order" / UInt16,
	"gmd_name_index" / UInt16,
	"gmd_description_index" / UInt16,
	"skill_id" / UInt16,
	"unknown6" / UInt16,
)

WpDatGEntry = Struct(
	"index" / UInt32,
	"Byte1" / Byte,
	"Byte2" / Byte,
	"base_model_id" / UInt16,
	"part1_id" / UInt16,
	"part2_id" / UInt16,
	"color" / UByte,
	"tree_id" / UByte,
	"is_fixed_upgrade" / UByte,
	"muzzel_type" / UByte,
	"barrel_type" / UByte,
	"magazine_type" / UByte,
	"scope_type" / UByte,
	"cost" / UInt32,
	"rarity" / UByte,
	"true_damage" / UInt16,
	"defense" / UInt16,
	"affinity" / Byte,
	"element_id" / UByte,
	"element_damage" / UInt16,
	"hidden_element_id" / UByte,
	"hidden_element_damage" / UInt16,
	"elderseal" / UByte,
	"shell_table_id" / UInt16,
	"deviation" / UByte,
	"num_gem_slots" / UByte,
	"gem_slot1_lvl" / UByte,
	"gem_slot2_lvl" / UByte,
	"gem_slot3_lvl" / UByte,
	"unknown31" / Byte,
	"unknown32" / Byte,
	"unknown33" / Byte,
	"unknown34" / Byte,
	"unknown35" / Byte,
	"unknown36" / Byte,
	"unknown37" / Byte,
	"unknown38" / Byte,
	"unknown39" / Byte,
	"unknown40" / Byte,
	"unknown41" / Byte,
	"unknown42" / Byte,
	"unknown43" / Byte,
	"special_ammo_id" / Byte,
	"tree_position" / UByte,
	"order" / UInt16,
	"gmd_name_index" / UInt16,
	"gmd_description_index" / UInt16,
	"skill_id" / UInt16,
	"unknown51" / Byte,
	"unknown52" / Byte,
)

class WpDat(DatFile):
    def __init__(self,filepath):
        self.nameGmd = self.datToText(str(filepath))
        self.descGmd = self.datToText(str(filepath))
        if any((wp in filepath for wp in ["bow","hbg","lbg"])):
            self.datEntry = WpDatGEntry
        else:
            self.datEntry = WpDatEntry
        super().__init__(filepath)
    def datToText(self,dat):
        dat = dat.replace(r"\common\equip",r"\common\text\steam")
        return dat.replace(".wp_dat_g","_eng.gmd").replace(".wp_dat","_eng.gmd")#TODO - Localize

KireEntry = Struct(
    "id" / UInt32,
    "red" / UInt16,
    "orange" / UInt16,
    "yellow" / UInt16,
    "green" / UInt16,
    "blue" / UInt16,
    "white" / UInt16,
    "purple" / UInt16,
)

class Kire(DatFile):
    datEntry = KireEntry

