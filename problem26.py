"""
Problem 26
==========

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with
denominators 2 to 10 are given:

    1/2	= 	0.5
    1/3	= 	0.(3)
    1/4	= 	0.25
    1/5	= 	0.2
    1/6	= 	0.1(6)
    1/7	= 	0.(142857)
    1/8	= 	0.125
    1/9	= 	0.(1)
    1/10	= 	0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a
6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal
fraction part.
"""

from utils.divisors import mult_ord


# The length of the recurring cycle of N is the multiplicative order of 10 modulo N
# If N and 10 are not relative primes, N = N1 * N2 where N2 is a product of powers of 2 and 5
# and N1 is relatively prime with 10; then the length of the cycle is the multiplicative order of
# 10 modulo N1


def cycle_length(n):
    while n % 2 == 0:
        n //= 2

    while n % 5 == 0:
        n //= 5

    if n == 1:
        return 0

    return mult_ord(10, n)


def max_cycle_length(upper_limit):
    lmax = 0
    nmax = 1

    for n in range(1, upper_limit):
        length = cycle_length(n)

        if length > lmax:
            lmax = length
            nmax = n

    return nmax, lmax


if __name__ == "__main__":
    print(max_cycle_length(1000))
