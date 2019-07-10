# Найдите произведение коэффициентов a и b квадратичного выражения, согласно которому можно получить максимальное количество простых чисел для последовательных значений n, начиная со значения n=0.
# n2+an+b, где |a|<1000 и |b|≤1000
<<<<<<< HEAD
=======
import math

>>>>>>> 82f961989e40644d98ee3f22d55b82192d41efbb

def range_simple_number(n, a, b):
    return n*n + a*n + b


def is_simple(num):
<<<<<<< HEAD
    for i in range(3, num, 1):
        if num%i==0:
=======
    if num % 2 == 0:
        return False
    for i in range(3, round(math.sqrt(abs(num)))+2, 2):
        if num % i == 0:
>>>>>>> 82f961989e40644d98ee3f22d55b82192d41efbb
            return False
    return True


<<<<<<< HEAD
r = [n for n in range(3, 100) if  is_simple(n)]
for n in range(100):
    for a in range(100):
        for b in range(100):
            if is_simple(range_simple_number(n, a, b)):
                print(range_simple_number(n, a, b))


=======
def len_simlple_range(ab):
    a,b = ab
    ls_simlpe = []
    for n in range(ch):
        res = range_simple_number(n, a, b)
        if is_simple(res):
            ls_simlpe.append(res)
        else:
            break
    return len(ls_simlpe)


r = [n for n in range(3, 100) if is_simple(n)]
# print(r)
ch = 1000
for a in range(-ch, ch):
    for b in range(-ch, ch):
        pass
        ab= a,b
        res = len_simlple_range(ab)
        if res > 60:
            print(res, *ab)
ans = max(((a, b) for a in range(-ch, ch)
           for b in range(2, ch)), key=len_simlple_range) # if you want search value for key then need use one element
print('ansver =', ans)
>>>>>>> 82f961989e40644d98ee3f22d55b82192d41efbb
