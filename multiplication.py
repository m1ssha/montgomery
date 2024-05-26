import gmpy2
import functions


def multiplication(a, b, n):
    bit_width = functions.calculate_r(n)
    r = gmpy2.mpz(2) ** bit_width
    x = (a * r) % n
    y = (b * r) % n
    montg_product = functions.product(x, y, r, n, bit_width)
    product_result = functions.product(montg_product, gmpy2.mpz(1), r, n, bit_width)

    return product_result
