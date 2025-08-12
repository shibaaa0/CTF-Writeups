def generate_key(u1: str, u2: str) -> list[int]:
    maxlen = max(len(u1), len(u2))
    key = []
    for i in range(maxlen):
        ch1 = ord(u1[i]) if i < len(u1) else 0
        ch2 = ord(u2[i]) if i < len(u2) else 0
        key.append(ch1 ^ ch2)

    for i in range(len(key)):
        val = key[i]
        shift = i % 8
        key[i] = ((val >> (8 - shift)) | (val << shift)) & 0xFF

    key.reverse()
    return key

def decrypt(key: list[int], encrypted_hex: str) -> str:
    ciphertext = bytes.fromhex(encrypted_hex)
    plaintext = bytes([c ^ key[i % len(key)] for i, c in enumerate(ciphertext)])
    return plaintext.decode(errors="replace")

# ==== NHẬP VÀO DỮ LIỆU Ở ĐÂY ====
username1 = "hun73r12"
username2 = "__purten75"
encrypted_hex = "08544f76b472694f3c03045c1b4aa6246027635f59684626f1644d016442355a5b20f74b2a4b0b5a13684026b74b2a4b610035515c24f37a7605"  # <-- chuỗi hex từ Encrypted Text

# ==== GIẢI MÃ ====
key = generate_key(username1, username2)
flag = decrypt(key, encrypted_hex)
print("Decrypted flag:", flag)
