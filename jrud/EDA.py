import pandas as pd

orders = pd.read_csv("./data/Orders.csv")                                                                        

orders['Profit'] = orders['Profit'].apply(lambda x: float(x.replace('$', '').replace(',','')))                   

orders['Sales'] = orders['Sales'].apply(lambda x: float(x.replace('$', '').replace(',','')))                     

