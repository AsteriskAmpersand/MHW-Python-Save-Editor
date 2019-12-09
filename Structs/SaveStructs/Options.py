# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 00:41:11 2019

@author: AsteriskAmpersand
"""
from construct import Struct
from construct import this
from construct import Int8sl as Byte
from construct import Int8ul as UByte
from construct import Int16sl as Int16
from construct import Int16ul as UInt16
from construct import Int32sl as Int32
from construct import Int32ul as UInt32
from construct import Int64sl as Int64
from construct import Int64ul as UInt64
from construct import Float32l as Float
from construct import Float64l as Double
from construct import PaddedString

"""
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
"""
SectionData_1  = Struct(
 "unkn0" / Byte[8],
 "soundoutput" / UByte,#VSoundOutputDevice,
 "dynamicrange" / UByte,#VDynamicRange,
 "_3DAudio" / UByte,
 "voiceVolume" / Byte,
 "bgmVolume" / Byte,
 "soundEffectVolume" / Byte,
 "unkn1" / Byte[2],
 "textLanguage" / UByte,#VLanguage,
 "voiceLanguage" / UByte,#VLanguage,
 "Subtitles" / UByte,#VToggle,
 "voiceB" / UByte,#VoiceLanguageB,
 "voiceChat" / UByte,#Toggle,
 "subtitleTextSize" / UByte,#TextSize,
 "hudHelpTextSize" / UByte,#TextSize,
 "confirmationButton" / UByte,#ConfirmationButton,
 "unkn2" / Byte[16],
 "brightness" / Float,
 "unkn3" / Byte[12],
 "DLCOwned" / Int16[256],#VDLCType,
 "unkn4" / Byte[456],
)