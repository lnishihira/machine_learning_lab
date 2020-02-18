import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

orders = pd.read_csv("./data/Orders.csv")                                                                        

orders['Profit'] = orders['Profit'].apply(lambda x: float(x.replace('$', '').replace(',','')))                   

orders['Sales'] = orders['Sales'].apply(lambda x: float(x.replace('$', '').replace(',','')))                     

orders['Order.Date'] = pd.to_datetime(orders['Order.Date'], format="%m/%d/%y")
orders['month_year'] = pd.to_datetime(orders['Order.Date']).dt.to_period('M')

orders.groupby('month_year')['Sales'].agg('sum').plot()

categories = orders['Category'].unique()

for category in categories:
    orders.loc[orders['Category']==category].groupby('month_year')['Sales'].agg('sum').plot(label=category)
    plt.ylabel('sales')
    plt.legend()


