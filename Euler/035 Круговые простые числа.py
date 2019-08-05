from MyFunction import is_prime

def circle(n):
    '''return generator for circle number'''
    n = str(n)
    for i in range(0, len(n)):
        n = n[-1]+n[0:-1]
        yield n

res = 1
for i in range(1, 1000_000):
    if is_prime(i):
        if all(is_prime(int(x)) for x in circle(i)):
            res+=1
print(res)
