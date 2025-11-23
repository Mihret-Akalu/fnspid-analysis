import pandas as pd

def compute_moving_average(series: pd.Series, window: int = 7) -> pd.Series:
    """
    Compute moving average of a time series.
    Useful for smoothing article frequency or sentiment trends.
    
    Args:
        series (pd.Series): Time series data
        window (int): Rolling window size
        
    Returns:
        pd.Series: Moving average series
    """
    return series.rolling(window=window, min_periods=1).mean()

def compute_rolling_std(series: pd.Series, window: int = 7) -> pd.Series:
    """
    Compute rolling standard deviation for volatility analysis.
    
    Args:
        series (pd.Series): Time series data
        window (int): Rolling window size
        
    Returns:
        pd.Series: Rolling standard deviation
    """
    return series.rolling(window=window, min_periods=1).std()