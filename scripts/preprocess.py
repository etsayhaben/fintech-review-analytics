import pandas as pd
import spacy
from config.config import RAW_CSV_PATH, CLEAN_CSV_PATH

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Load raw reviews
df = pd.read_csv(RAW_CSV_PATH)
print(f"Loaded {len(df)} raw reviews")

# Remove duplicates
df.drop_duplicates(subset=['review', 'bank'], inplace=True)

# Normalize dates
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Function to clean text: lemmatization + remove stopwords + keep alpha words
def clean_text(text):
    doc = nlp(str(text))
    return " ".join([token.lemma_ for token in doc if token.is_alpha and not token.is_stop])

# Apply cleaning
df['cleaned'] = df['review'].apply(clean_text)

# Save cleaned reviews
df.to_csv(CLEAN_CSV_PATH, index=False)
print(f"Saved cleaned reviews to {CLEAN_CSV_PATH}")
