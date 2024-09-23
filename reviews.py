import pandas as pd 
import numpy as np
import zipfile
import os 
pd.set_option('display.max_rows', 5)
df = pd.read_csv('data/winemag-data-130k-v2.csv.zip',index_col=0)
summary = df.groupby('country').agg(
    count = ('country', 'size'),
    points = ('points', 'mean'))
summary.sort_values(by=['count'], inplace=True, ascending=False)
summary = summary.round(1)
print(summary)
# write the new summary to a new csv file
summary.to_csv('data/reviews-per-country.csv')

print("Summary data has been written to 'reviews-per-country.csv'")
