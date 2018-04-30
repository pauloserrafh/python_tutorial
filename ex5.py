import pandas as pd
import numpy as np


def series_to_list():
    ds = pd.Series([2, 4, 6, 8, 10])
    print(ds)
    print(type(ds))
    conv = ds.tolist()
    print(conv)
    print(type(conv))

def compara():
    ds1 = pd.Series([2, 4, 6, 8, 10])
    ds2 = pd.Series([1, 3, 5, 7, 10])
    print("Soma:")
    print(ds1 + ds2)
    print("Subtração:")
    print(ds1 - ds2)
    print("Maior que:")
    print(ds1 > ds2)

if __name__ == '__main__':
    # series_to_list()
    compara()