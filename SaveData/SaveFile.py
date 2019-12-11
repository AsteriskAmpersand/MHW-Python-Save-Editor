# -*- coding: utf-8 -*-
try:
    from .Encryption import decrypt, encrypt
    from ...Structs.SaveStructs.SaveSections import SaveStructure
except:
    from Encryption import decrypt, encrypt
    sys.path.insert(1, '...')
    from Structs.SaveStructs.SaveSections import SaveStructure
    
SAVESIGNATURE = bytearray([0x72,0xC8,0x62,0x47,0xA2,0xA4,0xF0,0xC1])
DECRYPTEDSIGNATURE = bytearray([0x01,0x00,0x00,0x00,0x19,0x05,0x17,0x20])
SAVELENGTH = 0x9004E0
class invalidFileError(Exception):pass

class saveFile():
    def __init__(self, filepath):
        #TODO - Check if filepath exists
        #TODO - Check if save file opens correctly
        with open(filepath,"rb") as savehandle:
            saveBin = savehandle.read()
        #TODO - Check that it's a valid save encrypted (Sig) or decrypted (0s)
        encrypted = self.checkEncryption(saveBin)
        saveFile = self.decryptSave(saveBin) if encrypted else saveBin
        self.deserialize(saveFile)
        
    def checkEncryption(self,saveData):
        encryptedSig = saveData[0:8] == SAVESIGNATURE
        decryptedSig = saveData[0:8] == DECRYPTEDSIGNATURE
        if not (encryptedSig or decryptedSig):
            raise invalidFileError("File is not a save. Mismatch to encrypted or decrypted signature")
        return encryptedSig
    
    def decryptSave(self, saveData):
        decrypted = decrypt(saveData)
        self.checkEncryption(decrypted)
        assert not self.checkEncryption(decrypted)
        return decrypted
    
    def deserialize(self, saveFile):
        #TODO - Error check the parsing
        struct = SaveStructure.parse(saveFile)
        print(struct.data.savefiles[0].hunterName)
        
if '__main__' in __name__:
    s = saveFile(r"D:\Program Files (x86)\Steam\userdata\214331925\582010\remote\SAVEDATA1000")