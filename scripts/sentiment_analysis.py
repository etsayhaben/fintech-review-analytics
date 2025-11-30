import pandas as pd
from transformers import pipeline
from config.config import CLEAN_CSV_PATH, ANALYSIS_CSV_PATH

df = pd.read_csv(CLEAN_CSV_PATH)

# Simple sentiment analysis
sentiment_model = pipeline("sentiment-analysis")
df['sentiment'] = df['cleaned'].apply(lambda x: sentiment_model(str(x))[0]['label'])

# Save analysis CSV
df.to_csv(ANALYSIS_CSV_PATH, index=False)
print(f"Saved sentiment analysis to {ANALYSIS_CSV_PATH}")
