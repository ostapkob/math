def gcd(a,b):
    while a!=0 and b!=0:
        if a>b:
            a=a%b
        else:
            b%=a
    return a+b


def nod_f(a, b):
    n_max = 0
    rez_max=0
    for n in range(1, 10**6):
        rez = gcd(n**3 +b, ((n+a)**3)+b)
        if rez>rez_max:
            n_max=n
            rez_max=rez
    return n_max, rez_max


print(nod_f(5,5))

print(gcd(36,24))
