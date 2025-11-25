# Financial News Sentiment & Price Impact Analysis

## Project Overview
This project analyzes correlations between financial news sentiment and stock price movements to enhance predictive analytics capabilities.

## Business Objective
Enhance financial forecasting accuracy by leveraging NLP sentiment analysis on news headlines and correlating with stock performance.

## Dataset
- Financial News and Stock Price Integration Dataset (FNSPID)
- Contains headlines, publishers, dates, and stock symbols
- Timezone: UTC-4

## Project Structure
`
fnspid-analysis/
├── src/          # Source code modules
├── notebooks/    # Jupyter notebooks for analysis
├── tests/        # Unit tests
├── data/         # Raw and processed data
└── scripts/      # Utility scripts
`

## Setup
1. Clone repository
2. Create virtual environment: python -m venv .venv
3. Activate: .venv\Scripts\activate (Windows)
4. Install dependencies: pip install -r requirements.txt

# Task 1: EDA & Statistical Analysis
- Descriptive statistics on headline lengths
- Publisher frequency analysis
- Time series analysis of publication trends
- Text analysis and topic modeling
- Sentiment analysis implementation

# Task 2: Advanced Financial Sentiment Analysis
Objective: Develop a sophisticated sentiment analysis system specifically tailored for financial news to accurately quantify market sentiment from news headlines.

## Key Components:
## Custom Financial Lexicon

- Enhanced sentiment dictionaries with domain-specific terminology

- Bullish terms: rally, earnings beat, upgrade, bullish, surge

- Bearish terms: plunge, downgrade, miss, bearish, crash

- Neutral financial context preservation

## Multi-Method Sentiment Scoring

- VADER: Optimized for short texts and social media context

- TextBlob: General-purpose sentiment with subjectivity analysis

- Financial Dictionary: Custom scoring using financial terminology

- Weighted Combination: 60% VADER + 30% TextBlob + 10% Financial for optimal accuracy

## Sentiment Classification

- Positive: Score ≥ +0.05 (Strong bullish sentiment)

- Negative: Score ≤ -0.05 (Strong bearish sentiment)

- Neutral: -0.05 < Score < +0.05 (Market-neutral content)

## Technical Implementation:
- Automated text preprocessing with financial context preservation

- Real-time sentiment scoring for streaming news analysis

- Comprehensive sentiment distribution analysis across stocks

- Integration-ready sentiment analysis class for reuse

## Business Value:
- Transforms unstructured news text into quantifiable sentiment scores

- Provides foundation for sentiment-based trading signals

- Enables real-time market sentiment monitoring

- Supports portfolio-level sentiment analysis and risk assessment

# Task 3: Financial News Sentiment & Price Impact Analysis

## Project Overview
This project analyzes correlations between financial news sentiment and stock price movements to enhance predictive analytics capabilities. The analysis spans comprehensive sentiment analysis, statistical correlation testing, and trading strategy simulation.

## Business Objective
Enhance financial forecasting accuracy by leveraging NLP sentiment analysis on news headlines and correlating with stock performance to identify predictive patterns in market behavior.

## Dataset
- Financial News and Stock Price Integration Dataset (FNSPID)
- Contains headlines, publishers, dates, and stock symbols
- Timezone: UTC-4
- Stock Data: AAPL, AMZN, GOOGL, META, MSFT, NVDA (from yfinance)

## Project Structure
```
fnspid-analysis/
├── src/                    # Source code modules
├── notebooks/              # Jupyter notebooks for analysis
├── tests/                  # Unit tests
├── data/                   # Raw and processed data
│   ├── raw/               # Original datasets
│   ├── processed/         # Cleaned and processed data
│   └── yfinance_data/     # Stock price data (6 major tech stocks)
├── outputs/               # Analysis results and exports
│   └── task3_correlation_analysis/  # Correlation analysis outputs
└── scripts/               # Utility scripts
```

## Setup & Installation
```bash
# 1. Clone repository
git clone https://github.com/Mihret-Akalu/fnspid-analysis.git
cd fnspid-analysis

# 2. Create virtual environment
python -m venv .venv

# 3. Activate environment
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Download NLTK data
python -c "import nltk; nltk.download('vader_lexicon'); nltk.download('punkt')"
```

