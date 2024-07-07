from Crypto.Util.number import getPrime, bytes_to_long
from random import randint

FLAG = b"CSC{fake_flag}"
p = getPrime(32)
q = getPrime(3)
k = randint(5, 15)
n = p**k * q**k
m = bytes_to_long(FLAG)
e = 65537
ct = pow(m,e,n)

print(f"n = {n}")
print(f"ct = {ct}")