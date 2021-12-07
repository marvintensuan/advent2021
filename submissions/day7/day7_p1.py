
with open('inputs/day7.txt') as file:
    txt = file.read()
    data = [*map(int,txt.split(','))]


targets = list(range(
    min(data),
    max(data) + 1
))

def consumption(src, dest):
    n = abs(dest - src)
    return n * (n + 1) / 2


minima = [
    sum([abs(x - y) for x, y in zip(data, [target]*len(data))])
    for target in targets
]

print(min(minima))