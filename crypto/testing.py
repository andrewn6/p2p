import random
import string
from crypto import *


count = 0
num = int(input("How many test cases would you like to be ran? "))

for _ in range(num):
    letters = string.ascii_lowercase
    testcase = (''.join(random.choice(letters) for i in range(10)))

    with open('text.txt', "r") as f:
        contenta = f.read()

    encrypt("text.txt")
    decrypt("text.txt")

    with open ('text.txt', "r") as f:
        contentb = f.read()

    if contenta == contentb:
        count += 1


print(count)
