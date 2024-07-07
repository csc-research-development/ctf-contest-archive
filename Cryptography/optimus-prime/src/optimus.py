from Crypto.Util.number import getPrime, bytes_to_long
from random import randint

FLAG = b"CSC{Euler's_totient_function_solved43254}"
p = getPrime(32)
q = getPrime(32)
k = randint(5, 15)
n = p**k * q**k
m = bytes_to_long(FLAG)
e = 65537
ct = pow(m, e, n)

print(f"n = {n}")
print(f"ct = {ct}")