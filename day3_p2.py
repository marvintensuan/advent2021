import numpy as np

with open('inputs/day3.txt') as file:
    txt = file.read()
    data = tuple(map(str,txt.split(sep='\n')))

def recurse(data, pos=0, recurse_fewer=False):
    transposed = np.array([list(s) for s in data]).transpose().astype('int32')

    if len(data) == 1:
        return data.pop()

    digit = '1' if sum(transposed[pos])/len(transposed[pos])>= 0.5 else '0'


    if not recurse_fewer:
        return recurse([i for i in data if i[pos]==digit], pos=pos+1, recurse_fewer=recurse_fewer)
    else:
        return recurse([ i for i in data if i[pos]!=digit], pos=pos+1, recurse_fewer=recurse_fewer)


x = recurse(data)
y = recurse(data, recurse_fewer=True)

print(int(x,2) * int(y,2))
