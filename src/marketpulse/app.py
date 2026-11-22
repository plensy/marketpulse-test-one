import csv
import os
from pathlib import Path

from dash import Dash, html

from marketpulse.stats import max_drawdown, simple_returns

VERSION = os.getenv("APP_VERSION", "dev")
DATA = Path(__file__).resolve().parents[2] / "data" / "prices.csv"


def load_prices() -> list[float]:
    with open(DATA) as f:
        return [float(row["close"]) for row in csv.DictReader(f)]


prices = load_prices()

app = Dash(__name__)
server = app.server  # used by gunicorn

app.layout = html.Div(
    [
        html.H1(f"MarketPulse {VERSION}"),
        html.P(f"Last return: {simple_returns(prices)[-1]:+.2%}"),
        html.P(f"Max drawdown: {max_drawdown(prices):.2%}"),
    ]
)

if __name__ == "__main__":
    app.run(debug=True)
