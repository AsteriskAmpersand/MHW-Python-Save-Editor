//------------------------------------------------
//--- 010 Editor v9.0.2 Binary Template
//
//      File: 
//   Authors: 
//   Version: 
//   Purpose: 
//  Category: 
// File Mask: 
//  ID Bytes: 
//   History: 
//------------------------------------------------
//Save Attempt, Based off the respective HSL

Header  = Struct( 
{
 "sig" / UInt32,
 "unkn0" / UInt32,
 "unkn1" / UInt32,
 "dataHash" / UByte[20],
 "dataSize" / UInt64,
 "steamID" / UInt64,
 "padding" / UByte[16],
)


Section  = Struct(
{
 "signature" / UInt32,
 "unkn0" / UInt32,
 "sectionSize" / UInt64,
 "sectionData" / Byte[sectionSize],
)

Data  = Struct(
{
 "sectionIndex" / UInt64[4],
 "section" / Section[4],
 "padding" / Byte[8],
)

Savefile  = Struct( 
{
 "head" / Header,
 "data" / Data,
)


//Character/Cat Appearance

H_Appearance  = Struct(
{
 "makeup2Color"  /  UInt32,
 "makeup2PosX"   /   float,
 "makeup2PosY"   /   float,
 "makeup2SizeX"   /   float,
 "makeup2SizeY"   /   float,
 "makeup2Glossy"   /   float,
 "makeup2Metallic"   /   float,
 "makeup2Type"  /  UInt32,
 "makeup1Color"  /  UInt32,
 "makeup1PosX"   /   float,
 "makeup1PosY"   /   float,
 "makeup1SizeX"   /   float,
 "makeup1SizeY"   /   float,
 "makeup1Gloss"   /   float,
 "makeup1Metallic"   /   float,
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

P_Appearance  = Struct(
{
 "patternColor1"  /  UInt32,
 "patternColor2"  /  UInt32,
 "patternColor3"  /  UInt32,
 "furColor"  /  UInt32,
 "leftEyeColor"  /  UInt32,
 "rightEyeColor"  /  UInt32,
 "clothingColor"  /  UInt32,
 "furLength"   /   float,
 "furThickness"   /   float,
 "patternType"   /   UByte,
 "eyeType"   /   UByte,
 "earType"   /   UByte,
 "tailType"   /   UByte,
 "voiceType"  /  UInt16,
 "voicePitch"  /  UInt16,
)


//Monster Records?


Creatures8  = Struct(
{
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
{
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
{
 "captured" / Creatures16,
 "slayed" / Creatures16,
 "largest" / Creatures16,
 "smallest" / Creatures16,
 "researchLevel" / Creatures8,
)

//Weapon Usage

WeaponUsage  = Struct(
{
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
{
 "lowRank" / WeaponUsage,
 "highRank" / WeaponUsage,
 "investigations" / WeaponUsage,
)
//Arena Stuff

ArenaRecord  = Struct(
{
 "unkn" / Byte[4],
 "partnerName" / uchar[32],
 "partnerSteamID" / UInt64,
 "partnerCreated" / time64_t,
 "date" / time64_t,
)

ArenaStats  = Struct(
{
 "unkn" / UInt16,
 "arenaRecord" / ArenaRecord[5],
)

//Guild Card Stuff
HunterEquipment  = Struct(
{
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
{
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
{
 "palicoName" / uchar[64],
 "palicoRank_Minus_1" / UInt32,
 "palicoHealth" / UInt32,
 "palicoAttM" / UInt32,
 "palicoAttR" / UInt32,
 "palicoAffinity" / UInt32,
 "palicoDef" / UInt32,
 "palicoVsFire" / Int32sl,
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
{
 "steamID" / UInt64,
 "created" / time64_t,
 "unkn0" / UByte,
 "hunterRank" / UInt32,
 "playTime_s" / UInt32,
 "lastUpdated" / time64_t,
 "hunterName" / uchar[64],
 "primaryGroup" / uchar[54],
 "unkn1" / Byte[16],
 "hunterAppearance" / H_Appearance,
 "palicoAppearance" / P_Appearance,
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
 "positionX" / float,
 "positionY" / float,
 "zoom" / float,
 "arenaRecords" / ArenaStats[10],
 "creaturestats" / CreatureStats,

)

//Equipment Enums
typedef enum <uint32>
{
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
 
Equipment  = Struct(
{
 "SortIndex" / UInt32,
 "equipt" / EquipmentType,
 switch(equipt)
 {
  case 0: ArmorSlot armorslot; break;
  case 1: WeaponType weapt; break;
  case 2: UInt32 CharmPresence; break;
  case 3: break;
  case 4: UInt32 KinsectPresence; break;
  default: UInt32 None; break;
 }
 "IdInClass" / Int32,
 "UpgradeLevel" / Int32,
 "UpgradePoints" / Int32,
 "DecoSlot1" / Deco,
 "DecoSlot2" / Deco,
 "DecoSlot3" / Deco,
 switch(equipt)
 {
  case 1: BowGunMod bowgunmod1; break;
  case 4: KinsectType kint; break;
  default: BowGunMod bowgunmod1; break;
 }
 "bowgunmod2" / BowGunMod,
 "bowgunmod3" / BowGunMod,
 "augment1" / Augment,
 "augment2" / Augment,
 "augment3" / Augment,
 "unkn0" / Int32,
 "unkn1" / Int32,
)

typedef enum <int16>
{
    None                                      = 0,
    Origin_Armor_Set                          = 1,
    Fair_Wind_Charm                           = 2,
    Samurai_Set                               = 3,
    The_Handlers_Guildmarm_Costume            = 4,
    The_Handlers_Astera_3_Star_Chef_Coat      = 5,
    The_Handlers_Busy_Bee_Dress               = 7,
    The_Handlers_Sunshine_Pareo               = 8,
    Beginner_Commendation_Pack                = 12,
    Intermediate_Commendation_Pack            = 13,
    Expert_Commendation_Pack                  = 14,
    Champion_Commendation_Pack                = 15,
    Character_Edit_Voucher                    = 20,
    Face_Paint_Camouflage                     = 21,
    Face_Paint_Wyvern                         = 22,
    Face_Paint_Shade_Pattern                  = 23,
    Face_Paint_Heart_Shape                    = 24,
    Face_Paint_Eye_Shadow                     = 25,
    Hairstyle_Topknot                         = 26,
    Hairstyle_Provisions_Manager              = 27,
    Hairstyle_Field_Team_Leader               = 28,
    Hairstyle_The_Handler                     = 29,
    Hairstyle_The_Admiral                     = 30,
    Gesture_Zen                               = 31,
    Gesture_Ninja_Star                        = 32,
    Gesture_Sumo_Slap                         = 33,
    Gesture_Passionate                        = 34,
    Gesture_SpinORama                         = 35,
    Gesture_Air_Splits                        = 36,
    Gesture_Feverish_Dance                    = 37,
    Gesture_Gallivanting_Dance                = 38,
    Gesture_Interpretive_Dance                = 39,
    Gesture_Play_Possum                       = 40,
    Gesture_Kowtow                            = 41,
    Gesture_Sleep                             = 42,
    Gesture_Kneel                             = 43,
    Classic_Gesture_Dance                     = 44,
    Classic_Gesture_Prance                    = 45,
    Classic_Gesture_Rant                      = 46,
    Classic_Gesture_Clap                      = 47,
    Gesture_Devil_May_Cry_Dual_Guns           = 50,
    Gesture_Spirit_Fingers                    = 52,
    Gesture_Windmill_Whirlwind                = 53,
    Gesture_Disco_Fever                       = 54,
    Gesture_Squat_Day                         = 55,
    Sticker_Set_MH_All_Stars_Set              = 56,
    Sticker_Set_Sir_Loin_Set                  = 57,
    Sticker_Set_Poogie_Set                    = 58,
    Sticker_Set_Guild_Lasses_Set              = 59,
    Sticker_Set_Endemic_Life_Set              = 60,
    Sticker_Set_Classic_Monsters_Set          = 61,
    Sticker_Set_Research_Commission_Set       = 62,
    Sticker_Set_Mega_Man_Set                  = 63,
    Sticker_Set_Devil_May_Cry_Set             = 65,
    Character_Edit_Voucher_Single_Voucher     = 99,
    Character_Edit_Voucher_Two_Voucher_Pack   = 100,
    Character_Edit_Voucher_Three_Voucher_Pack = 101,
    DLC_None                                      = -1
}DLCType;
//Section Enums/Structs
typedef enum <ubyte>
{
 TV_Display   = 0,
 Home_Theatre = 1,
 Headphones   = 2

}SoundOutputDevice;
 
typedef enum <ubyte>
{
 Wide_Range   = 0,
 Mid_Range    = 1,
 Narrow_Range = 2

}DynamicRange;

typedef enum <ubyte>
{
 On  = 0,
 Off = 1

}Toggle;

typedef enum <ubyte>
{
 Japanese            = 0,
 English             = 1,
 French              = 2,
 Spanish             = 3,
 German              = 4,
 Italian             = 5,
 Korean              = 6,
 Traditional_Chinese = 7,
 Russian             = 10,
 Polish              = 11,
 Portuguese_Brazil   = 21,
 Arabic              = 22

}Language;

typedef enum <ubyte>
{
 Normal        = 0,
 MonsterHunter = 1
}VoiceLanguageB;

typedef enum <ubyte>
{
 Default = 0,
 Large   = 1

}TextSize;

typedef enum <ubyte>
{
 A = 0,
 B = 1
}ConfirmationButton;

ShortcutItem  = Struct(
{
 "categoryID" / UInt32,
 "entryID" / UInt32,
 "unkn" / UInt32,
)

Shortcuts  = Struct(
{
 "shortcutname" / uchar[32],
 "items" / ShortcutItem[8],
)

ItLoadout  = Struct(
{
 "loadoutName" / uchar[32],
 "unkn0" / Byte[584],
 "shortcuts" / Shortcuts[4],
)

ItemLoadout  = Struct(
{
 "iloadout" / ItLoadout[56],
 "itemLoadoutSort" / UByte[56],

)


Item  = Struct(
{
 "itemID" / UInt32,
 "itemQty" / UInt32,
)

string ReadItem(Item& e)
{
 string s;
 SPrintf(s, "ID=%d Qty=%d",e.itemID, e.itemQty); 
 return s;

}

ItemPouch  = Struct(
{
 "items" / Item[24],
 "ammo" / Item[16],
 "unkn" / Byte[256],
 "special" / Item[4],
)

ItemBox  = Struct(
{
 "items" / Item[200],
 "ammo" / Item[200],
 "materials" / Item[800],
 "decorations" / Item[200],
)

Investigation  = Struct(
{
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

EquipLoadout  = Struct(
{
 "slotID" / Int32,
 "loadoutName"  /  uchar[256],
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
{
 "equipmentSlot" / Equipment[1000],
)

typedef enum <ubyte>
{
 False = 0,
 True  = 1

}IsSlotActive;


SaveSlot  = Struct(
{
 "hunterName"   /   uchar[64],
 "hunterRank"  /  UInt32,
 "zenni"  /  UInt32,
 "researchPoints"  /  UInt32,
 "hunterXP"  /  UInt32,
 "playTime_S"  /  UInt32,
 "unkn0"    /    Byte[4],
 "hunterAppearance" / H_Appearance,
 "palicoAppearance" / P_Appearance,
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
 "slotactive" / IsSlotActive,
 "unkn6" / Byte[10375],
)
//Section Data

SectionData_0  = Struct(
{
 "unkn" / Byte[0x300000],

)


SectionData_1  = Struct(
{
 "unkn0" / Byte[8],
 "soundoutput" / SoundOutputDevice,
 "dynamicrange" / DynamicRange,
 "_3DAudio" / Toggle,
 "voiceVolume" / Byte,
 "bgmVolume" / Byte,
 "soundEffectVolume" / Byte,
 "unkn1" / Byte[2],
 "textLanguage" / Language,
 "voiceLanguage" / Language,
 "Subtitles" / Toggle,
 "voiceB" / VoiceLanguageB,
 "voiceChat" / Toggle,
 "subtitleTextSize" / TextSize,
 "hudHelpTextSize" / TextSize,
 "confirmationButton" / ConfirmationButton,
 "unkn2" / Byte[16],
 "brightness" / float,
 "unkn3" / Byte[12],
 "DLCOwned" / DLCType[256],
 "unkn4" / Byte[456],

)

SectionData_2  = Struct(
{ 
 "unkn" / Byte[56],

)

SectionData_3  = Struct(
{
 "unkn" / UInt32,
 "saveslot" / SaveSlot[3],
 "empty" / Byte[3267788],
)

Savefile save<bgcolor=0x00FF00>;
FSeek(save.data.sectionIndex[0]+16);
SectionData_0 controls <bgcolor=0x00CC00>;

FSeek(save.data.sectionIndex[1]+16);
SectionData_1 options <bgcolor=0x00CC00>;

FSeek(save.data.sectionIndex[2]+16);
SectionData_2  unknown <bgcolor=0x00CC00>;

FSeek(save.data.sectionIndex[3]+16);
SectionData_3 saveslots <bgcolor=0x00CC00>;
