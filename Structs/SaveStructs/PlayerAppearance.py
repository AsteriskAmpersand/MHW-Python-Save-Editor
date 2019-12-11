# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 01:02:24 2019

@author: AsteriskAmpersand
"""

try:
    from ..constructBoilerplate import *
except:
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *
    
#Character/Cat Appearance
playerAppearance  = Struct(

 "makeup2Color"  /  UInt32,
 "makeup2PosX"   /   Float,
 "makeup2PosY"   /   Float,
 "makeup2SizeX"   /   Float,
 "makeup2SizeY"   /   Float,
 "makeup2Glossy"   /   Float,
 "makeup2Metallic"   /   Float,
 "makeup2Type"  /  UInt32,
 "makeup1Color"  /  UInt32,
 "makeup1PosX"   /   Float,
 "makeup1PosY"   /   Float,
 "makeup1SizeX"   /   Float,
 "makeup1SizeY"   /   Float,
 "makeup1Gloss"   /   Float,
 "makeup1Metallic"   /   Float,
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
 "unused"   /   UByte[4],
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
 "furLength"   /   Float,
 "furThickness"   /   Float,
 "patternType"   /   UByte,
 "eyeType"   /   UByte,
 "earType"   /   UByte,
 "tailType"   /   UByte,
 "voiceType"  /  UInt16,
 "voicePitch"  /  UInt16,
)