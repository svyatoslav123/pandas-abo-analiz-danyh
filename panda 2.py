import pandas as pd


df = pd.read_csv("GoogleApps (3).csv")
print(df.groupby(by = 'Type')['Rating'].agg(['min','median',max]))
temp = df.pivot_table(index = "Content Rating", columns = 'Category', )