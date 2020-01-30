'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def get_primes_bis(N):
    primes = [False] * N
    prime_list = []
    for i in range(N):
        if is_prime(i):
            primes[i] = True
            prime_list.append(i)
    return primes, prime_list


def get_primes(N, verbose=0):
    primes = [False] * 2 + [True] * (N - 2)
    i = 2
    while i < N:
        j = 2
        while j*i < N:
            primes[j*i] = False
            j += 1
        i += 1
        while i < N and not primes[i]:
            i += 1

    prime_list = [i for i in range(N) if primes[i]]

    if verbose == 1:
        print(prime_list)
    elif verbose == 2:
        print(prime_list)
        print(primes)

    return primes, prime_list


def longest_prime_sum_from_start(N, start, primes, prime_list):

    longest = 0
    index = start
    S = 0
    i = start

    while S < N and i < len(prime_list):
        if primes[S]:
            longest = S
            index = i

        S += prime_list[i]
        i += 1
    
    return longest, index - start


def longest_prime_sum(N):
    primes, prime_list = get_primes(N)

    max_len = 0
    max_len_sum = 0
    for i in range(N):
        S, length = longest_prime_sum_from_start(N, i, primes, prime_list)
        if length > max_len:
            max_len = length
            max_len_sum = S
    return max_len_sum, max_len


def check_primes(N):
    primes, prime_list = get_primes(N)
    primes_bis, prime_list_bis = get_primes_bis(N)
    for i in range(len(primes)):
        assert primes[i] == primes_bis[i]
    assert len(prime_list) == len(prime_list_bis)
    for i in range(len(prime_list)):
        assert prime_list[i] == prime_list_bis[i]
    print('No error found')


check_primes(1000)


print(longest_prime_sum(1000000))