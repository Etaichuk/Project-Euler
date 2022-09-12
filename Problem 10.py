# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

def isprime(n):
    limit = int(n**(1/2)) + 1
    for q in range(2, limit):
        if n%q == 0:
            return False
    return True

def primes(n):
    p = 2
    while p <=n :
        if isprime(p):
            yield p
        p += 1

def sol_10a(n):
    num = 0
    for p in primes(n):
        num += p
    return num

def sol_10b(n):
    lis = [i for i in range(n+1)]

    lis[1] = 0
    curr = 2
    while curr <= n:
        for k in range(curr, n//curr + 1):
            lis[curr*k] = 0
        while lis[curr] == 0:
            curr += 1
    return sum(lis)
