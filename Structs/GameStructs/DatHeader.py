try:
    from MSE.Structs.PyStruct import PyStruct
    from MSE.Structs.GameStructs.Gmd import GmdFile
    from MSE.Structs.constructBoilerplate import *
except:
    from PyStruct import PyStruct
    from Gmd import GmdFile
    import sys
    sys.path.insert(1, '..')
    from constructBoilerplate import *
    
DatHeader = Struct(
    "identifier" / UInt16,
    "num_entries" / UInt32,
)

emptyDat = Struct()
class DatFile(PyStruct):
    datEntry = emptyDat
    def __init__(self,fileName):
        self.struct = Struct(
            "header" / DatHeader,
            "entries" / self.datEntry[this.header.num_entries],
        )
        super().__init__(fileName)
        if hasattr(self, "nameGmd"):
            self.loadGmdData(self.nameGmd,"name","gmd_name_index")
        if hasattr(self, "descGmd"):
            self.loadGmdData(self.descGmd,"desc","gmd_description_index")
        if hasattr(self, "setGmd"):
            self.loadGmdData(self.setGmd,"setname","set_group")
    def __iter__(self):
        return iter(self.structData.entries)
    def __getitem__(self,val):
        return self.structData.entries[val]
    def loadGmdData(self,gmdPath,attr, key):
        gmd = GmdFile(gmdPath)
        for entry in self:
            setattr(entry,attr,gmd[getattr(entry,key)])
            
        