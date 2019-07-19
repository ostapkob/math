from functools import lru_cache

# @lru_cache()
def kuzn(n, ls):

    if n <= 1:
        return 1
    else:
        # new_ls = [x for x in ls if x<=n]
        return sum([kuzn(n-x, ls) for x in [x for x in ls if x<=n]])

# coin = [1, 2, 5, ]
coin = [1,2,5,10]
print(kuzn(27, coin))
# for i in range(12):
#     print(i, ':', kuzn(i, coin))
