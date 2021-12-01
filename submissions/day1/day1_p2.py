from collections import Counter
from itertools import islice

with open('inputs/day1.txt') as file:
    txt = file.read()
    data = tuple(map(int,txt.split(sep='\n')))

counter = Counter()

for idx, val in enumerate(data):    
    if idx >=1:
        if sum(islice(data, idx-1, idx+2)) < sum(islice(data, idx, idx+3)):
            counter.update(['increased'])

    
print(counter)
