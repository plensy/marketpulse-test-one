def simple_returns(prices: list[float]) -> list[float]:
    """Daily returns: p[t] / p[t-1] - 1."""
    if len(prices) < 2:
        raise ValueError("need at least two prices")
    return [p1 / p0 - 1 for p0, p1 in zip(prices, prices[1:])]


def max_drawdown(prices: list[float]) -> float:
    """Worst fall from a previous peak, as a negative number."""
    peak, worst = prices[0], 0.0
    for p in prices:
        peak = max(peak, p)
        worst = min(worst, p / peak - 1)
    return worst