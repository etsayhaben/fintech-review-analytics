import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# ---------- PATHS ----------
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")

RAW_CSV_PATH = os.path.join(DATA_RAW, "reviews_raw.csv")
CLEAN_CSV_PATH = os.path.join(DATA_PROCESSED, "reviews_clean.csv")
ANALYSIS_CSV_PATH = os.path.join(DATA_PROCESSED, "reviews_analysis.csv")

# ---------- GOOGLE PLAY APP IDs ----------
APP_IDS = {
    "CBE": "com.combanketh.mobilebanking",
    "BOA": "com.boa.boaMobileBanking",
    "DASHEN": "com.dashen.dashensuperapp",
   
}

# ---------- DATABASE CONFIG ----------
POSTGRES = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": int(os.getenv("POSTGRES_PORT", 5432)),
    "db": os.getenv("POSTGRES_DB", "bank_reviews"),
    "user": os.getenv("POSTGRES_USER", "postgres"),
    "password": os.getenv("POSTGRES_PASSWORD", ""),
    "sslmode": os.getenv("POSTGRES_SSLMODE", "require")
}

# ---------- PROJECT CONSTANTS ----------
REVIEW_LIMIT = 500  # per bank
LANGUAGE = "en"
COUNTRY = "us"
