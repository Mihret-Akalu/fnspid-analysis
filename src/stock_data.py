import pandas as pd
import os
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

class StockDataLoader:
    """
    Load and prepare stock price data from CSV files for technical analysis.
    """
    
    def __init__(self, data_path: str = "data/yfinance_data"):
        """
        Initialize with path to stock CSV files.
        
        Args:
            data_path (str): Path to directory containing stock CSV files
        """
        self.data_path = data_path
        self.data = None
    
    def load_stock_from_csv(self, symbol: str) -> pd.DataFrame:
        """
        Load stock data from individual CSV file.
        
        Args:
            symbol (str): Stock ticker symbol (e.g., 'AAPL')
            
        Returns:
            pd.DataFrame: Stock data with OHLCV columns
        """
        try:
            file_path = os.path.join(self.data_path, f"{symbol}.csv")
            df = pd.read_csv(file_path)
            
            print(f" Loading from: {file_path}")
            print(f" Initial columns: {df.columns.tolist()}")
            print(f" Initial shape: {df.shape}")
            
            # Convert date column to datetime and set as index
            date_column = None
            for col in df.columns:
                if 'date' in col.lower():
                    date_column = col
                    break
            
            if date_column:
                df[date_column] = pd.to_datetime(df[date_column])
                df.set_index(date_column, inplace=True)
                df.index.name = 'Date'
            else:
                print(" No date column found, using default index")
            
            # Ensure we have the required columns (handle different column naming)
            column_mapping = {
                'open': 'Open', 'high': 'High', 'low': 'Low', 
                'close': 'Close', 'volume': 'Volume',
                'adj close': 'Adj Close', 'adj_close': 'Adj Close'
            }
            
            # Rename columns to standard format
            df.columns = [column_mapping.get(col.lower(), col) for col in df.columns]
            
            print(f"🔧 Standardized columns: {df.columns.tolist()}")
            
            required_columns = ['Open', 'High', 'Low', 'Close', 'Volume']
            if not all(col in df.columns for col in required_columns):
                available = df.columns.tolist()
                missing = [col for col in required_columns if col not in available]
                print(f" Missing columns for {symbol}: {missing}")
                print(f"   Available columns: {available}")
            
            # Clean data
            df = df.dropna()
            
            print(f" Loaded {len(df)} days of data for {symbol}")
            return df
            
        except FileNotFoundError:
            print(f" CSV file not found for {symbol} at {self.data_path}")
            return None
        except Exception as e:
            print(f" Error loading data for {symbol}: {e}")
            return None
    
    def load_multiple_stocks(self, symbols: list) -> dict:
        """
        Load multiple stock datasets.
        
        Args:
            symbols (list): List of stock ticker symbols
            
        Returns:
            dict: Dictionary of DataFrames keyed by symbol
        """
        stock_data = {}
        for symbol in symbols:
            print(f"\n{'='*50}")
            print(f"Loading {symbol}...")
            data = self.load_stock_from_csv(symbol)
            if data is not None:
                stock_data[symbol] = data
                print(f" Successfully loaded {symbol}")
            else:
                print(f" Failed to load {symbol}")
            print(f"{'='*50}")
        return stock_data
    
    def get_available_stocks(self) -> list:
        """Get list of available stock CSV files."""
        if not os.path.exists(self.data_path):
            print(f" Directory not found: {self.data_path}")
            return []
        
        csv_files = [f for f in os.listdir(self.data_path) if f.endswith('.csv')]
        stocks = [f.replace('.csv', '') for f in csv_files]
        print(f" Found {len(stocks)} stock files: {stocks}")
        return stocks

    def get_data_summary(self, df: pd.DataFrame) -> dict:
        """Get basic summary statistics of loaded data."""
        if df is None:
            return {}
        
        return {
            'start_date': df.index.min(),
            'end_date': df.index.max(),
            'total_days': len(df),
            'columns': df.columns.tolist(),
            'price_range': f"${df['Close'].min():.2f} - ${df['Close'].max():.2f}",
            'latest_close': f"${df['Close'].iloc[-1]:.2f}",
            'missing_values': df.isnull().sum().to_dict()
        }

# Example usage
if __name__ == "__main__":
    loader = StockDataLoader("data/yfinance_data")
    available = loader.get_available_stocks()
    print(f"Available stocks: {available}")
    
    if available:
        data = loader.load_stock_from_csv(available[0])
        if data is not None:
            print(data.head())
            print(loader.get_data_summary(data))