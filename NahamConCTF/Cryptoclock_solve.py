import socket
import time
import binascii

HOST = 'challenge.nahamcon.com'  # hoặc IP server
PORT = 30890

def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        data = s.recv(4096).decode()

        # Trích xuất ciphertext flag từ welcome message
        for line in data.splitlines():
            if "The encrypted flag is" in line:
                hex_flag = line.split(":")[1].strip()
                enc_flag = bytes.fromhex(hex_flag)
                break
        else:
            print("Không tìm thấy ciphertext flag")
            return

        print(f"[+] Encrypted flag: {enc_flag.hex()}")

        # Gửi input: "A" * len(flag)
        plaintext = b"A" * len(enc_flag)
        s.sendall(plaintext + b"\n")
        response = s.recv(4096).decode()
        for line in response.splitlines():
            if "Encrypted:" in line:
                hex_encrypted_input = line.split(":")[1].strip()
                enc_input = bytes.fromhex(hex_encrypted_input)
                break
        else:
            print("Không nhận được phản hồi đúng")
            return

        print(f"[+] Encrypted input: {enc_input.hex()}")

        # Tính key và giải mã flag
        key = xor_bytes(enc_input, plaintext)
        flag = xor_bytes(enc_flag, key)

        print(f"[+] Key: {key.hex()}")
        print(f"[!] FLAG: {flag.decode(errors='ignore')}")

if __name__ == "__main__":
    main()

