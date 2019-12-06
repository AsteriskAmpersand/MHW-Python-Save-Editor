# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 02:35:46 2019

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

ShortcutItem  = Struct(

 "categoryID" / UInt32,
 "entryID" / UInt32,
 "unkn" / UInt32,
)

Shortcuts  = Struct(

 "shortcutname" / PaddedString(32,"utf8"),
 "items" / ShortcutItem[8],
)

ItLoadout  = Struct(

 "loadoutName" / PaddedString(32,"utf8"),
 "unkn0" / Byte[584],
 "shortcuts" / Shortcuts[4],
)

ItemLoadout  = Struct(

 "iloadout" / ItLoadout[56],
 "itemLoadoutSort" / UByte[56],

)


Item  = Struct(

 "itemID" / UInt32,
 "itemQty" / UInt32,
)

ItemPouch  = Struct(

 "items" / Item[24],
 "ammo" / Item[16],
 "unkn" / Byte[256],
 "special" / Item[4],
)

ItemBox  = Struct(

 "items" / Item[200],
 "ammo" / Item[200],
 "materials" / Item[800],
 "decorations" / Item[200],
)