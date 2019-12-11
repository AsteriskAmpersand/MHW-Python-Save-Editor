# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 02:37:29 2019

@author: AsteriskAmpersand
"""
try:
    from ..constructBoilerplate import *
except:
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *
    
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