# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:44:44 2019

@author: aguevara
"""


try:
    from MSE.Structs.GameStructs.DatHeader import DatFile
    from MSE.StructsconstructBoilerplate import *
except:
    from DatHeader import DatFile
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *

#common/text/steam/ot_armor_eng.gmd
#common/text/steam/ot_series_eng.gmd

OAmDatEntry = Struct(
    "id" / UInt32,
    "set_id" / UInt16,
    "equip_slot" / UByte,
    "unk1" / UByte,
    "defense" / UInt32,
    "rarity" / UByte,
    "order" / UInt16,
    "model_id" / UInt32,
    "crafting_cost" / UInt32,
    "variant" / UByte,
    "unk2" / UByte,
    "unk3" / UByte,
    "unk4" / UByte,
    "fire_res" / Byte,
    "water_res" / Byte,
    "ice_res" / Byte,
    "thunder_res" / Byte,
    "dragon_res" / Byte,
    "unk5" / UInt32,
    "set_group" / UInt16,
    "gmd_name_index" / UInt16,
    "gmd_desc_index" / UInt16,
)
class OAmDat(DatFile):
    datEntry = OAmDatEntry

#common/text/steam/ot_weapon_eng.gmdcommon/text/steam/ot_weapon_eng.gmd

OWpDatEntry = Struct(
    "id" / UInt32,
    "set_id" / UInt16,
    "element_id" / UByte,
    "attack_type" / UByte,
    "unkn5" / UByte,
    "raw_damage_melee" / UInt16,
    "raw_damage_ranged" / UInt16,
    "element_damage" / UInt16,
    "affinity" / Int16,
    "defense" / UInt16,
    "elderseal" / UByte,
    "rarity" / UByte,
    "order" / UInt16,
    "unkn14" / UInt16,
    "unkn15" / UInt16,
    "crafting_cost" / UInt32,
    "set_group" / UInt16,
    "gmd_name_index" / UInt16,
    "gmd_description_index" / UInt16,
)

class OWpDat(DatFile):
    datEntry = OWpDatEntry