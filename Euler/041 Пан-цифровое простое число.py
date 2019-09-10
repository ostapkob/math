from MyFunction import tuple_to_int, is_prime
from itertools import permutations

num = 7
max_res = 0
for i in permutations(range(1,num+1), num):
    ch = tuple_to_int(i)
    if is_prime(ch):
       max_res= ch

print(max_res)

