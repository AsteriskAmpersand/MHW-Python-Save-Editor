from Crypto.Cipher import Blowfish
import sys
import struct

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]
        
def endianness_reversal(data):
    return b''.join(map(lambda x: x[::-1],chunks(data, 4)))

def CapcomBlowfishDecrypt(file):
    cipher = Blowfish.new(b"xieZjoe#P2134-3zmaghgpqoe0z8$3azeq", Blowfish.MODE_ECB)
    return endianness_reversal(cipher.decrypt(endianness_reversal(file)))

def CapcomBlowfishEncrypt(file):
    cipher = Blowfish.new(b"xieZjoe#P2134-3zmaghgpqoe0z8$3azeq", Blowfish.MODE_ECB)
    return endianness_reversal(cipher.encrypt(endianness_reversal(file)))

if __name__ == "__main__":
    if len(sys.argv)<2:
        saveFile = r"D:\Program Files (x86)\Steam\userdata\214331925\582010\remote\SAVEDATA1000"
    else:
        saveFile = sys.argv[1]
    with open(saveFile, "rb") as sf:
        orig = sf.read()
        save = CapcomBlowfishDecrypt(orig)
        resave = CapcomBlowfishEncrypt(save)
        print (orig==resave)
        
    print("Melder Slot 1:" + hex(struct.unpack('I',save[0x3DACA9:0x3DACA9+4])[0]))
    print("Food Slot 1:" + hex(struct.unpack('I',save[0x3DACAD:0x3DACAD+4])[0]))
        