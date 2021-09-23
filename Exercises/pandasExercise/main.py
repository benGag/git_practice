import pandas as pd

d1 = {
    "Id": [1, 2, 3],
    "Product": ["table", "chair", "window"],
    "Price": [200, 150, 800]}

d2 = {
    "Id": [4, 5, 6],
    "Name": ["Michi", "Peter", "Lola"],
    "Wohnort": ["Berlin", "Wien", "Amsterdam"]}

df1 = pd.DataFrame(d1)
df2 = pd.DataFrame(d2)

df1.merge(df2='key', how='inner')

print(df1)

