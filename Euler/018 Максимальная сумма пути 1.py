import numpy as np
from pprint import pprint

def find_neighbors(mas, el: tuple):
    x, y = el[0], el[1]
    return mas[x + 1][y], mas[x + 1][y + 1]


def variables_payh(mas, keys, val=[],  step=-1):
    if len(val) >= len(mas):
        return val
    else:
        step += 1
        print(val)
        for key in keys:
            for k in key:
                for neg in find_neighbors(mas, k):
                    val.append(neg)
                    print(val)


n = np.array([
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10],
    [20, 4, 82, 47, 65],
    [19, 1, 23, 75, 3, 34],
    [88, 2, 77, 73, 7, 63, 67],
    [99, 65, 4, 28, 6, 16, 70, 92],
    [41, 41, 26, 56, 83, 40, 80, 70, 33],
    [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
    [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
    [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
    [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
    [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
    [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23] ])

n = np.array([
    [75],
    [95, 64],
    [17, 47, 82],
    [18, 35, 87, 10], ])
# список идексов всех элементов
# key = [(x, y) for x in range(len(n)) for y in range(x + 1)]
key = [[(y, x) for x in range(y+1)] for y in range(len(n))]
pprint(key)
# fn = find_neighbors(n, (2, 2))

variables_payh(n, key)


# size = 14
# for i in range(1, size):
#     mas.insert(0, 1)
#     row = [mas[x - 1] + mas[x] for x in range(1, len(mas))]
#     mas = row
#     mas.append(1)
# print(sum(row))
