# -*- coding: utf-8 -*-
try:
    from .Encryption import decrypt, encrypt
    from .SaveHeader import SaveHeader
    from .SaveSettings import SaveSettings
    from .SaveSlots import SaveSlots
    from ...Structs.SaveStructs.SaveSections import SaveStructure
except:
    from Encryption import decrypt, encrypt
    import sys
    sys.path.insert(1, '...')
    from Structs.SaveStructs.SaveSections import SaveStructure
    from SaveHeader import SaveHeader
    from SaveSettings import SaveSettings
    from SaveSlots import SaveSlots
    
SAVESIGNATURE = bytearray([0x72,0xC8,0x62,0x47,0xA2,0xA4,0xF0,0xC1])
DECRYPTEDSIGNATURE = bytearray([0x01,0x00,0x00,0x00,0x19,0x05,0x17,0x20])
SAVELENGTH = 0x9004E0
class invalidFileError(Exception):pass

class saveFile():
    def __init__(self, filepath):
        with open(filepath,"rb") as savehandle:
            saveBin = savehandle.read()
        encrypted = self.checkEncryption(saveBin)
        saveFile = self.decryptSave(saveBin) if encrypted else saveBin
        self.deserialize(saveFile)
        
    def checkEncryption(self,saveData):
        encryptedSig = saveData[0:8] == SAVESIGNATURE
        decryptedSig = saveData[0:8] == DECRYPTEDSIGNATURE
        if not (encryptedSig or decryptedSig):
            raise invalidFileError("File is not a save. Mismatch to encrypted or decrypted signature.")
        return encryptedSig
    
    def decryptSave(self, saveData):
        decrypted = decrypt(saveData)
        self.checkEncryption(decrypted)
        assert not self.checkEncryption(decrypted)
        return decrypted
    
    def deserialize(self, saveFile):
        try:
            self.struct = SaveStructure.parse(saveFile)
            self.header = SaveHeader(self.struct.header)
            self.settings = SaveSettings(self.struct.data.controls,self.struct.data.options,self.struct.data.unknown)
            self.saveslots = SaveSlots(self.struct.data.savefiles)
        except:
            raise invalidFileError("File structure is corrupted.")
        
if '__main__' in __name__:
    s = saveFile(r"C:\Users\aguevara\Downloads\SAVEDATA1000")