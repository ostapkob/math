from MyFunction import find_all_divisor
s = 0
for i in range (1000):
    a = sum(find_all_divisor(i))
    if sum(find_all_divisor(a))==i:
        print(i,a)
        s +=i
print(s)


