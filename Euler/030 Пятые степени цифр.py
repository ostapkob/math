from functools import reduce


def pows(num, p=4):
    st = list(''.join(str(num)))
    fc = lambda x: int(x)**p
    res = sum([fc(x) for x in  st])
    if res == num:
        return True
    else:
        return False

summ = 0
for i in range(2, 999999):
    if pows(i, 5):
        print(i)
        summ +=i
print(summ, '==')
