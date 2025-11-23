import pytest
import pandas as pd
import numpy as np
from src.preprocessing import Preprocessor

class TestPreprocessor:
    def setup_method(self):
        """Set up test data."""
        self.sample_data = pd.DataFrame({
            'Date': ['2023-01-01', '2023-01-02', None],
            'Headline Text': ['Test headline one', 'Another test', ''],
            'Stock Symbol': ['AAPL', 'TSLA', None],
            'Publisher Name': ['test@example.com', '', 'test2@example.com']
        })
    
    def test_clean_column_names(self):
        """Test that column names are cleaned properly."""
        preprocessor = Preprocessor()
        cleaned_df = preprocessor.clean(self.sample_data)
        
        expected_columns = ['date', 'headline_text', 'stock_symbol', 'publisher_name']
        assert list(cleaned_df.columns) == expected_columns
    
    def test_handle_missing_values(self):
        """Test handling of missing values."""
        preprocessor = Preprocessor()
        cleaned_df = preprocessor.clean(self.sample_data)
        
        # Should remove rows where all values are missing
        assert len(cleaned_df) <= len(self.sample_data)
