# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 02:34:40 2019

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


Creatures8  = Struct(

 "Great_Jagras" / UByte,
 "Kulu_Ya_Ku" / UByte,
 "Pukei_Pukei" / UByte,
 "Barroth" / UByte,
 "Jyuratodus" / UByte,
 "Tobi_Kadachi" / UByte,
 "Anjanath" / UByte,
 "Rathian" / UByte,
 "Tzitzi_Ya_Ku" / UByte,
 "Paolumu" / UByte,
 "Great_Girros" / UByte,
 "Radobaan" / UByte,
 "Legiana" / UByte,
 "Odogaron" / UByte,
 "Rathalos" / UByte,
 "Diablos" / UByte,
 "Kirin" / UByte,
 "Zorah_Magdaros" / UByte,
 "Dodogama" / UByte,
 "Pink_Rathian" / UByte,
 "Bazelgeuse" / UByte,
 "Lavasioth" / UByte,
 "Uragaan" / UByte,
 "Azure_Rathalos" / UByte,
 "Black_Diablos" / UByte,
 "Nergigante" / UByte,
 "Teostra" / UByte,
 "Kushala_Daora" / UByte,
 "Vaal_Hazak" / UByte,
 "Xenojiiva" / UByte,
 "Deviljho" / UByte,
 "Kulve_Taroth" / UByte,
 "Lunastra" / UByte,
 "Behemoth" / UByte,
 "Leshen" / UByte,
 "Ancient_Leshen" / UByte,
 "Unused" / UByte[28],
)

Creatures16  = Struct(

 "Great_Jagras" / UInt16,
 "Kulu_Ya_Ku" / UInt16,
 "Pukei_Pukei" / UInt16,
 "Barroth" / UInt16,
 "Jyuratodus" / UInt16,
 "Tobi_Kadachi" / UInt16,
 "Anjanath" / UInt16,
 "Rathian" / UInt16,
 "Tzitzi_Ya_Ku" / UInt16,
 "Paolumu" / UInt16,
 "Great_Girros" / UInt16,
 "Radobaan" / UInt16,
 "Legiana" / UInt16,
 "Odogaron" / UInt16,
 "Rathalos" / UInt16,
 "Diablos" / UInt16,
 "Kirin" / UInt16,
 "Zorah_Magdaros" / UInt16,
 "Dodogama" / UInt16,
 "Pink_Rathian" / UInt16,
 "Bazelgeuse" / UInt16,
 "Lavasioth" / UInt16,
 "Uragaan" / UInt16,
 "Azure_Rathalos" / UInt16,
 "Black_Diablos" / UInt16,
 "Nergigante" / UInt16,
 "Teostra" / UInt16,
 "Kushala_Daora" / UInt16,
 "Vaal_Hazak" / UInt16,
 "Xenojiiva" / UInt16,
 "Deviljho" / UInt16,
 "Kulve_Taroth" / UInt16,
 "Lunastra" / UInt16,
 "Behemoth" / UInt16,
 "Leshen" / UInt16,
 "Ancient_Leshen" / UInt16,
 "Unused" / UInt16[28],
)

CreatureStats  = Struct(

 "captured" / Creatures16,
 "slayed" / Creatures16,
 "largest" / Creatures16,
 "smallest" / Creatures16,
 "researchLevel" / Creatures8,
)

#Weapon Usage

WeaponUsage  = Struct(

 "GS" / UInt16,
 "LS" / UInt16,
 "SnS" / UInt16,
 "DB" / UInt16,
 "Hammer" / UInt16,
 "HH" / UInt16,
 "Lance" / UInt16,
 "GL" / UInt16,
 "SA" / UInt16,
 "CB" / UInt16,
 "IG" / UInt16,
 "LBG" / UInt16,
 "HBG" / UInt16,
 "Bow" / UInt16,
)

