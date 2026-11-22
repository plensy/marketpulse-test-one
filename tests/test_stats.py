import pytest
from marketpulse.stats import simple_returns, max_drawdown

def test_returns():
    assert simple_returns([100, 110]) == pytest.approx([0.10])

def test_returns_needs_two_prices():
    with pytest.raises(ValueError):
        simple_returns([100])

def test_drawdown():
    assert max_drawdown([100, 120, 90, 130]) == pytest.approx(-0.25)

def test_no_drawdown_when_prices_only_rise():
    assert max_drawdown([1, 2, 3]) == 0.0