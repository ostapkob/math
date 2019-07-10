# Найдите сумму всех положительных чисел, которые не могут быть
# записаны как сумма двух избыточных чисел
#4179871


from MyFunction import find_all_divisor
import time

def with_perfect(num):
    result = sum(find_all_divisor(num))
    if num < result:  # избыточное
        return 1
    elif num == result:
        return 0
    else:
        return -1

start = time.time()
sum_result = 0
izb_ls = []
for i in range(5000):
    for izb in izb_ls:
        if (i - izb) not in izb_ls:
            sum_result += i
            # print(i, izb_ls)
            break
    if with_perfect(i) == 1:
        izb_ls.append(i)


print(sum_result)
print(time.time()-start  )

