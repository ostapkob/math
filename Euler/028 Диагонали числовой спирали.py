def sum_anle_not_even(num):
    sum_angle = num_exp
    for _ in range(3):
        sum_angle += num**2-num-1
    return sum_angle
print(sum([sum_anle_not_even(x) for x in range(1001, 1, -2)]))
