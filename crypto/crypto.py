import typing
import hashlib
from Crypto.Random import get_random_bytes

key = get_random_bytes(32)

print(key)

def encrypt(nFile, OutFile, keyAes):
    file_out = open("key.txt", "wb")
    file_out.write(key)
    file_out.close()


def decrypt():
    pass