from pprint import pprint


def find_neighbors(el):
    x, y = el[0], el[1]
    return (x + 1, y), (x + 1, y + 1)


def variables_path(el_key=(0, 0), val=[]):
    global keys
    val.append(el_key)
    print(val)
    if len(val) > 4:
        print(val)
        return val
    else:
        r, l = find_neighbors(el_key)
        variables_path(r, val)
        variables_path(l, val)


n = [[75],
     [95, 64],
     [17, 47, 82],
     [18, 35, 87, 10]]
keys = [[(y, x) for x in range(y+1)] for y in range(len(n))]
pprint(keys)
# print(find_neighbors((2,1)))
# print('='*39)
print(variables_path())
for key in keys:
    for k in key:
        pass
        # print(find_neighbors(k))
