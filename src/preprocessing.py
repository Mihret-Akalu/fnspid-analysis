import pandas as pd

class Preprocessor:
    """
    Basic preprocessing utilities:
    - handle missing values
    - standardize column names
    - data type conversions
    """
    def __init__(self):
        pass

    def clean(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Standardize column names and handle missing values.

        Args:
            df (pd.DataFrame): Raw input data

        Returns:
            pd.DataFrame: Cleaned data
        """
        df = df.copy()
        
        # Standardize column names: lowercase, replace spaces with underscores
        df.columns = [c.strip().lower().replace(" ", "_") for c in df.columns]
        
        # Drop rows with all missing values
        df = df.dropna(how='all')
        
        print(f"✓ Data cleaned: {df.shape[0]} rows remaining")
        return df
    
    def handle_datetime(self, df: pd.DataFrame, date_column: str = 'date') -> pd.DataFrame:
        """
        Convert date column to datetime and handle timezones.
        
        Args:
            df (pd.DataFrame): Input data
            date_column (str): Name of date column
            
        Returns:
            pd.DataFrame: Data with proper datetime handling
        """
        df = df.copy()
        
        # Convert to datetime
        df[date_column] = pd.to_datetime(df[date_column], errors='coerce')
        
        # Handle timezone (dataset uses UTC-4)
        if df[date_column].dt.tz is not None:
            df['date_local'] = df[date_column].dt.tz_convert('Etc/GMT+4')
        else:
            df['date_local'] = df[date_column].dt.tz_localize('UTC').dt.tz_convert('Etc/GMT+4')
        
        df['date_utc'] = df['date_local'].dt.tz_convert('UTC')
        
        return df