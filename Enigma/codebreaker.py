from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

simple_key=get_random_bytes(32)
print(simple_key)

salt=b'\xbb\xcd\xf1\xb8\x90\n\xa8J\x82-\xd7\xb1\xcd\xa2\xf2\xefn\xb7\x84S\x00\x91\xb2\xa6\xc9\xd3\x81=\x86\xc6\xb9_'
password="mypassword"
key=PBKDF2(password,salt,dkLen=32)
message=b"Secret Message from Hitler"
cipher=AES.new(key,AES.MODE_CBC)
ciphered_data=cipher.encrypt(pad(message, AES.block_size))
print(ciphered_data)
with open('encrypted.bin','wb')as f:
    f.write(cipher.iv)
    f.write(ciphered_data)
'''with open('encrypted.bin','rb')as f:
    iv=f.read(16)
    decrypt_data=f.read()
cipher = AES.new(key,AES.MODE_CBC,iv=iv)
original=unpad(cipher.decrypt(decrypt_data),AES.block_size)'''

with open('key.bin','wb') as f:
    f.write(key)


