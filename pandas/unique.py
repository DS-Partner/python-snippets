# Get the unique values from a feature

import pandas as pd

df = pd.read_csv("../data/customers.csv")

df.Prefix.unique()
