from textblob import TextBlob

# Test karne ke liye sentences
sentences = [
    "I love this project, it is amazing!",
    "This is the worst experience ever, I hate it.",
    "The product is okay, not too good but not bad."
]

for text in sentences:
    analysis = TextBlob(text)
    
    # Sentiment polarity check karna (-1 se +1)
    if analysis.sentiment.polarity > 0:
        sentiment = "Positive"
    elif analysis.sentiment.polarity < 0:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
        
    print(f"Text: {text} | Sentiment: {sentiment}")