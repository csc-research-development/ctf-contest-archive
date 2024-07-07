from Crypto.Util.number import long_to_bytes
from sympy.ntheory import factorint
from pwn import *

def solver(e, n, ct):
    data = factorint(n)
    p, q = data.keys()
    assert len(set(data.values())) == 1

    k = data[p]
    phi = p**(k-1)*(p-1) * q**(k-1)*(q-1)
    d = pow(e, -1, phi)
    return long_to_bytes(pow(ct, d, n))

e = 0x10001

io = remote("103.185.44.248", 1347)
io.recvuntil(b"n = ")
n = int(io.recvline())
io.recvuntil(b"ct = ")
ct = int(io.recvline())

success(f"FLAG : {solver(e, n, ct)}")