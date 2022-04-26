import random
import string
import tracemalloc
import timeit
from main import *

count = 0
num = int(input("How many test cases would you like to be ran? "))

# Initialize benchmarking
tracemalloc.start()
start = timeit.default_timer()

# Tests
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


end = timeit.default_timer()
memorg = tracemalloc.get_traced_memory()

# Test results
print(f"\n{count} successful tests out of {num} total.\nPercentage: {(num/count)*100:.5f}")

# Benchmarking
print(f"Time elapsed: {end-start}\nAverage time per test: {(end-start)/count}")
print(f"Total used memory: {(memorg[0] + memorg[1])/2}\nAverage memory used per test: {(memorg[0] + memorg[1])/(2*num)}")

tracemalloc.stop()

















