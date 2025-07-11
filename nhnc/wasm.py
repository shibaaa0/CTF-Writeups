iv = b"Hi_I_am_iv_owo!!"
with open("challenge.wasm", "rb") as f:
    f.seek(65536 + 176)
    ciphertext = f.read(16)

plaintext = bytes([c ^ i for c, i in zip(ciphertext, iv)])
print(plaintext)
