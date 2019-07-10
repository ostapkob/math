# The sum of the squares of the first ten natural numbers is,
#     12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
#     (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

import matplotlib.pyplot as plt
from pprint import pprint
from functools import reduce
from MyFunctions import print_lists


def sum_square(num):
    return sum(range(1, num+1))**2


def square_sum(num):
    return sum([x*x for x in range(1, num+1)])


def two_multiply(num):
    return sum([((i**2)+2*i*j) - (i**2)
                for i in range(1, num+1)
                for j in range(i+1, num+1)])


def sq_sum(n):
    s1 = 0
    s2 = 0
    for i in range(1, n+1):
        s1 += (i**2)
        s2 += (i**2)
        for j in range(i+1, n+1):
            s1 += 2*i*j
    return s1-s2


num = list(range(1, 11))
pol = ['---' for _ in num]
s1 = [sum_square(x) for x in num]
s2 = [square_sum(x) for x in num]
s3 = [sum_square(x)-square_sum(x) for x in num]
s4 = [two_multiply(x) for x in num]
s5 = [sq_sum(x) for x in num]
print_lists([num, pol, s1, s2, s3, s4])
