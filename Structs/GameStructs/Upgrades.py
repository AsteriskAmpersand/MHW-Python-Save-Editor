# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 17:39:02 2019

@author: AsteriskAmpersand
"""


try:
    from MSE.Structs.GameStructs.DatHeader import DatFile
    from MSE.Structs.constructBoilerplate import *
except:
    print(1)
    from DatHeader import DatFile
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *

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

class EqCus(DatFile):
    datEntry = EqCusEntry


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


class EqCrt(DatFile):
    datEntry = EqCrtEntry
