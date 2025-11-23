import pandas as pd

class DataLoader:
    """
    Load raw CSV datasets into pandas DataFrames.
    Handles file reading and basic validation.
    """
    def __init__(self, filepath: str):
        self.filepath = filepath

    def load_data(self) -> pd.DataFrame:
        """
        Load CSV data into a DataFrame with error handling.
        
        Returns:
            pd.DataFrame: Loaded dataset
            
        Raises:
            FileNotFoundError: If the file doesn't exist
            pd.errors.EmptyDataError: If file is empty
        """
        try:
            df = pd.read_csv(self.filepath)
            print(f"✓ Data loaded successfully: {df.shape[0]} rows, {df.shape[1]} columns")
            return df
        except FileNotFoundError:
            print(f"✗ Error: File {self.filepath} not found")
            raise
        except pd.errors.EmptyDataError:
            print("✗ Error: File is empty")
            raise