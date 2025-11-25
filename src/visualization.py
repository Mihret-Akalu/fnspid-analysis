import matplotlib.pyplot as plt
import seaborn as sns

class StockVisualizer:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        plt.style.use('seaborn-v0_8')
    
    def plot_basic_analysis(self, symbol: str):
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
        
        # Price and SMA
        ax1.plot(self.data.index, self.data['Close'], label='Close Price', color='black')
        ax1.plot(self.data.index, self.data['SMA_20'], label='SMA 20', alpha=0.7)
        ax1.plot(self.data.index, self.data['SMA_50'], label='SMA 50', alpha=0.7)
        ax1.set_title(f'{symbol} - Price and Moving Averages')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # RSI
        ax2.plot(self.data.index, self.data['RSI_14'], label='RSI 14', color='purple')
        ax2.axhline(70, color='red', linestyle='--', alpha=0.7, label='Overbought (70)')
        ax2.axhline(30, color='green', linestyle='--', alpha=0.7, label='Oversold (30)')
        ax2.set_title('RSI Indicator')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
