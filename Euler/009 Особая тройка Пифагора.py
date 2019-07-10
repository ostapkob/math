# Тройка Пифагора - три натуральных числа a < b < c, для которых выполняется равенство
# a2 + b2 = c2
# Например, 32 + 42 = 9 + 16 = 25 = 52.
# Существует только одна тройка Пифагора, для которой a + b + c = 1000.
# Найдите произведение abc.
import time


def is_trio(a, b, c):
    if a**2 + b**2 == c**2 and a < b and b < c:
        return True
    return False
start = time.time()
flag = False
for a in range(1, 1000):
    for b in range(a, 1000):
        for c in range(b, 1000):
            if is_trio(a, b, c) and a + b + c == 1000:
                print(a, b, c)
                flag = True
                break
        if flag:
            break
    if flag:
        break
print(time.time() - start)
