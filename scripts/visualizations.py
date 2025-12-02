import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from config.config import ANALYSIS_CSV_PATH
import os

df = pd.read_csv(ANALYSIS_CSV_PATH)

os.makedirs("plots", exist_ok=True)

# Sentiment per bank
plt.figure(figsize=(8,6))
sns.countplot(x='sentiment_label', hue='bank', data=df)
plt.title("Sentiment Distribution by Bank")
plt.savefig("plots/sentiment_distribution.png")
plt.close()

# Theme distribution
plt.figure(figsize=(10,6))
sns.countplot(x='theme', hue='bank', data=df)
plt.title("Theme Distribution by Bank")
plt.xticks(rotation=45)
plt.savefig("plots/theme_distribution.png")
plt.close()

# Rating distribution
plt.figure(figsize=(8,6))
sns.countplot(x='rating', hue='bank', data=df)
plt.title("Rating Distribution by Bank")
plt.savefig("plots/rating_distribution.png")
plt.close()

print("[INFO] Plots saved in /plots folder")
