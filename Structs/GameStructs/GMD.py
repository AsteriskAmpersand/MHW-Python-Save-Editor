# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 12:58:23 2019

@author: AsteriskAmpersand
"""
try:
    from MSE.Structs.constructBoilerplate import *
    from construct import IfThenElse
except:
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *
    from construct import IfThenElse

GmdHeader = Struct(
    "magic" / UInt32,
    "version" / UInt32,
    "lang_id" / UInt32,
    "unknown1" / UInt32,
    "unknown2" / UInt32,
    "key_count" / UInt32,
    "string_count" / UInt32,
    "key_block_size" / UInt32,
    "string_block_size" / UInt32,
    "name_size" / UInt32,
    "name" / PaddedString(this.name_size+1,"utf-8"),
)
GmdInfoEntry = Struct(
    "string_index" / UInt32,
    "hash_key_2x" / Int32,
    "hash_key_3x" / Int32,
    "pad" / UInt32,
    "key_offset" / UInt64,
    "bucket_index" / UInt64,
)
Gmd = Struct(
    "header" / GmdHeader,
    "info_entries" / GmdInfoEntry[this.header.key_count],
    "buckets" / IfThenElse(this.header.key_count > 0, UInt64[256], UInt64[0]),
    "key_block" / CString("utf8")[this.header.key_count],
    "string_block" / CString("utf8")[this.header.string_count],
)

class GmdFile():
    def __init__(self, path):
        with open(path,"rb") as gmd:
            self.gmdData = Gmd.parse(gmd.read())
    def keys(self):
        return self.gmdData.key_block
    def strings(self):
        return self.gmdData.string_block
    def __getitem__(self,val):
        return self.strings()[val]
    def __iter__(self):
        return iter(self.strings())