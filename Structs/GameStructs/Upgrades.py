# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:39:02 2019

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

EqCusEntry = Struct(
    "equip_type" / UByte,
    "equip_id" / UInt16,
    "key_item_id" / UInt16,
    "unk1" / Int32,
    "unk2" / UInt32,
    "unk3" / UInt32,
    "item1_id" / UInt16,
    "item1_qty" / UByte,
    "item2_id" / UInt16,
    "item2_qty" / UByte,
    "item3_id" / UInt16,
    "item3_qty" / UByte,
    "item4_id" / UInt16,
    "item4_qty" / UByte,
    "descendant1_idx" / UInt16,
    "descendant2_idx" / UInt16,
    "descendant3_idx" / UInt16,
    "descendant4_idx" / UInt16,
    "unk4" / UByte,
    "group" / UByte,
    "unk5" / UInt16,
)

EqCusHeader = Struct(
    "identifier" / UInt16,
    "num_entries" / UInt32,
)

EqCus = Struct(
    "header" / EqCusHeader,
    "entries" / EqCusEntry[this.header.num_entries],
)


EqCrtEntry = Struct(
    "equip_type" / UByte,
    "equip_id" / UInt16,
    "key_item" / UInt16,
    "unknown1" / UInt32,
    "unknown2" / UInt32,
    "rank" / UInt32,
    "item1_id" / UInt16,
    "item1_qty" / UByte,
    "item2_id" / UInt16,
    "item2_qty" / UByte,
    "item3_id" / UInt16,
    "item3_qty" / UByte,
    "item4_id" / UInt16,
    "item4_qty" / UByte,
    "unknown3" / Byte,
    "unknown4" / Byte,
    "unknown5" / Byte,
    "unknown6" / Byte,
	)


EqCrtHeader = Struct(
    "identifier" / UInt16,
    "num_entries" / UInt32,
)

EqCrt = Struct(
    "header" / EqCrtHeader,
    "entries" / EqCrtEntry[this.header.num_entries],
)
