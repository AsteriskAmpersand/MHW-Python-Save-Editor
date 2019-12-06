# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 02:35:12 2019

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
"""
//Equipment Enums
typedef enum <uint32>

  Antidote_Jewel_1         =0,
  Antipara_Jewel_1         =1,
  Pep_Jewel_1              =2,
  Steadfast_Jewel_1        =3,
  Antiblast_Jewel_1        =4,
  Suture_Jewel_1           =5,
  Def_Lock_Jewel_1         =6,
  Earplug_Jewel_3          =7,
  Wind_Resist_Jewel_2      =8,
  Footing_Jewel_2          =9,
  Attack_Jewel_1           =10,
  Defense_Jewel_1          =11,
  Vitality_Jewel_1         =12,
  Recovery_Jewel_1         =13,
  Fire_Res_Jewel_1         =14,
  Water_Res_Jewel_1        =15,
  Ice_Res_Jewel_1          =16,
  Thunder_Res_Jewel_1      =17,
  Dragon_Res_Jewel_1       =18,
  Resistor_Jewel_1         =19,
  Blaze_Jewel_1            =20,
  Stream_Jewel_1           =21,
  Frost_Jewel_1            =22,
  Bolt_Jewel_1             =23,
  Dragon_Jewel_1           =24,
  Venom_Jewel_1            =25,
  Paralyzer_Jewel_1        =26,
  Sleep_Jewel_1            =27,
  Blast_Jewel_1            =28,
  Poisoncoat_Jewel_3       =29,
  Paracoat_Jewel_3         =30,
  Sleepcoat_Jewel_3        =31,
  Blastcoat_Jewel_3        =32,
  Release_Jewel_3          =33,
  Expert_Jewel_1           =34,
  Critical_Jewel_2         =35,
  Tenderizer_Jewel_2       =36,
  Charger_Jewel_2          =37,
  Handicraft_Jewel_3       =38,
  Draw_Jewel_2             =39,
  Destroyer_Jewel_2        =40,
  KO_Jewel_2               =41,
  Drain_Jewel_1            =42,
  Flight_Jewel_2           =43,
  Throttle_Jewel_2         =44,
  Challenger_Jewel_2       =45,
  Flawless_Jewel_2         =46,
  Potential_Jewel_2        =47,
  Fortitude_Jewel_1        =48,
  Furor_Jewel_2            =49,
  Sonorous_Jewel_1         =50,
  Magazine_Jewel_2         =51,
  Trueshot_Jewel_1         =52,
  Artillery_Jewel_1        =53,
  Heavy_Artillery_Jewel_1  =54,
  Sprinter_Jewel_2         =55,
  Physique_Jewel_2         =56,
  Refresh_Jewel_2          =57,
  Hungerless_Jewel_1       =58,
  Evasion_Jewel_2          =59,
  Jumping_Jewel_2          =60,
  Ironwall_Jewel_1         =61,
  Sheath_Jewel_1           =62,
  Friendship_Jewel_1       =63,
  Enduring_Jewel_1         =64,
  Satiated_Jewel_1         =65,
  Gobbler_Jewel_1          =66,
  Grinder_Jewel_1          =67,
  Bomber_Jewel_1           =68,
  Fungiform_Jewel_1        =69,
  Protection_Jewel_1       =70,
  Meowster_Jewel_1         =71,
  Botany_Jewel_1           =72,
  Geology_Jewel_1          =73,
  Mighty_Jewel_2           =74,
  Stonethrower_Jewel_1     =75,
  Tip_Toe_Jewel_1          =76,
  Brace_Jewel_3            =77,
  Smoke_Jewel_1            =78,
  Mirewalker_Jewel_1       =79,
  Specimen_Jewel_1         =80,
  Miasma_Jewel_1           =81,
  Scent_Jewel_1            =82,
  Intimidator_Jewel_1      =83,
  Slider_Jewel_2           =84,
  Medicine_Jewel_1         =85,
  Forceshot_Jewel_3        =86,
  Pierce_Jewel_3           =87,
  Spread_Jewel_3           =88,
  Enhancer_Jewel_2         =89,
  Crisis_Jewel_1           =90,
  Dragonseal_Jewel_3       =91,
  Maintenance_Jewel_1      =92,
  Mighty_Bow_Jewel_2       =93,
  Minds_Eye_Jewel_2        =94,
  Shield_Jewel_2           =95,
  Sharp_Jewel_2            =96,
  Elementless_Jewel_2      =97,
  No_Deco                  =-1
}Deco;

typedef enum <uint32>
{
 Armor   =0,
 Weapon  =1,
 Charm   =2,
 Kinsect =4

}EquipmentType;

typedef enum <uint32>
{
 Head  =0,
 Torso =1,
 Arms  =2,
 Coil  =3,
 Legs  =4

}ArmorSlot;

typedef enum <uint32>
{
 GreatSword     =0,
 SwordAndShield =1,
 DualSword      =2,
 Longsword      =3,  
 Hammer         =4,
 HuntingHorn    =5,
 Lance          =6,
 Gunlance       =7,
 SwitchAxe      =8,
 Chargeblade    =9,
 InsectGlaive   =10,
 Bow            =11,
 HeavyBowgun    =12,
 LightBowgun    =13
}WeaponType;

typedef enum <uint32>
{
 No_Mod             =-1,
 RecoilSupressor    =0,
 ReloadAssist       =1,
 DeviationSupressor =2,
 CloseRangeUp       =3,
 RangedAttUp        =4,
 Shield             =5
}BowGunMod;

typedef enum <int32>
{
 Kin_None    =-1,
 Kin_NoEle   =0,
 Kin_Fire    =1,
 Kin_Water   =2,
 Kin_Ice     =3,
 Kin_Thunder =4,
 Kin_Dragon  =5

}KinsectType;


typedef enum <int32>
{
 Aug_None         =-1,
 Aug_Empty        =0,
 Aug_Attack       =1,
 Aug_Affinity     =2,
 Aug_Defense      =3,
 Aug_SlotUpgrade  =4,
 Aug_HealthRegen  =5,
 ArmorIsAugmented =6

}Augment;
//Equipment

 switch(equipt)
 {
  case 0: ArmorSlot armorslot; break;
  case 1: WeaponType weapt; break;
  case 2: UInt32 CharmPresence; break;
  case 3: break;
  case 4: UInt32 KinsectPresence; break;
  default: UInt32 None; break;
 }EquipmentSlot
 
  switch(equipt)
 {
  case 1: BowGunMod bowgunmod1; break;
  case 4: KinsectType kint; break;
  default: BowGunMod bowgunmod1; break;
 }GunModKin
 """
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