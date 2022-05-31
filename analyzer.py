import os
import pandas as pd
from fileinput import filename
print("-"*7)
print(*[filename.split(".")[0] for filename in os.listdir("./opinions/")], sep="\n")
print("-"*7)

product_id = input('Please enter a product\'s id: ')


opinions = pd.read_json(f"opinions/{product_id}.json")

opinions_count = len(opinions)
pros_count = opinions["pros"].map(bool).sum()
cons_count = opinions["cons"].map(bool).sum()
average_score = opinions["score"].mean().round(2)

stars_recommendation = pd.crosstab(opinions["rcmd"], opinions["score"], dropna=False)
print(stars_recommendation)
