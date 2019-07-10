from collections import defaultdict
from copy import deepcopy

def acceptable_steps(num, ls):
    steps = defaultdict(list)
    for n in range(1, num+1):
        for l in ls:
            if n-l>=0:
                steps[n].append(n-l)
    return steps

def variables_steaps(num, a=[]):
    if num < 0:

        print(a)#, end=' ')
        a=[]
        return 1
    else:
        a.append(num)
        b = deepcopy(a)
        variables_steaps(num-1, a)
        variables_steaps(num-2, b)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

coins = [1, 2,]
acc_steps = acceptable_steps(4, coins)
print(acc_steps)
variables_steaps(4)
