from collections import Counter

with open('../inputs/day6.txt') as file:
    txt = file.read()
    data = [*map(int, txt.split(','))]

days = 256 # Part 1: 80, Part 2: 256

for day in range(days):

    data = [ i - 1 for i in data ]

    if -1 in data:
        c = Counter(data)

        data += [8] * c[-1]
        data = [ i if i != -1 else 6 for i in data ]

    # breakpoint()
print(len(data))