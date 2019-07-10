from functools import lru_cache
import time
import MyFunction

@lru_cache()
def fib (n):
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)


start = time.time()
n, l = 0, 0
# while l < 1000:
#     n +=1
#     l = MyFunction.len_x(fib(n))
# print(n,  l, sep=' : ')
# print(time.time() - start)
a, b = 0, 1
for i in range(1000):
    a, b = b, a+b

print(a, b)
