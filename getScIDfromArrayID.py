import hashlib
import uuid
arrayID = raw_input("Please enter a FlashArray ID: ") 
def scid_uuid(farrayID):
   m = hashlib.md5()
   m.update(farrayID)
   b = m.digest()
   m = hashlib.md5()
   m.update(b)
   b = bytearray(m.digest())
   b[6] &= 0x0f 
   b[6] |= 0x30 
   b[8] &= 0x3f 
   b[8] |= 0x80 
   return uuid.UUID(bytes=str(b))

a = scid_uuid(arrayID)
newStr = str(a).replace('-', '')
myUuid = newStr[:16] + "-" + newStr[16:]
print "vvol:" + myUuid