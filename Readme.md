# Customer Experience Analytics for Fintech Apps

A Real-World Data Engineering Challenge: Scraping, Analyzing, and Visualizing Google Play Store Reviews for Ethiopian Banks.

---

## **Project Overview**

This project analyzes customer satisfaction with mobile banking apps from three Ethiopian banks:

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia (BOA)**
- **Dashen Bank**

We scraped Google Play Store reviews, analyzed sentiments and themes, and generated visualizations and actionable insights to help banks improve app performance and customer experience.

---

## **Business Objective**

Omega Consultancy aims to help banks:

- Identify satisfaction drivers (e.g., speed, UI quality) and pain points (e.g., crashes, login errors).  
- Improve user retention and app features.  
- Enhance support and operational efficiency.

---

## **Project Structure**

fintech-review-analytics/
│
├─ data/
│ └─ cleaned_reviews.csv # Cleaned review dataset
│
├─ plots/ # Generated plots
│ ├─ all_banks_sentiment_distribution.png
│ ├─ all_banks_theme_distribution.png
│ └─ <per-bank folders>/
│ └─ bank_name_plots.png
│
├─ reports/ # Generated reports
│ ├─ all_banks_sentiment_counts.csv
│ ├─ all_banks_mean_sentiment.csv
│ ├─ all_banks_theme_counts.csv
│ └─ <per-bank folders>/
│ └─ sentiment, theme, keywords CSVs and summary TXT
│
├─ scripts/ # Python scripts
│ ├─ scraping.py
│ ├─ preprocessing.py
│ ├─ sentiment_analysis.py
│ ├─ theme_analysis.py
│ ├─ db_insert.py
│ └─ visualization.py
│
├─ requirements.txt # Python dependencies
├─ README.md # Project documentation
├─ final_report.pdf # Stakeholder report
└─ .gitignore

yaml
Copy code

---

## **Key Tasks & Branches**

| Task | Branch | Description |
|------|--------|-------------|
| Task 1 | task-1 | Scrape and preprocess reviews from Google Play Store. |
| Task 2 | task-2 | Sentiment analysis & thematic keyword extraction. |
| Task 3 | task-3 | Insert cleaned data into PostgreSQL database. |
| Task 4 | task-4 | Generate visualizations, reports, and insights. |
| Final Submission | main | Merge all tasks, ready-to-submit final repository. |

---

## **Getting Started**

### **1. Clone the Repository**

```bash
git clone <repository_url>
cd fintech-review-analytics
2. Create a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
Scripts Overview
scraping.py: Scrapes reviews from Google Play Store.

preprocessing.py: Cleans data, removes duplicates, normalizes dates.

sentiment_analysis.py: Computes sentiment labels and scores.

theme_analysis.py: Extracts keywords and clusters into themes.

db_insert.py: Inserts data into PostgreSQL tables.

visualization.py: Generates plots and per-bank reports.

Database Schema
Banks Table

Column	Type	Description
bank_id	INT PK	Bank identifier
bank_name	TEXT	Bank name
app_name	TEXT	App name

Reviews Table

Column	Type	Description
review_id	INT PK	Review identifier
bank_id	INT FK	Linked bank
review_text	TEXT	Review content
rating	INT	Star rating 1-5
review_date	DATE	Review posting date
sentiment_label	TEXT	Positive / Neutral / Negative
sentiment_score	FLOAT	Numeric sentiment score
theme	TEXT	Identified theme
source	TEXT	Review source (Google Play)

Reports & Plots
All CSV reports are saved in the reports/ folder.

All visualizations are saved in the plots/ folder.

Per-bank reports include sentiment counts, mean sentiment score, theme counts, and keywords per theme.

Overall reports summarize all banks together.

Final Deliverables
GitHub Repository with code, scripts, CSV data, and reports.

Plots for sentiment and theme distribution (overall + per bank).

final_report.pdf: 10-page stakeholder report with insights and actionable recommendations.

PostgreSQL database scripts to recreate tables and insert data.

How to Run
bash
Copy code
# Preprocess data
python scripts/preprocessing.py

# Run sentiment analysis
python scripts/sentiment_analysis.py

# Run theme analysis
python scripts/theme_analysis.py

# Insert into PostgreSQL
python scripts/db_insert.py

# Generate plots and reports
python scripts/visualization.py
Authors & Contributors
Kerod

Mahbubah

Filimon

Facilitated by Omega Consultancy.

References
google-play-scraper PyPI

Pandas Documentation

VADER Sentiment Analysis

TextBlob

spaCy

Transformers Pipeline

PostgreSQL Documentation

yaml
Copy code

---

This README is **complete for final submission**. It documents:

- Project overview and objectives  
- Repository structure  
- Branch strategy and tasks  
- How to run scripts  
- Database schema  
- Plots and reports organization  
- References  

---

I can now create a **final Git commit plan** showing exactly what to commit and in what order so you can