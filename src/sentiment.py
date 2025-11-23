from textblob import TextBlob

def compute_sentiment(text: str) -> float:
    """
    Compute simple sentiment polarity of a text using TextBlob.
    
    Args:
        text (str): Input text for sentiment analysis
        
    Returns:
        float: Polarity score in range [-1, 1]
            -1 = very negative, 0 = neutral, 1 = very positive
    """
    if not isinstance(text, str) or text.strip() == "":
        return 0.0  # Return neutral for empty/missing text
    
    try:
        blob = TextBlob(text)
        return blob.sentiment.polarity
    except Exception:
        return 0.0  # Fallback for any processing errors