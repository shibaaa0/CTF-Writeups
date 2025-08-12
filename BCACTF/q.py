from pwn import *
import ast

context.log_level = 'info'

HOST = 'challs.bcactf.com'
PORT = 32783

r = remote(HOST, PORT)

with open("output.txt", "w") as f:
    # Nhận đến khi thấy 'What is the secret?'
    data = r.recvuntil(b'What is the secret?', timeout=10).decode()
    print(data)
    f.write(data)
r.interactive()
