import itertools


def alone_char(s):
    for i in s:
        if s[0] != i:
            return False
    return True


def find_repeat_number(num):
    num = f'{num:.60f}'[2:]
    part_text = ''
    max_part_text = ''
    for j in range(0, len(num)//2+1):
        for i in range(j+1, len(num)):
            part1 = num[j:i]
            part2 = num[i:i+i-j]
            if len(part1) != len(part2):
                break
            if part1 == part2:
                part_text = part1
            if len(part_text)>len(max_part_text):
                max_part_text =part_text
    return max_part_text


def test_function(fun, question, ansver):
    if fun(question) == ansver:
        return True
    else:
        return False

for i in range(11, 100):
    res = find_repeat_number(1/i)
    if len(res)>6 and not alone_char(res):
        print(f'{1/i:.60f}',res, i)
print('------------')
