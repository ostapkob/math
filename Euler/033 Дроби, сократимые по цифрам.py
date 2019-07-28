def find_similar_number(z, d):
    z0 = int(list(str(z))[0])
    z1 = int(list(str(z))[1])
    d0 = int(list(str(d))[0])
    d1 = int(list(str(d))[1])
    if z0 == d1 and z1/d0 == z/d:
            return z, d
    return False

n = 99
drobs = [(x, y) for x in range(10, n) for y in range(10, x)]

sum_d = 1
sum_z = 1
for z, d in drobs:
    if find_similar_number(z, d):
        sum_d*=d
        sum_z*=z
        print(z, d)

print(sum_z, sum_d)



