# The sequence of triangle numbers is generated
# by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

# Let us list the factors of the first seven triangle numbers:

#  1: 1
#  3: 1,3
#  6: 1,2,3,6
# 10: 1,2,5,10
# 15: 1,3,5,15
# 21: 1,3,7,21
# 28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?


def num_ID(n):
    pr_fac = {}
    if n%2 == 0:
        pr_fac[2] = 1
        n = n//2
        while n%2 == 0:
            pr_fac[2] += 1
            n = n//2
    p = 3
    while n > 1:
        if n%p == 0:
            pr_fac[p] = 1
            n = n//p
            while n%p == 0:
                pr_fac[p] += 1
                n = n//p
        p += 2
    return pr_fac

def sol_12(n):
    count = 1
    num = 1
    while count <= n:
        count = 1
        num += 1
        for val in num_ID(num*(num+1)//2).values():
            count *= val + 1

    return num*(num + 1)//2
