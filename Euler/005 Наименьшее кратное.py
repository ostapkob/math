# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?
def all_simple_number(number):
    mas =False
    for i in range(2,number):
        if number%i==0:
            mas=True
    return mas

def find_all_simple_number(number):
    mas = []
    for i in range(2, number):
        if not all_simple_number(i):
            mas.append(i)
    return mas[::-1]


def is_divided_for_range(number, rangge):
    for i in rangge:
        if number % i != 0:
            return False
    return True

num = 19
i =num


# for el in range(num):
#     print(el, find_all_simple_number(el))

# while not is_divided_for_range(i, find_all_simple_number(num)):
while not is_divided_for_range(i,range(2, num)):
    i +=num
print(i, find_all_simple_number(num))

print('=========')
for r in range(1,20):
    print(i/r, r)