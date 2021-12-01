from collections import Counter
from itertools import zip_longest

with open('inputs/day1.txt') as file:
    txt = file.read()
    data = tuple(map(int,txt.split(sep='\n')))

counter = Counter()

for cur, next in zip_longest(data, data[1:], fillvalue=0):
    if cur < next:
        counter.update(['increased'])

print(counter)
