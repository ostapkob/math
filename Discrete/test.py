from itertools import  product as con



t = [True, False]
var = list(con(t, repeat=2))

print(var)

# for p, q in var:
#     print( p, q,'-', not p and (not q), not(p and(not q)), (not p) or q)

sum_ = 0
for n in range(10):
    # o = n*(2*n-1)
    o = (n*(n+1))/2
    sum_ +=n
    print(n, sum_,  o)
