import spacy
from collections import Counter
import pandas as pd

# Load the SpaCy language model
nlp = spacy.load("en_core_web_sm")

# Sample IMDb dataset (replace this with actual file loading)
reviews = [
    {"text": "The movie was amazing, absolutely fantastic!", "sentiment": "positive"},
    {"text": "It was a terrible and ugly experience.", "sentiment": "negative"},
    {"text": "Absolutely grateful for such a masterpiece!", "sentiment": "positive"},
    {"text": "The plot was boring and uninteresting.", "sentiment": "negative"}
]

# Initialize counters for adjectives
positive_adjectives = Counter()
negative_adjectives = Counter()

# Process each review
for review in reviews:
    doc = nlp(review["text"])
    sentiment = review["sentiment"]
    for token in doc:
        if token.pos_ == "ADJ":  # Check if the token is an adjective
            if sentiment == "positive":
                positive_adjectives[token.text.lower()] += 1
            elif sentiment == "negative":
                negative_adjectives[token.text.lower()] += 1

# Combine results
all_adjectives = set(positive_adjectives.keys()).union(set(negative_adjectives.keys()))
results = [
    {"word": adj, "negative": negative_adjectives[adj], "positive": positive_adjectives[adj]}
    for adj in all_adjectives
]

# Convert to a DataFrame for better visualization
df = pd.DataFrame(results).sort_values(by="word")
print(df)
