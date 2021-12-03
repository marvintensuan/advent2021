import numpy as np

with open('inputs/day3.txt') as file:
    txt = file.read()
    data = tuple(map(str,txt.split(sep='\n')))

transposed = np.array([list(s) for s in data]).transpose().astype('int32')


gamma = ''
epsilon = ''

for position in transposed:
    t = (sum(position)/len(position) > 0.5)
    gamma += '1' if t else '0'
    epsilon += '1' if not t else '0'

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma * epsilon)