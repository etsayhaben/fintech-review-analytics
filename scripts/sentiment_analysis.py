import pandas as pd
from transformers import pipeline
from config.config import CLEAN_CSV_PATH, ANALYSIS_CSV_PATH
import logging
from tqdm import tqdm
import os

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

df = pd.read_csv(CLEAN_CSV_PATH)
logging.info(f"Loaded {len(df)} cleaned reviews")

# Remove empty reviews
df.dropna(subset=['cleaned'], inplace=True)
logging.info(f"After dropping empty reviews: {len(df)} rows")

# Sentiment pipeline
sentiment_model = pipeline("sentiment-analysis")

labels, scores = [], []
for text in tqdm(df['cleaned'], desc="Analyzing sentiment"):
    try:
        result = sentiment_model(str(text)[:512])[0]
        labels.append(result['label'])
        scores.append(result['score'])
    except:
        labels.append("ERROR")
        scores.append(0.0)

df['sentiment_label'] = labels
df['sentiment_score'] = scores

os.makedirs(os.path.dirname(ANALYSIS_CSV_PATH), exist_ok=True)
df.to_csv(ANALYSIS_CSV_PATH, index=False)
logging.info(f"Sentiment analysis saved to {ANALYSIS_CSV_PATH}")

bank_counts = df.groupby('bank')['review'].count()
logging.info(f"Reviews per bank:\n{bank_counts}")
