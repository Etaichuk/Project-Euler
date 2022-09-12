# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def problem_1(n, p, q):
    k_1 = n//p
    k_2 = n//q
    k_3 = n//(p*q)
    num = p*(k_1*(k_1 + 1)//2) + q*(k_2*(k_2 + 1)//2) - p*q*(k_3*(k_3 + 1)//2)
    return num