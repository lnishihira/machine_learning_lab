import pandas as pd
import matplotlib.pyplot as plt
import datetime as dt

df = pd.read_csv("data/Orders.csv")
returns = pd.read_csv("data/Returns.csv")


cols = df.columns.to_list()
cols = [col.lower() for col in cols]
cols = [col.replace(".","_") for col in cols]

r_cols = returns.columns.to_list()
r_cols = [col.lower() for col in r_cols]
r_cols = [col.replace(" ","_") for col in r_cols]

df.columns = cols
returns.columns = r_cols

# clean profit col and sales col
df.profit = df.profit.str.replace("$", "")
df.profit = df.profit.str.replace(",", "")
df.profit = df.profit.astype(float)

df.sales = df.sales.str.replace("$", "")
df.sales = df.sales.str.replace(",", "")
df.sales = df.sales.astype(float)

# make into datetime
df.order_date = pd.to_datetime(df.order_date, format='%m/%d/%y')  

#df['order_date'] = pd.to_datetime(df['order_date'], format="%m/%d/%y")
df['month_year'] = pd.to_datetime(df['order_date']).dt.to_period('M')

df.groupby('month_year')['sales'].agg('sum').plot()

categories = df['category'].unique()

for category in categories:
    df.loc[df['category']==category].groupby('month_year')['sales'].agg('sum').plot(label=category)
    plt.ylabel('sales')
    plt.legend()



returned_df = pd.merge(df, returns, on = "order_id", how = "inner")

returns_by_customer = returned_df.groupby('customer_id').agg({'profit':'sum', 'order_id':'count'}) 

repeat_returns = returns_by_customer.groupby('order_id').count() 

returned_by_subcat = returned_df.groupby('sub_category').agg({'profit':'sum', 'order_id':'count'}

#machine learning
returned_df.returned.fillna("No",inplace=True) 

