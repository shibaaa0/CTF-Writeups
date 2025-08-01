from pwn import *
p=remote('83.136.253.59',49225)
for i in range(10):
    p.send(b'w')
p.interactive()
