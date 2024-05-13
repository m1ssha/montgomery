def calculate_r(n):
    for i in range(0, 32):
        r = 2 ** i
        if (r > n) and (r / 2 <= n):
            return i


def negative_inverse_calc(n, bit_width, base):
    def_base = 2 ** (bit_width - 1)
    neg_inverse = base - n ** (def_base - 1) % base
    return neg_inverse


def product(a, b, r, n, bit_width):
    t = a * b % r
    m = (t * negative_inverse_calc(n, bit_width, r)) % r
    s = (a * b + m * n) / r
    if s >= n:
        return s - n
    else:
        return s

