import itertools


def variants_mathes(n):
    ls = list(range(1, n+1))
    variants = list(itertools.permutations(ls, len(ls)))
    count = 0
    for variant in variants:
        for en, var in enumerate(variant, 1):
            if en == var:
                count += 1
                break
    return 1-(count/len(variants))


for i in range(2, 11):
    print(i, variants_mathes(i))
