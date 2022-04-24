# imports
import typing
import bcrypt
from cryptography.fernet import Fernet

def encrypt(ifile:str) -> None:

    """Encrypt file"""
    global key
    key = Fernet.generate_key()


    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    fernet = Fernet(key)

    with open(ifile, 'rb') as file:
        original = file.read()

    encrypted = fernet.encrypt(original)

    with open(ifile, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt(file:str) -> None:
    """Decrypt file"""

    fernet = Fernet(key)


    with open(file, 'rb') as enc_file:
        encrypted = enc_file.read()

    decrypted = fernet.decrypt(encrypted)

    with open(file, 'wb') as dec_file:
        dec_file.write(decrypted)








