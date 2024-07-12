import pandas as pd
from pandas import DataFrame
import os

ROOT = os.getcwd()

def read_csv() -> DataFrame:
    df = pd.read_csv(fr"{ROOT}\base_dados\produtos.csv", sep=',')
    return df

def main() -> DataFrame:
    excel = read_csv()
    excel['obs'] = excel['obs'].apply(lambda x: '' if str(x) == "nan" else x)
    return excel