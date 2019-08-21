def is_all_diferent(n):
    n = str(n)
    a = []
    for i in n:
        if i in a:
            return False
        else:
            a.append(i)
    return True


res = 0
start=10_000
stop= 99999
for i in range(start,stop):
    if is_all_diferent(i):
        res += 1
print(res/(stop-start))
