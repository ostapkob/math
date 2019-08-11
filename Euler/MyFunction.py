def print_lists(list_of_list, round_digit=2):
    mm = 0
    for i in list_of_list:
        mm = max(mm, len(i))
    maxl = [0]*mm
    for i in list_of_list:
        for n, j in enumerate(i):
            if type(j) == int or type(j) == float:
                j = round(j, round_digit)
            maxl[n] = max(maxl[n], len(str(j)))
    for i in list_of_list:
        for n, j in enumerate(i):
            if type(j) == int or type(j) == float:
                j = round(j, round_digit)
            print(str(j).ljust(maxl[n]), end=' | ')
        print()

def is_prime(n):
    '''Check is number simple'''
    n = int(n)
    if n % 2 == 0:
        return False
    d = 2
    while d <= n**(1/2) and n % d != 0:
        d += 1
    return d <= n and n % d != 0

def len_x(c):
    rez = 0
    while c:
        c = c // 10
        rez += 1
    return rez


def dec_find_max(fun):
    def wrapper(n=0):
        return fun(n)*2
    return wrapper


def sum_char(n):
    i = 0
    s = 0
    while i < len_x(n):
        i += 1
        s += (n % 10**i-(n % 10**(i-1)))/10**(i-1)
    return int(s)


def find_all_divisor(num):
    return [x for x in range(1, num) if num % x == 0]


def char_to_list(n):
    i = len_x(n)
    s = []
    while i > 0:
        s.append(int((n % 10**i-(n % 10**(i-1)))/10**(i-1)))
        i -= 1
        return s


def list_to_list_accumulation(ls):
    new = []
    new.append(ls[0])
    for en, i in enumerate(ls[1:], 1):
        new.append(new[en-1]+ ls[en])
        nw = [x-1 for en, x in enumerate(new)]
    return nw


def divided_parts(mas: list, n):
    mas.sort()
    result = []
    tmp = []
    part = len(mas)//n
    mod = len(mas)%n
    len_mas = len(mas)
    fun = lambda e: part+1 if e < mod else part
    quantity_elements=[fun(x)  for x in range(n)]
    numbers_col = list_to_list_accumulation(quantity_elements)
    numbers_col.append(0)
    id_col = 0
    for en, el in enumerate(mas, -1):
        if en == numbers_col[id_col]:
            result.append(tmp)
            tmp = []
            id_col+=1
        tmp.append(el)
    result.append(tmp)
    return  result
# import random
# n = [random.randint(0, 200) for _ in range(31)]
# n.sort()
# print(n)
# print_lists(divided_parts1(n, 7))

