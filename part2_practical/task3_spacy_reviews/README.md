# Task 2.3: NLP Analysis of Amazon Reviews with spaCy

## Overview
This module demonstrates the use of the `spaCy` library for two core NLP tasks:
1.  **Named Entity Recognition (NER)** to extract product and brand names.
2.  A **rule-based sentiment analysis** to classify reviews as positive, negative, or neutral.

## Files in this Directory
- `spacy_ner_sentiment.ipynb`: A Jupyter Notebook that walks through the process of setting up spaCy, performing NER, and implementing the custom sentiment logic.

## How to Run
1. Ensure you have the project's dependencies, especially `spacy`, installed.
2. **Download the spaCy model:** Before running the notebook, execute the following command in your terminal:
   ```bash
   python -m spacy download en_core_web_sm