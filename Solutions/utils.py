import math


def primes_list(n):
    ''' return a list with the primes up to number n'''
    primes = [2]
    for i in range (2,n):
        p = 1
        for j in primes:
            if (i % j) == 0:
                p = 0
                break
        if p == 1:
            primes.append(i)
    return primes


def primes_decompose(n):
    '''Decompose n into it's primes factors'''
    i = 2
    primes_factors = []
    while i * i <= n:
        if n % i != 0:
            i += 1
        else:
            n = n // i
            primes_factors.append(i)
    if n > 1:
        primes_factors.append(n)
    return primes_factors


def nth_prime(n):
    '''return the nth number prime'''
    primes = [2]
    i = 3
    while True:
        p = 1
        for j in primes:
            if (i % j) == 0:
                p = 0
                break

        if p == 1:
            primes.append(i)

        if len(primes) == n:
            break

        i += 1

    return primes[-1]


def lcm(x, y):
    return x * y // math.gcd(x, y)


def decompose_factors(n):
    '''return a list of the factors of n'''

    factors = []

    for i in range(1, n + 1 // 2):
        if n % i == 0:
            factors.append(i)

    return factors

def decompose_factors_2(n):
    '''return a list of the factors of sqrt(n)'''

    factors = []

    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)

    return factors