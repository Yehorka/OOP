from os import path
from timeit import timeit
from random import randint

f = open("sample.txt", "w")
while (path.getsize('sample.txt')/(1000000)) < 50:
    f.write(str(randint(0, 10000))+ "\n")

s = """
file1 = open("sample.txt", "r")
res = 0
for line in file1.readlines():
    if line.strip().isdigit():
        res+=1
file1.close()
"""
print(timeit(s, number=10))

s = """
file2 = open("sample.txt", "r")
res = 0
for line in file2:
    if line.strip().isdigit():
        res+=1
file2.close()
"""
print(timeit(s, number=10))

s = """
file3 = open("sample.txt", "r")
res = sum(int(line.strip().isdigit()) for line in file3)
file3.close()
"""
print(timeit(s, number=10))