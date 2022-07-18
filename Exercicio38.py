N = int(input())
for n in range(N):
    one_positions = list()
    for index, number in enumerate(input()):
        if int(number):
            one_positions.append(index)
    dif = map(lambda x, y: y - x - 1, one_positions[:-1], one_positions[1:])
    print(sum(filter(lambda x: x != 0, dif)))