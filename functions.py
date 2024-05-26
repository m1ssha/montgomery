import gmpy2


def calculate_r(n):
    i = n.bit_length() + 1
    r = gmpy2.mpz(2) ** i
    while gmpy2.gcd(r, n) != 1:
        i += 1
        r = gmpy2.mpz(2) ** i
    return i


def negative_inverse_calc(n, bit_width, base):
    def_base = gmpy2.mpz(2) ** (bit_width - 1)
    neg_inverse = base - pow(n, def_base - 1, base)
    return neg_inverse


def product(a, b, r, n, bit_width):
    t = (a * b) % r
    neg_inverse = negative_inverse_calc(n, bit_width, r)
    m = (t * neg_inverse) % r
    s = (a * b + m * n) // r
    if s >= n:
        return s - n
    else:
        return s