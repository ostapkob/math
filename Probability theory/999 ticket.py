from math import log
count = 100000000000000000000
ver = count/2
rez = .5
for n in range(1, count):
    rez *= ver/(count-n)
    if rez < 0.001:
        print(n, rez)
        break
print(log(10, 100))

print(100**0.5)
