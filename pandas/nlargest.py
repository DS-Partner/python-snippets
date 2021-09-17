# Get top N (10) records by 'Income'

import pandas as pd

df = pd.read_csv("../data/customers.csv")

df.nlargest(10, 'Income')
