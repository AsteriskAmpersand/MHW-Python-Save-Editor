# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 02:34:40 2019

@author: AsteriskAmpersand
"""
try:
    from ..constructBoilerplate import *
    from .PlayerAppearance import playerAppearance, palicoAppearance
except:
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *
    from PlayerAppearance import playerAppearance, palicoAppearance


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

 "captured" / UInt16[64],
 "slayed" / UInt16[64],
 "largest" / UInt16[64],
 "smallest" / UInt16[64],
 "researchLevel" / UByte[64],
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
 "partnerName" / UByte[32],
 "partnerSteamID" / UInt64,
 "partnerCreated" / Double,
 "date" / Double,
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
 "palicoName" / PaddedString(64,"utf8"),
 "palicoRank_Minus_1" / UInt32,
 "palicoHealth" / UInt32,
 "palicoAttM" / UInt32,
 "palicoAttR" / UInt32,
 "palicoAffinity" / UInt32,
 "palicoDef" / UInt32,
 "palicoVsFire" / Int32,
 "palicoVsWater" / Int32,
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
 "created" / Double,
 "unkn0" / UByte,
 "hunterRank" / UInt32,
 "playTime_s" / UInt32,
 "lastUpdated" / Double,
 "hunterName" / PaddedString(64,"utf8"),
 "primaryGroup" / PaddedString(54,"utf8"),
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
 "greeting" / PaddedString(256,"utf8"),
 "title" / PaddedString(256,"utf8"),
 "titleFirst" / UInt16,
 "titleMiddle" / UInt16,
 "titleLast" / UInt16,
 "positionX" / Float,
 "positionY" / Float,
 "zoom" / Float,
 "arenaRecords" / ArenaStats[10],
 "creaturestats" / CreatureStats,
)