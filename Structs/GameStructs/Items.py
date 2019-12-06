# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:50:30 2019

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

# =============================================================================
# SkillGemParam
# =============================================================================

Skill = Struct(
    "SkillID" / UInt32,
    "SkillPoints" / Byte,
    "Padding" / Byte[3],
)

Decoration = Struct(
    "ItemID" / UInt32,
    "DecoID" / UInt32 ,
    "DecoSize" / UInt32 ,
    "Skill1" / Skill,
    "Skill2" / Skill,
)

SkillGemParam = Struct(
    "Header" / UInt16 ,
    "Size" / UInt32 ,
    "Decorations" / Decoration[this.Size]
)

# =============================================================================
# Itm
# =============================================================================

ItmEntry = Struct(
    "id" / UInt32,
    "sub_type" / UByte,
    "type" / UInt32,
    "rarity" / UByte,
    "carry_limit" / UByte,
    "unk_limit" / UByte,
    "sort_order" / UInt16,
    "flags" / UInt32,
    "icon_id" / UInt32,
    "icon_color" / UInt16,
    "sell_price" / UInt32,
    "buy_price" / UInt32,
)

ItmHeader = Struct(
    "identifier" / UInt16,
    "num_entries" / UInt32,
)

Itm = Struct(
    "header" / ItmHeader,
    "entries" / ItmEntry[this.header.num_entries],
)
