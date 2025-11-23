import pytest
from src.sentiment import compute_sentiment

class TestSentiment:
    def test_sentiment_positive_text(self):
        """Test sentiment analysis with positive text."""
        text = "This is excellent and amazing news!"
        sentiment = compute_sentiment(text)
        assert isinstance(sentiment, float)
        assert -1 <= sentiment <= 1
    
    def test_sentiment_negative_text(self):
        """Test sentiment analysis with negative text."""
        text = "This is terrible and awful news"
        sentiment = compute_sentiment(text)
        assert isinstance(sentiment, float)
        assert -1 <= sentiment <= 1
    
    def test_sentiment_empty_string(self):
        """Test sentiment analysis with empty string."""
        sentiment = compute_sentiment("")
        assert sentiment == 0.0
    
    def test_sentiment_none_input(self):
        """Test sentiment analysis with None input."""
        sentiment = compute_sentiment(None)
        assert sentiment == 0.0
