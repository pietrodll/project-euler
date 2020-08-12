"""This module contains utility functions for divisors and prime numbers"""

from math import sqrt


def is_prime(n):
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def divisors(n, sort=False):
    div = [1]
    sqr = int(sqrt(n))

    for i in range(2, sqr + 1):
        if n % i == 0:
            div.append(i)

            if i != sqr:
                div.append(n // i)

    if sort:
        div.sort()

    return div


def divisor_sum(n):
    S = 1
    sqr = sqrt(n)

    for i in range(2, int(sqr) + 1):
        if n % i == 0:
            S += i

            if i != sqr:
                S += n // i

    return S
