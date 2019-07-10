def len_x(c):
    rez = 0
    while c:
        c = c // 10
        rez += 1
    return rez


def sum_char(n):
    i = 0
    s = 0
    while i<len_x(n):
        i+=1
        s+=(n%10**i-(n%10**(i-1)))/10**(i-1)
    return int(s)


num = 2**1000
print(num)
print(sum_char(num))
