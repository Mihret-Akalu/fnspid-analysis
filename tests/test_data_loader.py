import pytest
import pandas as pd
import os
from src.data_loader import DataLoader

class TestDataLoader:
    def test_data_loader_initialization(self):
        """Test that DataLoader initializes correctly."""
        loader = DataLoader('data/sample_financial_news.csv')
        assert loader.filepath == 'data/sample_financial_news.csv'
    
    def test_load_sample_data(self):
        """Test loading sample data."""
        try:
            loader = DataLoader('data/sample_financial_news.csv')
            df = loader.load_data()
            assert isinstance(df, pd.DataFrame)
            assert len(df) > 0
            expected_columns = ['date', 'headline', 'stock', 'publisher', 'url']
            for col in expected_columns:
                assert col in df.columns
        except FileNotFoundError:
            pytest.skip("Sample data file not available")
    
    def test_file_not_found(self):
        """Test handling of missing file."""
        loader = DataLoader('nonexistent_file.csv')
        with pytest.raises(FileNotFoundError):
            loader.load_data()
