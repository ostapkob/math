#This task not correct, it solve count permutations all coin
from functools import lru_cache

@lru_cache()
def kuzn(n):
    global coin
    if n <= 1:
        return 1
    else:
        return sum([kuzn(n-x) for x in [x for x in coin if x<=n]])

coin = [1,2,5,10,20, 50, 100, 200]
print(kuzn(200))
