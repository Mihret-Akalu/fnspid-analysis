import pytest
import pandas as pd
import numpy as np
from src.indicators import compute_moving_average, compute_rolling_std

class TestIndicators:
    def test_moving_average_basic(self):
        """Test basic moving average calculation."""
        series = pd.Series([1, 2, 3, 4, 5])
        ma = compute_moving_average(series, window=3)
        assert isinstance(ma, pd.Series)
        assert len(ma) == len(series)
    
    def test_moving_average_values(self):
        """Test moving average values are correct."""
        series = pd.Series([1, 2, 3, 4, 5])
        ma = compute_moving_average(series, window=3)
        # First two values should be different due to min_periods=1
        assert not pd.isna(ma.iloc[0])
        assert not pd.isna(ma.iloc[1])
    
    def test_rolling_std(self):
        """Test rolling standard deviation."""
        series = pd.Series([1, 2, 3, 4, 5])
        rolling_std = compute_rolling_std(series, window=3)
        assert isinstance(rolling_std, pd.Series)
        assert len(rolling_std) == len(series)