WeaponUsages  = Struct(

 "lowRank" / WeaponUsage,
 "highRank" / WeaponUsage,
 "investigations" / WeaponUsage,
)
#Arena Stuff

ArenaRecord  = Struct(

 "unkn" / Byte[4],
 "partnerName" / uchar[32],
 "partnerSteamID" / UInt64,
 "partnerCreated" / time64_t,
 "date" / time64_t,
)

ArenaStats  = Struct(

 "unkn" / UInt16,
 "arenaRecord" / ArenaRecord[5],
)

#Guild Card Stuff
HunterEquipment  = Struct(

 "weaponType" / UInt32,
 "weaponID" / UInt32,
 "headArmorType" / UInt32,
 "headArmorID" / UInt32,
 "chestArmorType" / UInt32,
 "chestArmorID" / UInt32,
 "armArmorType" / UInt32,
 "armArmorID" / UInt32,
 "waistArmorType" / UInt32,
 "waistArmorID" / UInt32,
 "legArmorType" / UInt32,
 "legArmorID" / UInt32,
 "charmType" / UInt32,
 "charmID" / UInt32,
 "tool1Type" / UInt32,
 "tool1ID" / UInt32,
 "tool2Type" / UInt32,
 "tool2ID" / UInt32,
)


PalicoEquipment  = Struct(

 "palicoWeaponType" / UInt32,
 "palicoWeaponID" / UInt32,
 "palicoHeadArmorType" / UInt32,
 "palicoHeadArmorID" / UInt32,
 "palicoBodyArmorType" / UInt32,
 "palicoBodyArmorID" / UInt32,
 "palicoGadgetType" / UInt32,
 "palicoGadgetID" / UInt32,
)

Palico  = Struct(

 "palicoName" / uchar[64],
 "palicoRank_Minus_1" / UInt32,
 "palicoHealth" / UInt32,
 "palicoAttM" / UInt32,
 "palicoAttR" / UInt32,
 "palicoAffinity" / UInt32,
 "palicoDef" / UInt32,
 "palicoVsFire" / Int32,
 "palicoVsWater" / Int32sl,
 "palicoVsThunder" / Int32,
 "palicoVsIce" / Int32,
 "palicoVsDragon" / Int32,
 "unknown0" / UByte,
 "palicoEquipment" / PalicoEquipment,
 "unknown1" / Byte[4],
 "palicoG1" / UByte,
 "palicoG2" / UByte,
 "palicoG3" / UByte,
 "palicoG4" / UByte,
 "palicoG5" / UByte,
 "palicoG6" / UByte,
)



GuildCard  = Struct(
        
 "steamID" / UInt64,
 "created" / time64_t,
 "unkn0" / UByte,
 "hunterRank" / UInt32,
 "playTime_s" / UInt32,
 "lastUpdated" / time64_t,
 "hunterName" / uchar[64],
 "primaryGroup" / uchar[54],
 "unkn1" / Byte[16],
 "hunterAppearance" / playerAppearance,
 "palicoAppearance" / palicoAppearance,
 "hunterEquipment" / HunterEquipment,
 "unkn2" / Byte[92],
 "palico" / Palico,
 "unity" / Int32,
 "unkn3" / Byte[16],
 "questsLR" / UInt16,
 "questsHR" / UInt16,
 "questsInvest" / UInt16,
 "questsArena" / UInt16,
 "tailRaiderUnity" / UInt32[5],
 "unkn" / Byte[15],
 "weaponusage" / WeaponUsages,
 "poseID" / UByte,
 "expressionID" / UByte,
 "backgroundID" / UByte,
 "stickerID" / UByte,
 "greeting" / uchar[256],
 "title" / uchar[256],
 "titleFirst" / UInt16,
 "titleMiddle" / UInt16,
 "titleLast" / UInt16,
 "positionX" / float32l,
 "positionY" / float32l,
 "zoom" / float32l,
 "arenaRecords" / ArenaStats[10],
 "creaturestats" / CreatureStats,
)