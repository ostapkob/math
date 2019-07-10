import time


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def IsPrime2(n):
    d = 2
    while d * d < n and n % d != 0:
        d += 1
    return d == n


print(IsPrime2(7))

start = time.time()

# for i in range(2, 10):
#     print(i, IsPrime(i))
a = [i for i in range(2, 10000) if IsPrime2(i)]

print(sum(a))
print(start - time.time())
