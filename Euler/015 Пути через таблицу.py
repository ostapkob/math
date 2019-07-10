size = 20
mas = [1]
for i in range(1,size):
    mas.insert(0, 1)
    row = [mas[x-1] + mas[x] for x in   range(1,len(mas))]
    mas = row
    mas.append(1)
print(row)
print(row[int(size/2)-1])
