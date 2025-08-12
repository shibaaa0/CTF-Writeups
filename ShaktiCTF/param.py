from math import gcd

# Extended Euclidean Algorithm
def extended_gcd(a, b):
    if b == 0:
        return a, 1, 0
    g, x1, y1 = extended_gcd(b, a % b)
    return g, y1, x1 - (a // b) * y1

# Generalized CRT: solves x ≡ a mod m, x ≡ b mod n
def crt_pair(a1, m1, a2, m2):
    g, s, t = extended_gcd(m1, m2)
    if (a2 - a1) % g != 0:
        return None, None  # No solution
    lcm = m1 * m2 // g
    x = (a1 + (a2 - a1) // g * s % (m2 // g) * m1) % lcm
    return x, lcm

# Full CRT for multiple (remainder, modulus) pairs
def generalized_crt(equations):
    x, m = equations[0]
    for a, n in equations[1:]:
        x, m = crt_pair(x, m, a, n)
        if x is None:
            raise ValueError("No solution exists")
    return x, m

# Your conditions
conds = [
    (0x5c, 0x7b),    # (92, 123)
    (0x1d, 0x1c8),   # (29, 456)
    (0x17c, 0x315),  # (380, 789)
    (2, 0x3db),      # (2, 987)
    (0x1f1, 0x28e),  # (497, 654)
    (0x128, 0x141),  # (296, 321)
]

# Run CRT
param1, modulus = generalized_crt(conds)
print(f"param_1 = {param1}")
print(f"(Smallest positive solution, repeats every {modulus})")
