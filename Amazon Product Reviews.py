import spacy
from spacy import displacy
import random

print("=== NLP Analysis with spaCy ===\n")

# Load spaCy model
print("Loading spaCy model...")
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Please install the model first: python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

# Sample Amazon reviews data
reviews = [
    "I absolutely love my new iPhone 14 Pro from Apple. The camera quality is amazing and battery life lasts all day!",
    "This Samsung Galaxy S23 is terrible. The screen cracked after one week and customer service was horrible.",
    "My Google Pixel 7 arrived yesterday and I'm already impressed with the Android experience.",
    "Don't buy this Huawei phone! It stopped working after 2 months and the warranty is useless.",
    "The Microsoft Surface Pro is fantastic for work. Great performance with Intel processor.",
    "This Sony headphones broke in one month. Very disappointed with the quality.",
    "Amazing Dell laptop! The performance is incredible and the design is sleek.",
    "Poor quality product from Acer. Keyboard stopped working and technical support is non-existent."
]

print("--- Named Entity Recognition (NER) ---\n")

# Sentiment analysis using rule-based approach
def rule_based_sentiment(text):
    """
    Simple rule-based sentiment analysis
    """
    positive_words = ['love', 'amazing', 'fantastic', 'great', 'impressed', 'incredible', 'excellent', 'awesome']
    negative_words = ['terrible', 'horrible', 'useless', 'disappointed', 'poor', 'broken', 'cracked']
    
    doc = nlp(text.lower())
    positive_count = sum(1 for token in doc if token.text in positive_words)
    negative_count = sum(1 for token in doc if token.text in negative_words)
    
    if positive_count > negative_count:
        return "POSITIVE"
    elif negative_count > positive_count:
        return "NEGATIVE"
    else:
        return "NEUTRAL"

# Analyze each review
for i, review in enumerate(reviews, 1):
    print(f"\n--- Review {i} ---")
    print(f"Text: {review}")
    
    # Process with spaCy
    doc = nlp(review)
    
    # Extract entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]
    print(f"Entities: {entities}")
    
    # Extract product names and brands
    products_brands = [(ent.text, ent.label_) for ent in doc.ents 
                      if ent.label_ in ['ORG', 'PRODUCT']]
    print(f"Products/Brands: {products_brands}")
    
    # Sentiment analysis
    sentiment = rule_based_sentiment(review)
    print(f"Sentiment: {sentiment}")
    
    # POS tagging for first few tokens
    print("Key POS tags:")
    for token in doc[:8]:  # Show first 8 tokens
        print(f"  {token.text}: {token.pos_}")

# Visualize NER for a sample review
print("\n--- NER Visualization ---")
sample_review = reviews[0]
doc = nlp(sample_review)
displacy.render(doc, style="ent", jupyter=True)

# Advanced analysis
print("\n--- Advanced NLP Analysis ---")
for review in random.sample(reviews, 3):
    doc = nlp(review)
    
    print(f"\nReview: {review}")
    print("Dependency Analysis (key relations):")
    
    # Find subject-verb-object relations
    for token in doc:
        if token.dep_ in ["nsubj", "dobj"] and token.head.pos_ == "VERB":
            print(f"  {token.text} --{token.dep_}--> {token.head.text}")
    
    # Lemmatization
    print("Key lemmas:")
    unique_lemmas = set(token.lemma_ for token in doc if token.is_alpha and not token.is_stop)
    print(f"  {list(unique_lemmas)[:5]}...") 
