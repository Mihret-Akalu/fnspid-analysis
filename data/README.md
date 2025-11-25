# Data Directory Structure

## Overview
This directory contains financial news datasets for sentiment analysis and correlation studies with stock prices.

## Files

### Raw Data (Gitignored - Not tracked in repository)
- aw/raw_analyst_ratings.csv (327 MB) - Full financial news dataset
  - Contains: 300,000+ financial news articles
  - Date range: 2020-2023
  - Sources: Multiple financial news publishers
  - Columns: date, headline, stock, publisher, url

### Sample Data (Included in repository)
- sample_financial_news.csv (2 KB) - Demonstration dataset
  - Contains: 20 sample financial news articles
  - Demonstrates: Data structure and analysis capabilities
  - Used for: Code testing and documentation

## Dataset Schema

| Column | Type | Description |
|--------|------|-------------|
| date | datetime | Publication date and time (UTC-4) |
| headline | string | News article headline |
| stock | string | Stock ticker symbol (e.g., AAPL, TSLA) |
| publisher | string | News publisher/author (email format) |
| url | string | Link to full article |

## Usage

### For Development
1. Use sample_financial_news.csv for testing and development
2. The EDA notebook automatically detects and uses available datasets

### For Full Analysis
1. Ensure aw_analyst_ratings.csv is placed in data/raw/
2. The file is automatically excluded from Git via .gitignore
3. Run analysis notebooks to process the full dataset

## Data Sources
- Financial News and Stock Price Integration Dataset (FNSPID)
- Multiple financial news outlets and publishers
- Stock ticker symbols from major exchanges

## Notes
- All datetime values are in UTC-4 timezone
- Stock symbols are normalized to uppercase
- Publisher information may contain email addresses
- URLs point to original article sources
