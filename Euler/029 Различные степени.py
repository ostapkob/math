m=101
comb =dict.fromkeys([(a**b) for a in range(2, m) for b in range(2, m)])
print(len(comb))
