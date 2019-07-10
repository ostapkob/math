from MyFunction import len_x, char_to_list
import itertools


def permutation_number(num):
    chars = char_to_list(num)
    return chars


n =123456789
# print(permutation_number(n))
n1 = '1234'
n2 = '1234'
iter1 =list(map(lambda x: int(''.join(x)),(itertools.permutations(n1, len(n1)))))
iter2 =list(map(lambda x: int(''.join(x)),(itertools.permutations(n2, len(n2)))))
difference = []
for en, i  in enumerate(iter1):
    if en==0:
        continue
    # print((iter1[en] - iter1[0]))
    difference.append(iter1[en] - iter1[0])
print(difference)
difdif=[]
for en, i  in enumerate(difference):
    if en==0:
        continue
    # print((iter1[en] - iter1[0]))
    difdif.append(difference[en] -difference[en-1])
print(difdif)
print(itertools.islice.__doc__)
