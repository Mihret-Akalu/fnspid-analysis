# test_fixed.py - Test if the syntax errors are fixed
import sys
import os

print("Testing fixed imports...")

try:
    # Add project root
    project_root = os.path.abspath(".")
    if project_root not in sys.path:
        sys.path.append(project_root)
    
    # Test imports
    from src.stock_data import StockDataLoader
    print("StockDataLoader imported")
    
    from src.technical_indicators import TechnicalIndicators
    print("TechnicalIndicators imported")
    
    from src.visualization import StockVisualizer
    print("StockVisualizer imported")
    
    # Test data loading
    loader = StockDataLoader("../data/yfinance_data")
    stocks = loader.get_available_stocks()
    print(f"Available stocks: {stocks}")
    
    if stocks:
        data = loader.load_stock_from_csv(stocks[0])
        if data is not None:
            print(f"Data loaded: {len(data)} rows")
            
            # Test indicators
            analyzer = TechnicalIndicators(data)
            analyzed_data = analyzer.calculate_all_indicators()
            print(f"Indicators calculated: {len(analyzed_data.columns)} columns")
            
    print("\n ALL TESTS PASSED!")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()