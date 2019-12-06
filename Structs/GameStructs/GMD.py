# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:58:23 2019

@author: aguevara
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

GmdHeader = Struct(
    "magic" / uint32,
    "version" / uint32,
    "lang_id" / uint32,
    "unknown1" / uint32,
    "unknown2" / uint32,
    "key_count" / uint32,
    "string_count" / uint32,
    "key_block_size" / uint32,
    "string_block_size" / uint32,
    "name_size" / uint32,
    "name" / char[this.name_size+1],
)
GmdInfoEntry = Struct(
    "string_index" / uint32,
    "hash_key_2x" / int32,
    "hash_key_3x" / int32,
    "pad" / uint32,
    "key_offset" / uint64,
    "bucket_index" / uint64,
)
Gmd = Struct(
    "header" / GmdHeader,
    "info_entries" / GmdInfoEntry[this.header.key_count],
    "buckets" / uint64[256],
    "key_block" / char[this.header.key_block_size],
    "string_block" / char[this.header.string_block_size],
)

