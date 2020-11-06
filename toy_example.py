from textblob import TextBlob
def sentiment(x):
    return TextBlob(x).sentiment.polarity