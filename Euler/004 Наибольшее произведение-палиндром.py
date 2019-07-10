# Число-палиндром с обеих сторон (справа налево и слева направо) читается одинаково.
# Самое большое число-палиндром, полученное умножением двух двузначных чисел – 9009 = 91 × 99.
# Найдите самый большой палиндром, полученный умножением двух трехзначных чисел.


def len_x(c):
    rez = 0
    while c:
        c = c // 10
        rez += 1
    return rez


def del_fist_and_last(x):
    ln = len_x(x)
    rez1 = x - (x // 10 ** (ln - 1)) * (10 ** (ln - 1))
    return rez1 // 10


def is_palendrom(c):
    c = str(c)
    while len(c)>1:
        if c[0]!=c[-1]:
            return False
        c = c[1:-1]
    return True
ch = []
max_palendrom=1
for i in range(100, 1000):
    for j in range(100, 1000):
        if is_palendrom(j*i):
            if j*i>max_palendrom:
                max_palendrom=j*i
                ch = [i,j]


print(max_palendrom, ch)




