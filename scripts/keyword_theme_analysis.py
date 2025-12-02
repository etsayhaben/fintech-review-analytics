import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from config.config import ANALYSIS_CSV_PATH
import logging
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Load CSV
df = pd.read_csv(ANALYSIS_CSV_PATH)
logging.info(f"Loaded {len(df)} reviews for theme extraction")

# Ensure 'cleaned' column is string, fill missing with empty string
df['cleaned'] = df['cleaned'].fillna('').astype(str)

# TF-IDF setup
vectorizer = TfidfVectorizer(max_df=0.8, min_df=5, ngram_range=(1,2), stop_words='english')
X = vectorizer.fit_transform(df['cleaned'])
keywords = vectorizer.get_feature_names_out()
logging.info(f"Extracted {len(keywords)} keywords with TF-IDF")

# Function to assign basic theme by keyword match
def assign_theme(text):
    if not isinstance(text, str) or text.strip() == '':
        return 'Other'
    
    text_lower = text.lower()
    if any(k in text_lower for k in ['login', 'password', 'access']):
        return 'Account Access Issues'
    elif any(k in text_lower for k in ['slow', 'lag', 'loading', 'speed']):
        return 'Transaction Performance'
    elif any(k in text_lower for k in ['ui', 'interface', 'design']):
        return 'User Interface & Experience'
    elif any(k in text_lower for k in ['support', 'help', 'customer service']):
        return 'Customer Support'
    elif any(k in text_lower for k in ['feature', 'add', 'tool']):
        return 'Feature Requests'
    else:
        return 'Other'

# Apply theme assignment
df['theme'] = df['cleaned'].apply(assign_theme)

# Save final CSV
df.to_csv(ANALYSIS_CSV_PATH, index=False)
logging.info(f"Keyword and theme analysis saved to {ANALYSIS_CSV_PATH}")
