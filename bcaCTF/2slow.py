from sympy import fibonacci, prime
from functools import lru_cache

# Dữ liệu mã hóa (từ GDB `x/27bx 0x555555556020`)
encrypted_flag = [
    0xEA, 0x09, 0x12, 0x47, 0x98, 0x2D, 0xDB, 0x17,
    0xD5, 0xBE, 0xE3, 0xDE, 0xCF, 0x62, 0xB3, 0xB2,
    0x73, 0xAF, 0xE6, 0xE1, 0xB5, 0x5F, 0xC3, 0x19,
    0x0E, 0xFD, 0x00
]

# Sử dụng cache để tránh tính lặp lại (tăng tốc nếu chạy nhiều lần)
@lru_cache(maxsize=None)
def fast_fib(n):
    return fibonacci(n) % 256

@lru_cache(maxsize=None)
def fast_prime(n):
    return prime(n) % 256

flag = ''.join(
    chr(encrypted_flag[i] ^ fast_fib(i + 10000) ^ fast_prime(i + 500000))
    for i in range(27)
)

print("Flag:", flag)
