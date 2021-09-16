import pandas as pd

data = [{"id": 1, "color": "b"},
        {"id": 2, "color": "r"}]

df = pd.DataFrame.from_records(data)

df.replace(["b", "r"], ["blue", "red"], inplace=True)
