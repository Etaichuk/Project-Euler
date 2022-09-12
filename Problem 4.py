# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers
# is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_pali(n):
    s = str(n)
    t = s[::-1]
    return s == t

def sol_4a(num):
    maxi = 0

    for n in range(10**(num - 1), 10**num - 1):
        for m in range(n, 10**num):
            if is_pali(n*m):
                maxi = max(maxi, n*m)

    return maxi

def sol_4b(num):
    maxi = 0
    a = 10**num - 1

    while a >= 10**(num-1):
        b = 10**num - 1
        while b >= a:
            if a*b < maxi:
                break
            if is_pali(a*b):
                maxi = a*b
            b -= 1
        a -= 1

    return maxi