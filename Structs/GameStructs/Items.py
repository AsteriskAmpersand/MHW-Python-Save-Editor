# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:50:30 2019

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

# =============================================================================
# SkillGemParam
# =============================================================================

Skill = Struct(
    "SkillID" / UInt32,
    "SkillPoints" / Byte,
    "Padding" / Byte[3],
)

DecorationEntry = Struct(
    "ItemID" / UInt32,
    "DecoID" / UInt32 ,
    "DecoSize" / UInt32 ,
    "Skill1" / Skill,
    "Skill2" / Skill,
)

class SkillGemParam(DatFile):
    datEntry = DecorationEntry

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


class Itm(DatFile):
    datEntry = ItmEntry