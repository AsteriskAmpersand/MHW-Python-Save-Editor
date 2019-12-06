# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:44:44 2019

@author: aguevara
"""
from Construct import Struct
from Construct import this
from Construct import Int8sl as Byte
from Construct import Int8ul as UByte
from Construct import Int16sl as Int16
from Construct import Int16ul as UInt16
from Construct import Int32sl as Int32
from Construct import Int32ul as UInt32
from Construct import Int64sl as Int64
from Construct import Int64ul as UInt64
from Construct import Float32l as Float
from Construct import Float64l as Double
from Construct import PaddedString

OAmDatHeader = Struct(
    "identifier" / UInt16,
    "num_entries" / UInt32,
)

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

OAmDat = Struct(
    "header" / OAmDatHeader,
    "entries" / OAmDatEntry[this.header.num_entries],
)


WpDatHeader = Struct(
    "identifier" / UInt16,
    "num_entries" / UInt32,
)

WpDatEntry = Struct(
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

WpDat = Struct(
    "header" / WpDatHeader,
    "entries" / WpDatEntry[this.header.num_entries],
)

