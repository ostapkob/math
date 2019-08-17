def is_palindrom(n):
    sn=str(n)
    if len(sn)%2==0:
        for i in range(1, int(len(sn)/2)+1):
            if sn[i-1] != sn[-i]:
                return False
        return True
    else:
        return False

for num in range(1000000):
    numb = str(bin(num))[2:]
    if is_palindrom(num) and is_palindrom(numb):
        print(num, numb)
