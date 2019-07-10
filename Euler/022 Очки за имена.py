def count_txt(txt):
    abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num = range(1, len(abc)+1)
    abc_num = dict(zip(abc, num))
    sum_abc = 0
    for t in txt:
        sum_abc+=abc_num[t]
    return sum_abc


with open('p022_names.txt') as f:
    names = []
    for line in f:
        for word in line.split(','):
            names.append(word[1:-1])
names.sort()
sum_count = 0
for name in names:
    sum_count +=count_txt(name)
    print(count_txt(name), name)
print(sum_count)
