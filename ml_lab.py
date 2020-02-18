import pandas as pd

df = pd.read_csv("Orders.csv")
df.columns
df.columns.to_list()
cols = df.columns.to_list()
cols = [col.lower() for col in cols]
cols = [col.replace(".","_") for col in cols]
df.columns = cols

# clean profit col
df.profit = df.profit.str.replace("$", "")
df.profit = df.profit.str.replace(",", "")
df.profit = df.profit.astype(float)

df.sales = df.sales.str.replace("$", "")
df.sales = df.sales.str.replace(",", "")
df.sales = df.sales.astype(float)

