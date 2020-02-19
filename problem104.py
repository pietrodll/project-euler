import math

def is_pandigital_last(N):
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    n = N
    if n < 100000000: return False
    for _ in range(9):
        digits.discard(n % 10)
        n = n // 10
    return len(digits) == 0


def is_pandigital_first(N):
    digits = {1, 2, 3, 4, 5, 6, 7, 8, 9}
    pow = int(math.log(N, 10)) + 1
    if pow < 9: return False
    n = N // 10**(pow - 9)
    for _ in range(9):
        digits.discard(n % 10)
        n = n // 10
    return len(digits) == 0


def find_number():
    a = 1
    b = 1
    k = 2
    while not is_pandigital_first(b) or not is_pandigital_last(b):
        a, b = b, a + b
        k += 1
    return k

print(find_number())

