# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isprime(n):
    limit = int(n**(1/2)) + 1
    for q in range(2, limit):
        if n%q == 0:
            return False
    return True


def prime_place(n):
    if n == 1:
        return 2
    p = 3
    count = 2
    while True:
        if isprime(p):
            if count == n:
                return p
            count += 1
        p += 2