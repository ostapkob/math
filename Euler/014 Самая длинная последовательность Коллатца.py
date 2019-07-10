from MyFunction import find_max

def test(n):
    return n*n

def colac(n, i=0):
    if n ==1:
        return i
    elif n%2 == 0:
        return colac(n/2, i=i+1)
    else:
        return colac(n*3+1, i=1+i)

print(test(4))


# for i in range(105,  120):
#     print(i, colac(i))












