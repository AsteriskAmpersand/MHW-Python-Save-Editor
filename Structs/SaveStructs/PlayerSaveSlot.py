# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 00:39:24 2019

@author: AsteriskAmpersand
"""
try:
    from ..constructBoilerplate import *
except:
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *

try:
    from .PlayerAppearance import playerAppearance, palicoAppearance
    from .PlayerGuildcard import GuildCard
    from .PlayerItems import ItemLoadout, ItemPouch, ItemBox
    from .PlayerEquipment import EquipmentSlots, EquipLoadout 
    from .PlayerInvestigations import Investigation
except:
    from PlayerAppearance import playerAppearance, palicoAppearance
    from PlayerGuildcard import GuildCard
    from PlayerItems import ItemLoadout, ItemPouch, ItemBox
    from PlayerEquipment import EquipmentSlots, EquipLoadout 
    from PlayerInvestigations import Investigation


SaveSlot  = Struct(

 "hunterName"   /   UByte[64],
 "hunterRank"  /  UInt32,
 "zenni"  /  UInt32,
 "researchPoints"  /  UInt32,
 "hunterXP"  /  UInt32,
 "playTime_S"  /  UInt32,
 "unkn0"    /    Byte[4],
 "hunterAppearance" / playerAppearance,
 "palicoAppearance" / palicoAppearance,
 "hunterGC"    /    GuildCard,
 "sharedGC"    /    GuildCard[100],
 "unkn1" / Byte[106038],
 "itemLoadouts" / ItemLoadout,
 "unkn10" / Byte[8],
 "itempouch" / ItemPouch,
 "itembox" / ItemBox,
 "equipslots" / EquipmentSlots,
 "unkn2" / Byte[148636],
 "investigations" / Investigation[250],
 "unkn3" / Byte[4025],
 "equiploadout" / EquipLoadout[112],
 "unkn4" / Byte[25889],
 "DLCClaimed" / UInt16[256],
 "unkn5" / Byte[469],
 "slotactive" / UByte,
 "unkn6" / Byte[10375],
)