import pandas as pd

data = pd.read_csv("squirrel_data.csv")
counts = data["Primary Fur Color"].value_counts()

data_dict = 
counts = pd.DataFrame(counts)
counts.to_csv("counts_by_color.csv")

print(counts)