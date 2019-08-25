from itertools import combinations as com
from itertools import permutations as per

# for i in com(range(3), 3):
#     print(i)


def find3(ls: list, count_simvols: int, sums: int):
    for i in range(len(ls)-count_simvols+1):
        if sum(ls[i: i+count_simvols]) == sums:
            return True
    return False


a = [0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
itog = 0
res = 0
for i in per(a, 10):
    itog += 1
    if find3(i, 3, 3):
        res += 1

print(res / itog)
print(res , itog)
