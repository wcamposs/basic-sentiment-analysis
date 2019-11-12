import nltk
import pandas as pd


dataset = ["Food is good and not too expensive. Serving is just right for adult. Ambient is nice too.", 
"Used to be good. Chicken soup was below average, bbq used to be good.", 
"Food was good, standouts were the spicy beef soup and seafood pancake!",
"Good office lunch or after work place to go with a big group as they have a lot of private areas with large tables",
"As a Korean person, it was very disappointing food quality and very pricey for what you get. I won't go back there again.",
"Not great quality food for the price. Average food at premium prices really.",
"Fast service. Prices are reasonable and food is decent.",
"Extremely long waiting time. Food is decent but definetively not worth the wait.",
"Clean premises, tasty food. My family favourites are the clear Tom yum soup, suffed chicken wings, chargrilled squid.",
"Really good and authentic Thai food! In particular, we loved their tom yup clear soup with sliced fish. It's so well balanced that we can have it just on it own."]

nltk.download('vader_lexicon')

def nltk_sentiment(sentence):
    from nltk.sentiment.vader import SentimentIntensityAnalyzer

    nltk_sentiment = SentimentIntensityAnalyzer()
    score = nltk_sentiment.polarity_scores(sentence)
    return(score)

nltk_results = [nltk_sentiment(row) for row in dataset]
results_df = pd.DataFrame(nltk_results)
text_df = pd.DataFrame(dataset, columns = ['text'])
nltk_df = text_df.join(results_df)

print(nltk_df)