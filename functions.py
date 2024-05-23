import gmpy2


def calculate_r(n):
    for i in range(0, 2048):
        r = gmpy2.mpz(2) ** i
        if (r > n) and (r / 2 <= n) and gcd(r, n) == 1:
            return i


def gcd(r, n):
    if n == 0:
        return r
    else:
        return gcd(n, r % n)


def negative_inverse_calc(n, bit_width, base):
    def_base = gmpy2.mpz(2) ** (bit_width - 1)
    neg_inverse = base - pow(n, def_base - 1, base)
    return neg_inverse


def product(a, b, r, n, bit_width):
    t = (a * b) % r
    m = (t * negative_inverse_calc(n, bit_width, r)) % r
    s = (a * b + m * n) // r
    if s >= n:
        return s - n
    else:
        return s
