import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from pandas import DataFrame
import re
import warnings
warnings.filterwarnings("ignore")

class Source:
    def __init__(self, name):
        self.name = name
        self.data = []

input_df = pd.read_excel("us_emissions_formatted.xlsx")
df = DataFrame(columns = ["YEAR", "MEASUREMENT", "SOURCE"])
for index, row in input_df.iterrows():
    name = row["Source"]
    source = Source(name)
    for year in [1970, 1975, 1980, 1985] + list(range(1990, 2020)):
        new_row = [year, round(row[year], 3), name]
        df.loc[len(df)] = new_row

df.to_csv('us_emissions.csv', index=False)
