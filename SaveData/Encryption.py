from Crypto.Cipher import Blowfish
import sys
import struct
import hashlib
from pathlib import Path

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
def endianness_reversal(data):
    return b''.join(map(lambda x: x[::-1],chunks(data, 4)))

def CapcomBlowfishDecrypt(file):
    cipher = Blowfish.new(b"xieZjoe#P2134-3zmaghgpqoe0z8$3azeq", Blowfish.MODE_ECB)
    return bytearray(endianness_reversal(cipher.decrypt(endianness_reversal(file))))

def CapcomBlowfishEncrypt(file):
    cipher = Blowfish.new(b"xieZjoe#P2134-3zmaghgpqoe0z8$3azeq", Blowfish.MODE_ECB)
    return endianness_reversal(cipher.encrypt(endianness_reversal(bytes(file))))

def CalculateChecksum(file):
    checksum = endianness_reversal(hashlib.sha1(file[64:]).digest())
    file[12:12+0x14]=bytearray(checksum)
    return file

decrypt = CapcomBlowfishDecrypt
encrypt = CapcomBlowfishEncrypt
   
def changeSteamID():
    saveFile = sys.argv[1]
    with open(saveFile,"rb") as sf:
        data = bytearray(sf.read())
        dec = CapcomBlowfishDecrypt(data)
        steamID = int.from_bytes(dec[0x28:0x32], byteorder='little', signed=False)   
        steamID = input("Current Steam ID: %d - New Steam ID: "%steamID)
        try:
            steamID = int(steamID)
        except:
            input("Invalid Value Inputted")
            return
        steamIDBin = bytearray(steamID.to_bytes(8, byteorder='little',signed=False))
        dec[0x28:0x30] = steamIDBin
        newob = CalculateChecksum(dec)
        out = CapcomBlowfishEncrypt(newob)
    with open(saveFile,"wb") as outfile:
        outfile.write(out)
        return

def decryptSave(filepath):
    with Path(filepath).open("rb") as savef:
        data = bytearray(savef.read())
    if data[0:4] == b'\x01\x00\x00\x00':
        enc = CapcomBlowfishEncrypt(data)
        with Path(filepath).with_suffix('').open("wb") as outf:
            outf.write(enc)
    else:
        dec = CapcomBlowfishDecrypt(data)
        with Path(filepath).with_suffix('.bin').open("wb") as outf:
            outf.write(dec)    
            

if __name__ == "__main__":
    #changeSteamID()
    decryptSave(sys.argv[1])
            
            
    
#    path = r"D:\Program Files (x86)\Steam\userdata\214331925\582010\remote"
#    for f in ("SAVEDATA1000Instant","SAVEDATA1000-PreIB","SAVEDATA1000"):
#        save = open(r"%s\%s"%(path,f),"rb").read()
#        dec = CapcomBlowfishDecrypt(save)
#        decsave = open(r"%s\%s.bin"%(path,f),"wb").write(dec)