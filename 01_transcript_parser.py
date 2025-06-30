# scripts/01_transcript_parser.py

import os
import re
import pandas as pd
from utils.cleaner import clean_text
from utils.stopwords_fr import STOPWORDS_FR

# Paths
INPUT_PATH = "../data/raw_transcripts/2024-06-29_transcript_openai.txt"
OUTPUT_PATH = "../data/parsed_output/cleaned_tokens.csv"

# Load transcript
with open(INPUT_PATH, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Clean and preprocess
cleaned = clean_text(raw_text)
tokens = re.findall(r"\b\w+\b", cleaned.lower())
tokens = [t for t in tokens if t not in STOPWORDS_FR]

# Save to CSV
pd.DataFrame(tokens, columns=["token"]).to_csv(OUTPUT_PATH, index=False)
print(f"Saved {len(tokens)} tokens to {OUTPUT_PATH}")
