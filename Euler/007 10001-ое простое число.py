# Выписав первые шесть простых чисел, получим 2, 3, 5, 7, 11 и 13.
# Очевидно, что 6-ое простое число - 13.
# Какое число является 10001-ым простым числом?

import time
def is_prime(n):
    if n % 2 == 0:
        return False
    d = 2
    while d*d <= n and n % d != 0:
        d += 1
    return d <= n and n % d != 0
start = time.time()

num = 0
i = 1
prime = 1
while i < 10 ** 6:
    i += prime
    if is_prime(i):
        prime =i
        if num == 10000:
            print(num, i)
            break
        num += 1
print(time.time()-start)
