import pandas as pd
import talib

class TechnicalIndicators:
    def __init__(self, data: pd.DataFrame):
        self.data = data.copy()
    
    def calculate_all_indicators(self) -> pd.DataFrame:
        # Moving Averages
        self.data['SMA_20'] = talib.SMA(self.data['Close'], timeperiod=20)
        self.data['SMA_50'] = talib.SMA(self.data['Close'], timeperiod=50)
        
        # RSI
        self.data['RSI_14'] = talib.RSI(self.data['Close'], timeperiod=14)
        
        # MACD
        self.data['MACD'], self.data['MACD_Signal'], self.data['MACD_Hist'] = talib.MACD(
            self.data['Close'], fastperiod=12, slowperiod=26, signalperiod=9
        )
        
        print(" All technical indicators calculated")
        return self.data
