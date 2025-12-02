import pandas as pd
import psycopg2
from config.config import ANALYSIS_CSV_PATH, POSTGRES

# Load analysis CSV
df = pd.read_csv(ANALYSIS_CSV_PATH)
print(f"[INFO] Loaded {len(df)} reviews from {ANALYSIS_CSV_PATH}")

# Fill missing values if needed
df['sentiment'] = df['sentiment'].fillna('Neutral')
df['theme'] = df['theme'].fillna('Other')

# Connect to PostgreSQL
conn = psycopg2.connect(
    host=POSTGRES['host'],
    port=POSTGRES['port'],
    dbname=POSTGRES['db'],
    user=POSTGRES['user'],
    password=POSTGRES['password'],
    sslmode=POSTGRES['sslmode']
)
cur = conn.cursor()

# Create tables
cur.execute("""
CREATE TABLE IF NOT EXISTS banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name TEXT UNIQUE,
    app_name TEXT
);
""")
cur.execute("""
CREATE TABLE IF NOT EXISTS reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating INT,
    review_date DATE,
    sentiment_label TEXT,
    sentiment_score FLOAT,
    theme TEXT,
    source TEXT
);
""")
conn.commit()

# Insert banks
banks = df['bank'].unique()
for bank in banks:
    cur.execute("""
        INSERT INTO banks (bank_name, app_name) 
        VALUES (%s,%s) 
        ON CONFLICT (bank_name) DO NOTHING;
    """, (bank, bank))
conn.commit()

# Insert reviews
for _, row in df.iterrows():
    cur.execute("""
        INSERT INTO reviews (
            bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, theme, source
        ) VALUES (
            (SELECT bank_id FROM banks WHERE bank_name=%s),
            %s, %s, %s, %s, %s, %s, %s
        );
    """, (
        row['bank'], 
        row['review'], 
        row['rating'], 
        row['date'], 
        row['sentiment'], 
        None,            # sentiment_score, can compute later
        row['theme'], 
        row['source']
    ))
conn.commit()
cur.close()
conn.close()
print("[INFO] Data inserted into PostgreSQL database")
