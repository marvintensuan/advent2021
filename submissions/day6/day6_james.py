from csv import reader
from pandas import Series, DataFrame
from numpy import arange, roll
from itertools import islice

def process(pop):
    while True:
        yield pop.copy()
        spawning, pop.loc[0] = pop.loc[0], 0
        pop.index = roll(pop.index, 1)
        pop.loc[6] += spawning
        pop.loc[8] += spawning

with open('inputs/day6.txt') as f:
    init_pop = [int(x) for x in next(reader(f))]
    init_pop = Series(init_pop)
    init_pop = init_pop.value_counts().reindex(arange(9), fill_value=0)

populations = (
    DataFrame.from_records([
        pop for pop in islice(process(init_pop), 256+1)
    ])
    .rename_axis('day', axis='index')
    .rename_axis('lifetime', axis='columns')
)

print(
    populations.loc[80].sum(),
    populations.loc[256].sum(),
    sep='\n',
)