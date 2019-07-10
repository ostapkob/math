# Сумма простых чисел меньше 10 равна 2 + 3 + 5 + 7 = 17.
# Найдите сумму всех простых чисел меньше двух миллионов.
import time
from math import sqrt
def is_prime(n):
    if n % 2 == 0:
        return False
    d = 2
    while d <= n**(1/2) and n % d != 0:
        d += 1
    return d <= n and n % d != 0

n = 1000000
start = time.time()
s = 3
for i in range(n):
    if is_prime(i):
        s += i
print(s, 'for', time.time() - start)


start = time.time()
mas = [True]*n
for p in range(2, n):
    if p:
        for j in range(p*p, n, p):
            mas[j]=False
s = 0
for el, m in enumerate(mas):
    if m:
        s += el
print(s, 'for', time.time() - start)
