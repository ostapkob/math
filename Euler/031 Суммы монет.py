def kuzn(n):
    if n <= 1:
        return 1
    else:
        if n>3:
            return kuzn(n-1) + kuzn(n-2) + kuzn(n-3) + kuzn(n-4)
        elif n>2:
            return kuzn(n-1) + kuzn(n-2) + kuzn(n-3)
        else:
            return kuzn(n-1) + kuzn(n-2)

def kuzn(n, ls):
    if n <= 1:
        return 1
    else:
        if n>3:
            return kuzn(n-1, ls) + kuzn(n-2, ls) + kuzn(n-3, ls) + kuzn(n-4, ls)
        elif n>2:
            return kuzn(n-1, ls) + kuzn(n-2, ls) + kuzn(n-3, ls)
        else:
            return kuzn(n-1, ls) + kuzn(n-2, ls)

# coin = [1, 2, 5, 10, 20, 50, 100]
coin = [1, 2, 3, 4]
print(kuzn(5, coin))

