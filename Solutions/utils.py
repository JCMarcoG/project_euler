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


def lcm(x, y):
    return x * y // math.gcd(x, y)