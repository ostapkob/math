# За круглым столом рассаживаются 5 мужчин и
# 5 женщин. Найти вероятность того, что: а) никакие два лица одного
# пола не сядут рядом; б) супруги сядут рядом, если эти мужчины и
# женщины образуют 5 супружеских пар
from math import factorial
import itertools
from pprint import pprint

def even_on_even(ls):
    if len(ls)%2 !=0:
        return False
    for en in range(len(ls)-1):
        if (ls[en]+ ls[en+1])%2==0:
            return False
    return True


def pars_even_not_even(ls):
    if len(ls)%2 !=0:
        return False
    len_ls = len(ls)
    n = 0
    while n<len_ls:
        if abs(ls[n]-ls[n+1])!=1:
            break
        n+=2
    # print(n, end='"')
    if n==len_ls:
        return True

    if abs(ls[0]-ls[-1])!=1:
        return False
    n = 1
    while n<len_ls-1:
        if abs(ls[n]-ls[n+1])!=1:
            # print(ls[n], ls[n-1], end='l')
            break
        n+=2
    if n==len_ls-1:
        return True
    return False
ls =  list(range(1, 4))

print(list(itertools.permutations(ls,2)))
print(list(itertools.product(ls, repeat=2)))
print(list(itertools.combinations(ls,2)))
print(list(itertools.combinations_with_replacement(ls,2)))
print(list(itertools.permutations(ls,3)))

variants = itertools.permutations(ls)
mas = []
mas1 = []
for i in variants:
    mas.append((i,even_on_even(i)))
    mas1.append((i,pars_even_not_even(i)))
    # print(i,pars_even_not_even(i))
res = 0
res1 = 0
for val, ft in mas:
    if ft:
        res+=1

for val, ft in mas1:
    if ft:
        # print(val)
        res1+=1
print(res)
print(res1)
