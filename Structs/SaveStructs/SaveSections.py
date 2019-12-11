try:
    from ..constructBoilerplate import *
except:
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *

try:
    from .Options import Options
    from .PlayerSaveSlot import SaveSlot
except:
    import sys
    sys.path.insert(1, '.')
    from Options import Options
    from PlayerSaveSlot import SaveSlot

Header  = Struct( 
 "sig" / UInt32,
 "unkn0" / UInt32,
 "unkn1" / UInt32,
 "dataHash" / UByte[20],
 "dataSize" / UInt64,
 "steamID" / UInt64,
 "padding" / UByte[16],
)


SectionHeader  = Struct(

 "signature" / UInt32,
 "unkn0" / UInt32,
 "sectionSize" / UInt64,
 #"sectionData" / Byte[this.sectionSize],
)

Controls  = Struct(
 "head" / SectionHeader,
 "unkn" / Byte[0x300000],

)

Unknown  = Struct(
 "head" / SectionHeader,
 "unkn" / Byte[56],

)

SaveFiles  = Struct(
 "head" / SectionHeader,
 "unkn" / UInt32,
 "saveslots" / SaveSlot[3],
 "empty" / Byte[3267788],
)

Data  = Struct(

 "sectionIndex" / UInt64[4],
 "controls" / Controls,
 "options" / Options,#SectionData_1
 "unknown" / Unknown,
 "savefiles" / SaveFiles,
 "padding" / Byte[8],
)

SaveStructure = Struct(
 "head" / Header,
 "data" / Data,
)