from random import randint, choice, shuffle

def find_empy_seat(seats):
    for i in range(1, len(seats)-1):
        if seats[i]:
            return i
    return 0

SEATS = 101
result = 0
for _ in range(1, 100000):
    seats = [True]*SEATS
    passengers=list(range(1, SEATS))
    shuffle(passengers)
    first = passengers.pop(0)
    rnd = randint(1, SEATS-1)
    seats[rnd] = False

    # print(passengers)
    # print('was', first, 'occupied', rnd)
    # print(seats[0], seats[1:])
    for passenger in passengers:
        last = passenger
        if seats[passenger]:
            seats[passenger] = False
        else:
            rnd =find_empy_seat(seats)
            seats[rnd] = False
        if sum(seats) == 2:
            break
    nxt = next((i for i, j in enumerate(seats[1:], 1) if j), 0)
    if passengers[-1]== nxt:
        result+=1
print(result)
