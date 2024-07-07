from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes
import random
with open('flag.txt') as handle:
	message = handle.read()
	m = bytes_to_long(message.encode())

p = getPrime(256)
q = getPrime(256)
n = p * q
n2 = 1
for i in range(50):
	n2 *= random.choice([p, q, p, q, p, 1])

e = 65537 
c = pow(m, e, n)
c2 = pow(m, e, n2)

print(f"e = {e}")
print(f"n = {n}")
print(f"c = {c}")
print(f"n2 = {n2}")
print(f"c2 = {c2}")