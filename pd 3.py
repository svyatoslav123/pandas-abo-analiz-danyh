import pandas as pd
df = pd.read_csv("GooglePlayStore_wild (1).csv")
print(df.info())

print(len(df[pd.isnull(df["Rating"])]))
df["Rating"] = df["Rating"].fillna(-1, inplace = True)

def make_size(size):
    if size[-1] == "M":
        return float(size[:-1])
    elif size[-1] == "K":
        return float(size[:-1])/1024
    return -1
df["Size"] = df["Size"].apply(make_size)
print(df[df("Category")] == 'TOOLS')


df["Price"]