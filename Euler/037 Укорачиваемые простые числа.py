from MyFunction import is_prime

def is_prime_all_circle_dell(n):
    sn = str(n)
    for i in range(1, len((sn))):
        if not is_prime(int(sn[:i])) or is_prime(int(sn[i:])):
            return False
    return True

for i in range(10000, 100000):
    if is_prime(i):
        if is_prime_all_circle_dell(i):
            print(i)
