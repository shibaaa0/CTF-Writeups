import socket
import time

HOST = "challenge.nahamcon.com"
PORT = 31996

def main():
    with socket.create_connection((HOST, PORT)) as sock:
        sock.settimeout(2)

        while True:
            try:
                # Gửi một dòng trống
                sock.sendall(b"\n")
                time.sleep(0.1)

                # Nhận dữ liệu
                data = sock.recv(4096)
                if not data:
                    print("[!] Server đóng kết nối.")
                    break

                decoded = data.decode(errors="ignore")

                if "flag{" in decoded:
                    print("[+] Tìm thấy flag!")
                    print(decoded)
                    break

            except socket.timeout:
                continue  # không có phản hồi, gửi tiếp
            except KeyboardInterrupt:
                print("\n[!] Dừng bởi người dùng.")
                break

if __name__ == "__main__":
    main()
