def is_Pandigital(n):
    if len(str(n))!=9:
        return False
    else:
        a = [int(x) for x in str(n)]
        a.sort()
        if a == [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return True
        else:
            return False

def combine_pdroduct_numbers(n):
    s = ''
    i=1
    while len(str(s))<9:
        s+=str(n*i)
        i+=1
    return s, i


for i in range(9999, 1, -1):
    res = combine_pdroduct_numbers(i)
    if is_Pandigital(res[0]):
        print(res, i)
        break

