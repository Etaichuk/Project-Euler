#Find the difference between the
# sum of the squares of the first one hundred natural numbers
# and the square of the sum.

def sol_6(n):
    sum_squares = n*(n + 1)*(2*n + 1)//6
    square_sum = ((n*(n+1))//2)**2
    return square_sum - sum_squares