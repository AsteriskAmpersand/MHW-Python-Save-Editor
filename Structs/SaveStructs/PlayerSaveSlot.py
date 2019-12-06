# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 00:39:24 2019

@author: AsteriskAmpersand
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


#Character/Cat Appearance
playerAppearance  = Struct(

 "makeup2Color"  /  UInt32,
 "makeup2PosX"   /   float32l,
 "makeup2PosY"   /   float32l,
 "makeup2SizeX"   /   float32l,
 "makeup2SizeY"   /   float32l,
 "makeup2Glossy"   /   float32l,
 "makeup2Metallic"   /   float32l,
 "makeup2Type"  /  UInt32,
 "makeup1Color"  /  UInt32,
 "makeup1PosX"   /   float32l,
 "makeup1PosY"   /   float32l,
 "makeup1SizeX"   /   float32l,
 "makeup1SizeY"   /   float32l,
 "makeup1Gloss"   /   float32l,
 "makeup1Metallic"   /   float32l,
 "makeup1Type"  /  UInt32,
 "leftEyeColor"  /  UInt32,
 "rightEyeColor"  /  UInt32,
 "eyebrowColor"  /  UInt32,
 "facialHairColor"  /  UInt32,
 "eyeWidth"    /    Byte,
 "eyeHeight"    /    Byte,
 "skinColorX"   /   UByte,
 "skinColorY"   /   UByte,
 "age"   /   UByte,
 "wrinkles"   /   UByte,
 "noseHeight"    /    Byte,
 "mouthHeight"    /    Byte,
 "gender"  /  UInt32,
 "browType"   /   UByte,
 "faceType"   /   UByte,
 "eyeType"   /   UByte,
 "noseType"   /   UByte,
 "mouthType"   /   UByte,
 "eyebrowType"   /   UByte,
 "eyelashLength"   /   UByte,
 "facialHairtype"   /   UByte,
 "unused"   /   uchar[4],
 "hairColor"  /  UInt32,
 "clothingColor"  /  UInt32,
 "hairType"  /  UInt16,
 "clothingType"   /   UByte,
 "voice"   /   UByte,
 "expression"  /  UInt32,
)

palicoAppearance  = Struct(

 "patternColor1"  /  UInt32,
 "patternColor2"  /  UInt32,
 "patternColor3"  /  UInt32,
 "furColor"  /  UInt32,
 "leftEyeColor"  /  UInt32,
 "rightEyeColor"  /  UInt32,
 "clothingColor"  /  UInt32,
 "furLength"   /   float32l,
 "furThickness"   /   float32l,
 "patternType"   /   UByte,
 "eyeType"   /   UByte,
 "earType"   /   UByte,
 "tailType"   /   UByte,
 "voiceType"  /  UInt16,
 "voicePitch"  /  UInt16,
)



Investigation  = Struct(

 "filled" / UInt32,
 "selected"  /  UByte,
 "attempts" / UInt32,
 "seen" / UInt32,
 "locale"  /  UByte,
 "rank"  /  UByte,
 "mon1" / UInt32,
 "mon2" / UInt32,
 "mon3" / UInt32,
 "mon1temper"  /  UByte,
 "mon2temper"  /  UByte,
 "mon3temper"  /  UByte,
 "hp"  /  UByte,
 "attack"  /  UByte,
 "defense"  /  UByte,
 "x3"  /  UByte,
 "y0"  /  UByte,
 "flourish"  /  UByte,
 "timeamount"  /  UByte,
 "y3"  /  UByte,
 "faints"  /  UByte,
 "playercount"  /  UByte,
 "rewards"  /  UByte,
 "zenny"  /  UByte,
)

SaveSlot  = Struct(

 "hunterName"   /   uchar[64],
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
 "DLCClaimed" / DLCType[256],
 "unkn5" / Byte[469],
 "slotactive" / UByte,
 "unkn6" / Byte[10375],
)