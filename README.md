# App Store Strategy Games: Data Analysis

Exploratory analysis of ~17,000 strategy games from the Apple App Store using
Python and pandas.

## Data

[17K Mobile Strategy Games](<https://www.kaggle.com/datasets/tristan581/17k-apple-app-store-strategy-games?resource=download>) on Kaggle, by <Tristan>,
licensed under CC BY 4.0. The data was collected on 3 August 2019, so
2019 is a partial year. Download `appstore_games.csv` and put it in the `data/`
folder (it is not included in this repository).

## Questions and findings

**Who published the most games?**
Tapps Tecnologia da Informação Ltda. (123 games), Vikash Patel (107) and
Netsummit Marketing (95).

**How many games were released each year?**
Releases grew from 47 in 2008 to a peak of 3,126 in 2016 and fell afterwards.
2019 (1,570 games) covers only January–August.

**Are free games rated higher than paid ones?**
About 84% of games are free (14,212 vs 2,795). Average ratings are very close:
4.07 for free and 4.01 for paid. Free games get about twice as many ratings
(3,602 vs 1,796 on average). Rating coverage is the same in both groups (~44%).

**Which genres are rated best?**
96% of titles have "Games" as the primary genre. Among genres with more than 20
rated apps: Sports (4.22), Education (4.15), Games (4.07), Utilities (4.06),
Entertainment (3.83).

**Which games are the best?**
Among games with more than 1,000 ratings and a 5.0 average, the most rated are
Cash, Inc. (374,772 ratings), Egg, Inc. (174,591) and AFK Arena (156,766).

## Data quality notes

- Only ~44% of games (7,561 of 17,007) have a rating, so rating analysis uses
  rated games only.
- Ratings are rounded to 0.5, so many games tie at 5.0; ties were broken by the
  number of ratings.
- Some names contain escaped characters (for example `\xe7\xe3`, `\u2122`).

## How to run

```bash
pip install -r requirements.txt
python 02_questions.py
```