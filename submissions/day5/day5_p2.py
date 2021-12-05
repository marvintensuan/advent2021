from collections import Counter
from itertools import zip_longest

with open('inputs/day5.txt') as file:
    txt = file.read()
    lines = txt.split(sep='\n')

lines = [
    [tuple(map(int, item.split(',')))
    for item in line.split('->')]
    for line in lines
]

def create_path(src, dest) -> list:
    x1, y1 = src
    x2, y2 = dest

    dx = x2 - x1
    dy = y2 - y1

    stopstep = {
        True: ((lambda x: x + 1), 1) ,
        False: ((lambda x: x - 1), -1)
    }

    stop, step = stopstep[dx > 0]
    rngx = range(0,stop(dx), step)

    stop, step = stopstep[dy > 0]
    rngy = range(0, stop(dy), step)

    return [
        f"{x1 + i}, {y1 + j}"
        if dx else f"{x1 + i}, {y1 + j}"
        for i,j in zip_longest(rngx, rngy, fillvalue=0)
    ]


if __name__ == '__main__':

    board = Counter()

    for src, dest in lines:
        coords = create_path(src, dest)

        board.update(coords)

    at_least_two = len([key for key, value in board.items() if value >=2])
    print(at_least_two)