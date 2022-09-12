# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def sol_9():

    for a in range(1,334):
        for b in range(a, 500 - a//2):
            if a**2 + b**2 == (1000 - a - b)**2:
                return a*b*(1000 - a -b)