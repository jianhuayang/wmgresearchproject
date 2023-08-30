import pandas as pd

df = pd.read_csv("video_data.csv", index_col=0)
print(df.head())