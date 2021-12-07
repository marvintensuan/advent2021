from functools import partial

# with open('/inputs/day6.txt') as file:
#     txt = file.read()
#     data = [*map(int, txt.split(','))]

data = [3, 4, 3 ,1 ,2]

days = 18

# g = lambda n, days: (days - (n + 1)) // 7 + 1
# eight = partial(g, n=8)
# f = partial(g,days=days)

def f(n, days):
    return (days - (n + 1)) // 7 + 1

def eight(d):

    no_of_child = d / 8

    if no_of_child <= 1:
        return 1

    return 1 + eight(d - 9)

assert eight(8) == 1
assert eight(9) == 2
assert eight(17) == 2
assert eight(18) == 3

# breakpoint()

children = [f(n, days) + 1 for n in data]
gc = [eight(days - n + 1) for n in data]

print(sum(gc) + sum(children))


# print(sum(children) + sum(grandchildren) + len(data))
breakpoint()