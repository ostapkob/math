from math import factorial
res = 0
for i in range(3, 100000):
    s = list(map(int, list(str(i))))
    if i == sum([factorial(x) for x in s]):
        print(i)
        res+=i
print(res)
