from math import sqrt
def triangular_number(num):
    return sum([x for x in range(num+1)])

def divisible_number(num):
    return [x for x in range(1, num+1) if num%x ==0]

def divisible_number2(num):
    nod = 2
    sq = int(sqrt(num))
    for i in range(2, sq):
        if num%i == 0:
            nod+=2
    if sq*sq == num:
        nod -=1
    return nod
# for i in range(1, 100):
#     print( triangular_number(i), ':', len(divisible_number(triangular_number(i))), divisible_number(triangular_number(i)))
# # while True:
#     i+=1
#     if len(divisible_number(triangular_number(i)))>50:
#         print(i,divisible_number(triangular_number(i)))
#         break
c=0
i = 0
while True:
    i+=1
    c+=i
    # if len(divisible_number2(c))>120:
    if divisible_number2(c)>500:
        print(i,divisible_number(c))
        break
