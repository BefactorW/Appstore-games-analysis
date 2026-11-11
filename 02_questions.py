import pandas as pd

games = pd.read_csv("data/appstore_games.csv")
games["Original Release Date"] = pd.to_datetime(games["Original Release Date"], dayfirst=True)
games["Is Free"] = games["Price"] == 0

print("1. Top 10 developers by number of games")
print(games["Developer"].value_counts().head(10))
print()

print("2. Games released per year")
print(games["Original Release Date"].dt.year.value_counts().sort_index())
print()

print("3. Free vs paid games")
print("Number of games:")
print(games.groupby("Is Free").size())
print("Average number of ratings:")
print(games.groupby("Is Free")["User Rating Count"].mean())
print("Average rating:")
print(games.groupby("Is Free")["Average User Rating"].mean())
total = games.groupby("Is Free").size()
rated = games.groupby("Is Free")["Average User Rating"].count()
print("Share of games that have a rating:")
print(rated / total)
print()

print("4. Genres (only genres with more than 20 rated games)")
genre_stats = games.groupby("Primary Genre")["Average User Rating"].agg(["mean", "count"])
print(genre_stats[genre_stats["count"] > 20].sort_values("mean", ascending=False))
print()

print("5. Top 10 games with more than 1000 ratings")
popular_games = games[games["User Rating Count"] > 1000]
best_games = popular_games.sort_values(["Average User Rating", "User Rating Count"], ascending=False)
print(best_games.head(10)[["Name", "Average User Rating", "User Rating Count"]])


