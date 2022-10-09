import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import missingno as msno
from pandas import DataFrame
import re
import warnings
warnings.filterwarnings("ignore")

class DataRow:
    def __init__(self, year, measurement, source):
        self.year = year
        self.measurement = measurement
        self.source = source
        self.diff = ""

diffs = {}

input_df = pd.read_csv("us_emissions.csv", delimiter=',', decimal=".")
all_rows = []
for index, row in input_df.iterrows():
    data_row = DataRow(row["YEAR"], row["MEASUREMENT"], row["SOURCE"])
    all_rows.append(data_row)
    if data_row.year == 1970:
        diffs[data_row.source] = [data_row.measurement]
    elif data_row.year == 2019:
        diffs[data_row.source].append(data_row.measurement)

for source, value in diffs.items():
    diffs[source] = abs(round((1 - value[1]/value[0])*100, 2))
    if diffs[source] < 100:
        diffs[source] = "-" + str(diffs[source]) + "%"
    else:
        diffs[source] = "+" + str(diffs[source]) + "%"

df = DataFrame(columns = ["YEAR", "MEASUREMENT", "SOURCE", "DIFF"])
for row in all_rows:
    new_row = [row.year, row.measurement, row.source, diffs[row.source] + " (from 1970 to 2019)"]
    df.loc[len(df)] = new_row

df.to_csv('us_emissions_diffed.csv', index=False)
