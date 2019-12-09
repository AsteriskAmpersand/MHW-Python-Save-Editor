# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 02:35:12 2019

@author: AsteriskAmpersand
"""
try:
    from ..constructBoilerplate import *
except:
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *

Equipment  = Struct(
 "SortIndex" / UInt32,
 "equipt" / UInt32,#EquipmentType,
 "equips" / UInt32,#EquipmentSlot,
 "IdInClass" / Int32,
 "UpgradeLevel" / Int32,
 "UpgradePoints" / Int32,
 "DecoSlot1" / UInt32,#Deco,
 "DecoSlot2" / UInt32,#Deco,
 "DecoSlot3" / UInt32,#Deco,
 "bowgunmod1" / UInt32,#GunModKin,
 "bowgunmod2" / UInt32,#BowGunMod,
 "bowgunmod3" / UInt32,#BowGunMod,
 "augment1" / UInt32,#Augment,
 "augment2" / UInt32,#Augment,
 "augment3" / UInt32,#Augment,
 "unkn0" / Int32,
 "unkn1" / Int32,
)


EquipLoadout  = Struct(

 "slotID" / Int32,
 "loadoutName"  /  PaddedString(256,"utf8"),
 "WeaponIndex" / Int32,
 "HelmetIndex" / Int32,
 "TorsoIndex" / Int32,
 "ArmsIndex" / Int32,
 "CoilIndex" / Int32,
 "FeetIndex" / Int32,
 "CharmIndex" / Int32,
 "Mantle1Index" / Int32,
 "Mantel2Index" / Int32,
 "WeaponDecosId1" / Int32,
 "WeaponDecosId2" / Int32,
 "WeaponDecosId3" / Int32,
 "HelmetDecosId1" / Int32,
 "HelmetDecosId2" / Int32,
 "HelmetDecosId3" / Int32,
 "TorsoDecosId1" / Int32,
 "TorsoDecosId2" / Int32,
 "TorsoDecosId3" / Int32,
 "ArmsDecosId1" / Int32,
 "ArmsDecosId2" / Int32,
 "ArmsDecosId3" / Int32,
 "CoilDecosId1" / Int32,
 "CoilDecosId2" / Int32,
 "CoilDecosId3" / Int32,
 "FeetDecosId1" / Int32,
 "FeetDecosId2" / Int32,
 "FeetDecosId3" / Int32,
 "Unknown" / Int32[27],
 "CharmDecosIndex1" / Int32,
 "CharmDecosIndex2" / Int32,
 "CharmDecosIndex3" / Int32,
 "Mantle1DecosIndex1" / Int32,
 "Mantle1DecosIndex2" / Int32,
 "Mantle1DecosIndex3" / Int32,
 "Mantle2DecosIndex1" / Int32,
 "Mantle2DecosIndex2" / Int32,
 "Mantle2DecosIndex3" / Int32,
 "BitMaskForCustomColours" / Int32,
 "BitMaskForRainbow" / Int32,
 "RGBHead" / Int32,
 "RGBTorso" / Int32,
 "RGBArms" / Int32,
 "RGBCoil" / Int32,
 "RGBWholeSet" / Int32,
 "unkn0" / Int32,
)

EquipmentSlots  = Struct(

 "equipmentSlot" / Equipment[1000],
)