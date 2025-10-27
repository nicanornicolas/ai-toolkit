import spacy
import re

# It's efficient to load the model once
# NOTE: You need to have the model downloaded! Run: python -m spacy download en_core_web_sm
try:
    NLP_MODEL = spacy.load("en_core_web_sm")
except OSError:
    print("Downloading spaCy model 'en_core_web_sm'...")
    from spacy.cli import download
    download("en_core_web_sm")
    NLP_MODEL = spacy.load("en_core_web_sm")

def extract_entities(text: str):
    """Extracts named entities (like product names and brands) from text."""
    doc = NLP_MODEL(text)
    entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ["PRODUCT", "ORG"]]
    return entities

def analyze_sentiment_rule_based(text: str) -> str:
    """Analyzes sentiment using a more robust rule-based approach by counting keywords."""
    positive_words = {"good", "great", "amazing", "love", "excellent", "fantastic", "best", "awesome", "wonderful"}
    negative_words = {"bad", "terrible", "awful", "hate", "poor", "worst", "disappointed", "boring", "horrible"}

    # Normalize the text and find all words
    words = re.findall(r"\b\w+\b", text.lower())

    pos_count = sum(word in positive_words for word in words)
    neg_count = sum(word in negative_words for word in words)

    # Determine sentiment based on the word count comparison
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    else:
        # If counts are equal (including 0 vs 0), it's neutral
        return "neutral"