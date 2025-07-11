from collections import Counter

MOD = 5 ** 9
TR = 48
PHI = MOD - MOD // 5

def v5(n):
    if n == 0:
        return 9
    v = 0
    while n % 5 == 0:
        n //= 5
        v += 1
    return v

def count_bc_solutions(v):
    if v == 9:
        return 5**17  # bc = 0 case
    return (9 - v) * (5 ** (9 + v - 1)) + 5**17

def main():
    count_v = Counter()
    # Vì a và 48 - a đều trong Z/5^9, chỉ cần duyệt vài triệu mẫu là đủ đại diện
    STEP = 5**4  # duyệt 625 mẫu trong khoảng 1953125
    for a in range(0, MOD, STEP):
        d = (TR - a) % MOD
        r = (a * d - 1) % MOD
        t = v5(r)
        count_v[t] += 1

    scale = MOD // STEP
    total = 0
    for t in range(10):
        reps = count_v[t] * scale  # scale lên toàn miền
        total += reps * count_bc_solutions(t)

    print(total)

if __name__ == "__main__":
    main()
