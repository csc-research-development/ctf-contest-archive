from ctypes import CDLL
from pwn import *

#io = process("./temple")
io = remote("103.185.44.248", 1338)
libc = CDLL("/lib/x86_64-linux-gnu/libc.so.6")
seed = 0

io.sendline(f"{seed}".encode())

libc.srand(seed)
a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p = libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand(), libc.rand()

def newSeed(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
    return j ^ p ^ a ^ m ^ f ^ b ^ e ^ i ^ d ^ h ^ c ^ g ^ k ^ l ^ n ^ o

seed = newSeed(f, a, m, c, j, b, e, d, g, i, h, k, l, n, o, p)
libc.srand(seed%10000)

io.sendline(f"{libc.rand()%10000}".encode())
io.interactive()
