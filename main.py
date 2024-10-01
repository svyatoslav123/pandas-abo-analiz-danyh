import pandas as pd
df = pd.read_csv("GoogleApps (3).csv")


print(df[df["Content Rating"] == ""]['Installs'].min())
free =df[df["Content Rating"] == "Free"]['Reviews'].max()
paid =df[df["Content Rating"] == "Paid"]['Reviews'].max()
print(free - paid)