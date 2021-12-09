import pandas as pd
from numpy import NaN

with open('inputs/day9_testcase.txt') as file:
    txt = file.read()
    data = [ [*map(int, line)] for line in txt.split('\n') ]


data = pd.DataFrame(data)

def check_downs(df: pd.DataFrame)-> pd.DataFrame:
    df = df.append([NaN], ignore_index=True)

    return pd.DataFrame([
        [True] * len(df.loc[i])
        if df.loc[i + 1].dropna().empty
        else list((df.loc[i] - df.loc[i + 1]) < 0)
        for i in df.index[:-1]
    ])

def check_ups(df: pd.DataFrame)-> pd.DataFrame:
    df.loc[-1] = [NaN] * len(df.loc[0])
    df = df.sort_index().reset_index(drop=True)

    return pd.DataFrame([
        [True] * len(df.loc[i])
        if df.loc[i].dropna().empty
        else list((df.loc[i] - df.loc[i - 1]) < 0)
        for i in df.index[:-1]
    ])

def check_lefts(df: pd.DataFrame)-> pd.DataFrame:
    ...

def check_rights(df: pd.DataFrame)-> pd.DataFrame:
    ...


map = check_lefts(data) & check_rights(data) & check_ups(data) & check_downs(data)


breakpoint()