import csv

from src.marketpulse.stats import max_drawdown, simple_returns

with open("data/prices.csv") as f:
    prices = [float(row["close"]) for row in csv.DictReader(f)]

print(f"last return : {simple_returns(prices)[-1]:+.2%}")
print(f"max drawdown: {max_drawdown(prices):.2%}")
