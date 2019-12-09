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
Header  = Struct( 

 "sig" / UInt32,
 "unkn0" / UInt32,
 "unkn1" / UInt32,
 "dataHash" / UByte[20],
 "dataSize" / UInt64,
 "steamID" / UInt64,
 "padding" / UByte[16],
)


Section  = Struct(

 "signature" / UInt32,
 "unkn0" / UInt32,
 "sectionSize" / UInt64,
 "sectionData" / Byte[this.sectionSize],
)

Data  = Struct(

 "sectionIndex" / UInt64[4],
 "section" / Section[4],
 "padding" / Byte[8],
)

Savefile  = Struct( 

 "head" / Header,
 "data" / Data,
)

SectionData_0  = Struct(

 "unkn" / Byte[0x300000],

)

SectionData_2  = Struct(
 
 "unkn" / Byte[56],

)

SectionData_3  = Struct(

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
