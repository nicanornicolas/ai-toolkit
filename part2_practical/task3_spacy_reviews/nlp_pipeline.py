import spacy

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
    """Analyzes sentiment using a simple rule-based approach."""
    text_lower = text.lower()
    
    positive_keywords = ["love", "great", "amazing", "excellent", "best", "perfect"]
    negative_keywords = ["hate", "terrible", "awful", "bad", "disappointed", "worst"]
    
    has_positive = any(keyword in text_lower for keyword in positive_keywords)
    has_negative = any(keyword in text_lower for keyword in negative_keywords)
    
    if has_positive and not has_negative:
        return "positive"
    elif has_negative and not has_positive:
        return "negative"
    else:
        # If both or neither are present, classify as neutral
        return "neutral"