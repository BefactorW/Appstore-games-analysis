import pandas as pd

games = pd.read_csv("appstore_games.csv")
print(games.head())
print(games.shape)
games.info()
print(games.isna().sum())
print(games.describe())
