from itertools import permutations as var
from math import factorial

def combination_my(n, m):
    assert n>m
    from math import factorial
    return int(factorial(n)/(factorial(m)*factorial(n-m)))

num = 8
yes = 0
no = 0
total = 0
for i in var(range(1, num+1), int(num/2)):
    if (1 in i or 2 in i) and not(1 in i and 2 in i):
        # print('++', i)
        no += 1
    else:
        # print('--', i)
        yes += 1
    total += 1

print(no, yes, total)
print(no,combination_my(16,8))
print(combination_my(2,1)*combination_my(14, 7)/combination_my(16,8))
print(((combination_my(5,1)*combination_my(19, 2))/combination_my(24, 19)))

