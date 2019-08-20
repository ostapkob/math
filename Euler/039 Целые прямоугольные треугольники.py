from pprint import pprint

def posible_triangle(n):
    ls = []
    st = set()
    for a in range(1, n//2):
        for b in range(1, a):
            c = (a**2+b**2)**(1/2)
            if a+b+c==n:
                angle = [a,b,int(c)]
                angle.sort()
                if angle[0] not in st:
                    st.add(angle[0])
                    ls.append(angle)
    if ls:
        return ls
    else:
        return False


for i in range(1000):

    res = posible_triangle(i)
    if res and len(res)>4:
        print(i, res)
