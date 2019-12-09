# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:21:57 2019

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

AmUpEntry = Struct(
    "unk1" / UInt16,
    "unk2" / UInt16,
    "unk3" / UInt16,
    "unk4" / UInt16,
    "unk5" / UInt16,
    "unk6" / UInt16,
    "unk7" / UInt16,
    "unk8" / UInt16,
    "unk9" / UInt16,
    "unk10" / UInt16,
    "unk11" / UInt16,
)

class AmUp(DatFile):
    datEntry = AmUpEntry

AmDatEntry = Struct(
    "id" / UInt16,
    "unk1" / Byte,
    "unk2" / Byte,
    "order" / UInt16,
    "variant" / UByte,
    "set_id" / UInt16,
    "type" / UByte,
    "equip_slot" / UByte,
    "defense" / UInt16,
    "mdl_main_id" / UInt16,
    "mdl_secondary_id" / UInt16,
    "icon_color" / UByte,
    "unk3" / Byte,
    "icon_effect" / UByte,
    "rarity" / UByte,
    "crafting_cost" / UInt32,
    "fire_res" / Byte,
    "water_res" / Byte,
    "ice_res" / Byte,
    "thunder_res" / Byte,
    "dragon_res" / Byte,
    "num_gem_slots" / UByte,
    "gem_slot1_lvl" / UByte,
    "gem_slot2_lvl" / UByte,
    "gem_slot3_lvl" / UByte,
    "set_skill1_id" / UInt16,
    "set_skill1_lvl" / UByte,
    "set_skill2_id" / UInt16,
    "set_skill2_lvl" / UByte,
    "skill1_id" / UInt16,
    "skill1_lvl" / UByte,
    "skill2_id" / UInt16,
    "skill2_lvl" / UByte,
    "skill3_id" / UInt16,
    "skill3_lvl" / UByte,
    "gender" / UByte,
    "unk4" / Byte,
    "unk5" / Byte,
    "unk6" / Byte,
    "set_group" / UInt16,
    "gmd_name_index" / UInt16,
    "gmd_desc_index" / UInt16,
    "is_permanent" / UByte,
)

class AmDatUp(DatFile):
    datEntry = AmDatEntry