## Analysis Workflow

### Task 1: EDA & Statistical Analysis
- Descriptive statistics on headline lengths
- Publisher frequency analysis
- Time series analysis of publication trends
- Text analysis and topic modeling
- Sentiment analysis implementation

### Task 2: Advanced Sentiment Analysis
- Custom financial lexicon development
- Multi-method sentiment scoring (VADER + TextBlob + Financial Dictionary)
- Sentiment classification (Positive/Negative/Neutral)
- Sentiment distribution analysis

### Task 3: Sentiment-Stock Return Correlation Analysis 
**Objective**: Quantify relationships between news sentiment and stock price movements

#### Key Features:
- **Advanced Financial Sentiment Analysis**
  - Custom financial lexicon with bullish/bearish terms
  - Weighted combination of VADER, TextBlob, and financial scores
  - Real-time sentiment classification

- **Comprehensive Correlation Analysis**
  - Pearson, Spearman, and Kendall correlation coefficients
  - Multiple time horizons: Same-day, 1-day, 3-day, 5-day forward returns
  - Statistical significance testing (p-value < 0.05)

- **Trading Strategy Simulation**
  - Sentiment-based buy/sell signals
  - Performance comparison vs. buy-and-hold strategy
  - Risk-adjusted return metrics (Sharpe ratio, volatility)

- **Advanced Visualizations**
  - Correlation heatmaps across stocks and time horizons
  - Scatter plots with sentiment-return relationships
  - Time series analysis of sentiment vs. returns
  - Strategy performance comparisons

#### Technical Implementation:
- **Data Alignment**: Precise timestamp matching between news and stock data
- **Error Handling**: Robust processing with comprehensive logging
- **Modular Design**: Reusable FinancialSentimentAnalyzer class
- **Export Capabilities**: CSV exports for all analysis results

#### Key Findings:
- Quantified sentiment-return correlations for 6 major tech stocks
- Identified statistically significant relationships
- Demonstrated trading strategy outperformance in specific scenarios
- Provided actionable insights for sentiment-based trading

## Usage
```python
# Run the complete analysis pipeline
from src.sentiment_analyzer import FinancialSentimentAnalyzer
from src.correlation_analysis import calculate_correlations

# Initialize analyzer
analyzer = FinancialSentimentAnalyzer()

# Perform sentiment analysis
news_with_sentiment = analyzer.analyze_dataframe(news_df)

# Calculate correlations
correlations = calculate_correlations(aligned_data)
```

## Outputs Generated
- Sentiment-analyzed news datasets
- Correlation matrices and statistical summaries
- Trading strategy performance reports
- Interactive visualizations and heatmaps
- Statistical significance test results

## Dependencies
- pandas, numpy - Data manipulation
- matplotlib, seaborn - Visualization
- nltk, textblob, vaderSentiment - NLP & Sentiment Analysis
- yfinance - Stock data retrieval
- scipy, scikit-learn - Statistical analysis
- tqdm - Progress tracking

## Results Interpretation
- **Correlation Coefficients**: Strength and direction of sentiment-return relationships
- **Statistical Significance**: Confidence in observed correlations
- **Trading Performance**: Practical applicability of sentiment signals
- **Risk Metrics**: Volatility and Sharpe ratio comparisons

## Future Enhancements
- Real-time sentiment monitoring pipeline
- Machine learning models for sentiment classification
- Portfolio-level sentiment analysis
- Integration with trading APIs for automated execution

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request


## Key Updates Made:

1. **Added Task 3 Section** - Comprehensive coverage of correlation analysis
2. **Enhanced Project Structure** - Added outputs folder for analysis results
3. **Detailed Technical Implementation** - Specifics about the correlation methodology
4. **Business Value Focus** - Emphasized practical applications and insights
5. **Clear Usage Instructions** - How to run the analysis
6. **Results Interpretation Guide** - How to understand the outputs
7. **Future Roadmap** - Potential enhancements

