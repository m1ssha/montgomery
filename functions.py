def gcd_extended(a, b):
      if b == 0:
        return (a, 1, 0)
      else:
        (d, x1, y1) = gcd_extended(b, a % b)
        return (d, y1, x1 - (a // b) * y1)

def mod_inverse(a, m):
      (d, x, y) = gcd_extended(a, m)
      if d != 1:
        return -1
      else:
        return (x % m)
