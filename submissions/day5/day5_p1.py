from collections import Counter

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

    axis = dx if dx else dy

    stop_at, step = stopstep[axis > 0]
    rng = range(0, stop_at(axis), step)

    return [
        f"{x1 + i}, {y1}"
        if dx else f"{x1}, {y1 + i}"
        for i in rng
    ]


if __name__ == '__main__':

    lines = [*filter(
        lambda line: (line[0][0] == line[1][0]) or (line[0][1] == line[1][1]),
        lines)
    ]

    board = Counter()

    for src, dest in lines:
        coords = create_path(src, dest)

        board.update(coords)

    at_least_two = len([key for key, value in board.items() if value >=2])
    print(at_least_two)