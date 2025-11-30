import pandas as pd
from google_play_scraper import reviews
from config.config import APP_IDS, RAW_CSV_PATH, REVIEW_LIMIT, LANGUAGE, COUNTRY

all_reviews = []

for bank, app_id in APP_IDS.items():
    print(f"Scraping {bank} reviews...")
    result, _ = reviews(app_id, count=REVIEW_LIMIT, lang=LANGUAGE, country=COUNTRY)
    for r in result:
        all_reviews.append({
            "bank": bank,
            "review": r["content"],
            "rating": r["score"],
            "date": r["at"],
            "source": "Google Play"
        })

df = pd.DataFrame(all_reviews)

# Remove duplicates
df.drop_duplicates(subset=['review', 'bank'], inplace=True)

# Normalize dates
df['date'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m-%d')

# Save raw CSV
df.to_csv(RAW_CSV_PATH, index=False)
print(f"Saved raw reviews to {RAW_CSV_PATH}")
