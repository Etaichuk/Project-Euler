#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def isprime(n, primes):
    for q in primes:
        if n%q == 0:
            return False
    return True


def primes(n):
    primelist = [2]
    p = 3
    while p<=n:
        if isprime(p, primelist):
            primelist.append(p)
            yield p
        p += 2

def sol_3a(n):
    prime_fac = []
    k = int(n**(1/2)) + 1
    for p in primes(k):
        if n%p == 0:
            prime_fac.append(p)
            n = n//p
    if len(prime_fac) > 0:
        return max(prime_fac)
    return n


def sol_3b(n):
    m = n
    max_factor = 1
    if m%2 == 0:
        max_factor = 2
        m = m//2
        while m %2 == 0:
            m = m//2

    k = 3
    while k <= m:
        if m%k == 0:
            max_factor = k
            m = m//k
            while m % k == 0:
                m = m // k
        k += 2
    return max_factor


def sol_3c(m):

    if m % 2 == 0:
        last_factor = 2
        m = m//2
        while m % 2 == 0:
            m = m//2

    k = 3
    last_factor = 1
    max_factor = int(m**(1/2)) + 1

    while k < max_factor and m > 1:
        if m % k == 0:
            last_factor = k
            m = m//k
            while m % k == 0:
                m = m // k
            max_factor = int(m ** (1 / 2)) + 1
        k += 2

    if m == 1:
        return last_factor
    return m