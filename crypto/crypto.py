# import necessary libraries/modules
import typing
import bcrypt
from cryptography.fernet import Fernet

def encrypt(ifile:str) -> None:

    """Encrypt file"""
    global key
    key = Fernet.generate_key()


    # string the key in a file
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)

    # opening the key
    with open('filekey.key', 'rb') as filekey:
        key = filekey.read()

    # using the generated key
    fernet = Fernet(key)

    # read in the original file
    with open(ifile, 'rb') as file:
        original = file.read()

    # encrypt the file
    encrypted = fernet.encrypt(original)

    # write the encrypted file to the original file
    with open(ifile, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)


def decrypt(file:str) -> None:
    """Decrypt file"""

    # using the key
    fernet = Fernet(key)


    # opening the encrypted file
    with open(file, 'rb') as enc_file:
        encrypted = enc_file.read()

    # decrypting the file
    decrypted = fernet.decrypt(encrypted)

    # opening the file in write mode and
    # writing the decrypted data
    with open(file, 'wb') as dec_file:
        dec_file.write(decrypted)








