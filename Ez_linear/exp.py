# -*- coding utf-8 -*-
# @Time : 2024/1/1 19:40
import string
from output import A,c
from Crypto.Util.number import *
for i in range(len(A)):
    A[i]=list(A[i])
s = b'flag{'
s = bytes_to_long(s)
s = [int(i) for i in bin(s)[2:].zfill(40)]
s1 = b'}'
s1 = bytes_to_long(s1)
s1 = [int(i) for i in bin(s1)[2:].zfill(8)]
for i in range(len(s)):
    t = [0]*336
    t[i] = 1
    A.append(t)
    c.append(s[i])
for i in range(8):
    t = [0]*336
    t[i+328] = 1
    A.append(t)
    c.append(s1[i])
for i in range(36):
    t = [0]*336
    t[40+i*8] = 1
    A.append(t)
    c.append(0)
A = Matrix(GF(2),A)
c = vector(c)
res = A.solve_right(c)
k = A.right_kernel()
def j(b):
    for i in b:
        if chr(i) in string.printable:
            continue
        else:
            return 0
    return 1
for i in k:
    temp = res + i
    temp = [str(i) for i in temp]
    if j(long_to_bytes(int(''.join(temp),2))):
        print(long_to_bytes(int(''.join(temp),2)))
# output
# b"flag{'jfevyvV\\.XJFDX|#8z/M)vTQ($,UI\r %_ U}"
# b'flag{f66a51d2-485f-4ad7-8466-0386b945263a}'