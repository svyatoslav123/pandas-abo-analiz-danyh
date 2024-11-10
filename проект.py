import pandas as pd
df = pd.read_csv("menu (1).csv")




print(df[df['Category']== "Desserts"]["Serving Size"].min())


print(df['Calories'].max())


print(df[df['Category']== "Salads"]["Calories"].min())


print(df[df['Category']== "Smoothies & Shakes"]["Calories"].max())

print(df[df['Category']== "Chicken & Fish"]["Total Fat"].max())



