import itertools
from math import factorial
from operator import mul
from functools import reduce


def fac(n, k):
    res = 1
    for i in range(n+1, k+1):
        res *= i
    return res


n = 25
f1 = factorial(365)/(365**n * factorial(365-n))
f3 = fac(365-n, 365)/365**n
m = reduce(mul, range(366-n, 366))
print(m, fac(365-n, 365))
print("don't guess", f1, f3)
