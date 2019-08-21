from itertools import combinations as com

def combination_my(n, m):
    assert n>m
    from math import factorial
    return int(factorial(n)/(factorial(m)*factorial(n-m)))

s= 0
e = 0
ls  = [1,1,1,1,2,2,3,3,4]
fnd = [1,1,1,1,2,2,3,3]

for var in com(ls, len(fnd)):
    v = sorted(var)
    if v == fnd:
        e +=1
    s +=1
print(e/s)
print(1/combination_my(len(ls), len(fnd)))
