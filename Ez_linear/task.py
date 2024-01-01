# -*- coding utf-8 -*-
# @Time : 2023/12/26 19:31
from Crypto.Util.number import *
flag = b'*****'

assert flag.startswith(b'flag{')
assert flag.endswith(b'}')
assert len(flag)==42
flag = bytes_to_long(flag)
m = [int(i) for i in bin(flag)[2:].zfill(336)]
A = random_matrix(GF(2),240,336)
m = vector(GF(2),m)
c = list(A*m)

print(c)
print(A)