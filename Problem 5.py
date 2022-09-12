# 2520 is the smallest number
# that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number
# that is evenly divisible by all of the numbers from 1 to 20?

def isprime(n):
    limit = int(n**(1/2)) + 1
    for q in range(2, limit):
        if n%q == 0:
            return False
    return True


def primes(n):
    p = 2
    while p <= n:
        if isprime(p):
            yield p
        p += 1

from math import log

def sol_5a(n):
    lcm = 1

    for p in primes(n):
        k = int(log(n)//log(p))
        lcm *= p**k

    return lcm

def gcd(a,b):
    c = min(a,b)
    d = max(a,b)
    if c == 0:
        return d
    else:
        return gcd(c, d % c)
def lcm(a,b):
    return a*b//gcd(a,b)

def seq_lcm(n):
    if n==3:
        return lcm(2,3)
    return lcm(seq_lcm(n-1), n)
